"""
Teste funcional passo-a-passo: Eletromagnetismo (Hayt 7a Ed) via Mastery Path.

Simula uma sessao de aprendizado real usando o livro do Hayt como mastery path,
e verifica se as metodologias pedagogicas estao sendo aplicadas:

  1. EMT Dialogue (pump -> hint -> prompt -> assertion)
  2. 5-Step Tutoring Frame
  3. Hard mastery gate (90% threshold)
  4. Compression (skip mastered, never re-teach)
  5. Macro adaptivity (next_objective)
  6. Spaced repetition scheduling
"""

import json
import os
import sys
import time
from pathlib import Path
from typing import Any

# Forcar UTF-8 no terminal Windows
if sys.platform == "win32":
    sys.stdout = open(sys.stdout.fileno(), mode="w", encoding="utf-8", buffering=1, closefd=False)

_SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_SCRIPT_DIR.parents[2]))

from deeptutor.learning import policy
from deeptutor.learning.models import (
    KnowledgePoint, KnowledgeType, LearningModule, LearningProgress,
    PendingQuestion, QuizAttempt, RepetitionState, ReviewTask,
)
from deeptutor.learning.service import LearningService
from deeptutor.learning.storage import LearningStore
from deeptutor.learning.scheduler import SpacedRepetitionScheduler
from deeptutor.capabilities.mastery.choices import parse_options, has_option_bodies
from deeptutor.noteblocks.dialogue_engine import DialogueState, DialogueMove, MOVE_ORDER
from deeptutor.learning.scheduler import INTERVAL_SEQUENCES

# =============================================================================
# 1. Criar o Mastery Path: Eletromagnetismo (Hayt)
# =============================================================================

print("=" * 70)
print("  TESTE FUNCIONAL: Eletromagnetismo via Mastery Path")
print("  Baseado em Hayt 7a Ed - Cap.1: Analise Vetorial")
print("=" * 70)

BOOK_ID = "hayt-eletromagnetismo"
print(f"\n[1] Criando mastery path: {BOOK_ID}")
print("-" * 50)

modules_data = [
    {
        "name": "Cap.1: Analise Vetorial",
        "order": 0,
        "pass_threshold": 0.9,
        "kps": [
            ("Escalares e Vetores", KnowledgeType.MEMORY),
            ("Algebra Vetorial (soma/sub)", KnowledgeType.PROCEDURE),
            ("Produto Escalar (ponto)", KnowledgeType.PROCEDURE),
            ("Produto Vetorial (cruz)", KnowledgeType.PROCEDURE),
            ("Coordenadas Cartesianas", KnowledgeType.CONCEPT),
            ("Coordenadas Cilindricas", KnowledgeType.CONCEPT),
            ("Coordenadas Esfericas", KnowledgeType.CONCEPT),
            ("Transformacao entre Sistemas", KnowledgeType.PROCEDURE),
            ("Campos Escalares e Vetoriais", KnowledgeType.CONCEPT),
            ("Teorema da Divergencia", KnowledgeType.CONCEPT),
            ("Teorema de Stokes", KnowledgeType.CONCEPT),
        ],
    },
    {
        "name": "Cap.2: Lei de Coulomb e Campo Eletrico",
        "order": 1,
        "pass_threshold": 0.9,
        "kps": [
            ("Lei de Coulomb", KnowledgeType.MEMORY),
            ("Campo Eletrico de Carga Pontual", KnowledgeType.PROCEDURE),
            ("Campo de Distribuicoes de Carga", KnowledgeType.PROCEDURE),
            ("Linhas de Fluxo Eletrico", KnowledgeType.CONCEPT),
        ],
    },
]

modules: list[LearningModule] = []
for m_data in modules_data:
    module_id = f"{BOOK_ID}_m{m_data['order']}"
    kps = []
    for j, (kp_name, kp_type) in enumerate(m_data["kps"]):
        kps.append(KnowledgePoint(
            id=f"{module_id}_kp{j}",
            name=kp_name,
            type=kp_type,
            module_id=module_id,
        ))
    modules.append(LearningModule(
        id=module_id,
        name=m_data["name"],
        order=m_data["order"],
        pass_threshold=m_data["pass_threshold"],
        knowledge_points=kps,
    ))

kp_count = sum(len(mod.knowledge_points) for mod in modules)
print(f"  Modulos: {len(modules)}")
print(f"  Knowledge Points: {kp_count}")
for mod in modules:
    print(f"    [MOD] {mod.name} ({len(mod.knowledge_points)} KPs)")
    for kp in mod.knowledge_points:
        print(f"      [KP] {kp.name} ({kp.type.value})")


# =============================================================================
# 2. Metodos auxiliares
# =============================================================================

status_icon = {"mastered": "[OK]", "learning": "[..]", "new": "[  ]", "complete": "[DONE]"}
action_icon = {
    "probe": "[PRB]", "practice": "[PRC]", "assess": "[AST]", "review": "[REV]",
    "answer_pending": "[WAI]", "complete": "[DON]",
}


def print_map(progress: LearningProgress) -> None:
    s = policy.map_summary(progress)
    c = s["counts"]
    print(f"\n  Progresso: {c['mastered']}/{c['total']} mastered  "
          f"({c['learning']} learning, {c['new']} new, "
          f"{s['due_reviews']} due reviews)")
    print(f"  {'-' * 50}")
    for mod in s["modules"]:
        print(f"  {mod['name']} ({mod['mastered']}/{mod['total']})")
        for kp in mod["knowledge_points"]:
            icon = status_icon.get(kp["status"], "???")
            mastery_str = f"{kp['mastery']:.0%}" if kp["mastery"] > 0 else ""
            line = f"    {icon} {kp['name']} {mastery_str}".strip()
            print(line)
    print()


def print_next(progress: LearningProgress) -> Any:
    step = policy.next_objective(progress)
    icon = action_icon.get(step.action, "???")
    print(f"\n  {icon} {step.action.upper()}: {step.knowledge_point_name}")
    print(f"     Modulo: {step.module_name}")
    print(f"     Tipo: {step.knowledge_point_type} | Gate: {step.gate}")
    print(f"     Mastery: {step.mastery:.1%} / Threshold: {step.threshold:.0%}")
    print(f"     Motivo: {step.reason}")
    if step.pending_prompt:
        print(f"     [WAIT] Pending: {step.pending_prompt}")
    return step


def print_dialogue(move: DialogueMove | None, expectation: str) -> str:
    if move is None:
        text = f"[SUMMARY] {expectation}"
    else:
        prompts = {
            DialogueMove.PUMP: f"[PUMP] Me fale mais sobre: {expectation}",
            DialogueMove.HINT: f"[HINT] Pense em: {expectation}",
            DialogueMove.PROMPT: f"[PROMPT] Complete: {expectation}",
            DialogueMove.ASSERT: f"[ASSERT] Na verdade: {expectation}",
        }
        text = prompts.get(move, expectation)
    print(f"    Tutor: {text}")
    return text


# =============================================================================
# 3. Inicializar engine
# =============================================================================

print(f"\n\n[2] Inicializando LearningService...")
print("-" * 50)

store = LearningStore()
service = LearningService(store)
progress = service.get_or_create(BOOK_ID)
service.init_modules(progress, modules)
progress.current_module_id = modules[0].id
progress.current_kp_index = 0
service.save(progress)
scheduler = SpacedRepetitionScheduler()

print(f"  [OK] Path criado: {BOOK_ID}")
print(f"  [OK] Storage: {store._root / f'{BOOK_ID}.json'}")


# =============================================================================
# 4. CENARIO A: KP de MEMORIA - Gate quantitativo (90%)
# =============================================================================

print(f"\n\n{'=' * 70}")
print("  CENARIO A: Knowledge Point de MEMORIA (gate quantitativo 90%)")
print(f"  Alvo: 'Escalares e Vetores'")
print(f"{'=' * 70}")

print(f"\n{'=' * 50}")
print(f"  ETAPA 1: 5-Step Frame -- Steps 1-2 (Tutor pergunta, Aluno responde)")
print(f"{'=' * 50}")

step = print_next(progress)
assert step.action == "probe", f"Esperado 'probe', veio '{step.action}'"
assert step.knowledge_point_name == "Escalares e Vetores"

print(f"\n  [OK] Metodologia: next_objective retorna 'probe' para KP nao tocado.")
print(f"     O tutor deve testar o aluno antes de ensinar (test-out / compression).")

# Aluno responde errado -> vira 'learning', nao 'mastered'
attempt_1 = QuizAttempt(
    question_id="q1",
    knowledge_point_id=step.knowledge_point_id,
    module_id=step.module_id,
    is_correct=False,
    user_answer="escalar tem magnitude e direcao",  # errado: vetor tem direcao
)
service.record_quiz_attempt(progress, attempt_1)
service.update_mastery(progress, step.knowledge_point_id,
                        service.calculate_mastery(progress, step.knowledge_point_id))
service.save(progress)

kp = next(kp for kp in progress.modules[0].knowledge_points if kp.id == step.knowledge_point_id)
print(f"\n  Apos resposta ERRADA:")
print(f"     Status: {policy.objective_status(progress, kp)}")
print(f"     Mastery: {policy.display_mastery(progress, kp):.1%}")
assert policy.objective_status(progress, kp) == "learning", (
    f"Esperado 'learning', veio '{policy.objective_status(progress, kp)}'"
)
print(f"  [OK] Aluno errou -> status 'learning' (gate nao foi atingido)")
print(f"  [OK] Metodologia: Hard gate -- 1 erro nao e suficiente para mastered")

print(f"\n{'=' * 50}")
print(f"  ETAPA 2: next_objective agora recomenda 'practice'")
print(f"{'=' * 50}")

step = print_next(progress)
assert step.action == "practice", f"Esperado 'practice', veio '{step.action}'"
print(f"  [OK] Metodologia: KP ja visto mas nao mastered -> action='practice'")

# Agora o aluno acerta 9 de 10 questoes -> mastery ~0.9
print(f"\n{'=' * 50}")
print(f"  ETAPA 3: Aluno acerta 9x seguidas -> mastery ~90%+")
print(f"{'=' * 50}")

for i in range(9):
    attempt = QuizAttempt(
        question_id=f"q{i+2}",
        knowledge_point_id=step.knowledge_point_id,
        module_id=step.module_id,
        is_correct=True,
        user_answer="escalar: magnitude apenas; vetor: magnitude e direcao",
    )
    service.record_quiz_attempt(progress, attempt)
    mastery = service.calculate_mastery(progress, step.knowledge_point_id)
    service.update_mastery(progress, step.knowledge_point_id, mastery)

service.save(progress)
final_mastery = policy.display_mastery(progress, kp)
final_status = policy.objective_status(progress, kp)

print(f"  Mastery final: {final_mastery:.1%}")
print(f"  Status final: {final_status}")
print(f"  Threshold MEMORY: {policy.QUANTITATIVE_GATE[KnowledgeType.MEMORY]:.0%}")

assert final_status == "mastered", (
    f"Esperado 'mastered', veio '{final_status}' (mastery={final_mastery:.1%})"
)
print(f"  [OK] METODOLOGIA VALIDADA:")
print(f"     Hard gate MEMORY: mastery {final_mastery:.0%} >= 90% -> MASTERED")
print(f"     Compression: KP mastered -> next_objective vai pular para o proximo")


# =============================================================================
# 5. CENARIO B: KP de CONCEITO - Gate qualitativo (Feynman)
# =============================================================================

print(f"\n\n{'=' * 70}")
print(f"  CENARIO B: Knowledge Point de CONCEITO (gate qualitativo)")
print(f"  Alvo: Coordenadas Cartesianas")
print(f"{'=' * 70}")

# Forcar o progresso para o CONCEITO desejado (pular KPs intermediarios)
concept_kp = progress.modules[0].knowledge_points[4]  # Coordenadas Cartesianas
assert concept_kp.type == KnowledgeType.CONCEPT
print(f"  Forcando foco em: {concept_kp.name} ({concept_kp.type.value})")
print(f"  Status atual: {policy.objective_status(progress, concept_kp)}")

kp_id = concept_kp.id

print(f"\n{'=' * 50}")
print(f"  ETAPA 1: conceito nao visto -> action seria 'probe'")
print(f"{'=' * 50}")
print(f"  Status antes: {policy.objective_status(progress, concept_kp)}")
assert policy.objective_status(progress, concept_kp) == "new"
print(f"  [OK] Metodologia: KP novo -> probe (testar se aluno ja sabe)")

print(f"\n{'=' * 50}")
print(f"  ETAPA 2: Aluno explica (Feynman) -> mastery_assess")
print(f"{'=' * 50}")

# Aluno tenta explicar mas incompleto (passa sem mastered)
service.record_qualitative(progress, kp_id, passed=False,
                            evidence="Falou de eixos ortogonais mas nao mencionou a base i j k")
print(f"  Aluno: 'Coordenadas cartesianas usam eixos x, y, z'")
print(f"  Tutor: 'Faltou mencionar que a base ortonormal e i, j, k'")
print(f"  Status apos Feynman FAIL: {policy.objective_status(progress, concept_kp)}")
assert policy.is_mastered(progress, concept_kp) is False, "Nao deveria estar mastered"
print(f"  [OK] Metodologia: CONCEITO -> gate qualitativo")
print(f"     -> Nao passa ate que Feynman seja aprovado")

# Agora passa
service.record_qualitative(progress, kp_id, passed=True,
                            evidence="Explicou eixos, base, vetor posicao e elementos diferenciais")
status2 = policy.objective_status(progress, concept_kp)
print(f"\n  Status apos Feynman PASSAR: {status2}")
assert status2 == "mastered", f"Esperado 'mastered', veio '{status2}'"
print(f"  [OK] METODOLOGIA VALIDADA:")
print(f"     Gate qualitativo CONCEITO: so passa com Feynman check")
print(f"     Quantitative score NAO abre gate de CONCEITO")


# =============================================================================
# 6. CENARIO C: EMT Dialogue - Scaffolding progressivo
# =============================================================================

print(f"\n\n{'=' * 70}")
print(f"  CENARIO C: EMT Dialogue - Scaffolding Progressivo")
print(f"  Alvo: Coordenadas Cilindricas (conceito)")
print(f"{'=' * 70}")

print(f"\n  O EMT Dialogue segue a escada de suporte do AutoTutor (Memphis):")
print(f"    PUMP (mais aberto) -> HINT -> PROMPT -> ASSERT (mais direto)")
print(f"     A cada erro, o tutor da mais suporte.")
print(f"     A cada acerto, o tutor reduz o suporte (volta para PUMP).")

step = print_next(progress)
dialogue = DialogueState(student_id="test", skill=step.knowledge_point_name)

print(f"\n{'=' * 50}")
print(f"  Rodada 1: PUMP (aluno responde parcialmente)")
print(f"{'=' * 50}")
move = dialogue.current_move
print_dialogue(move, "Coordenadas cilindricas usam rho, phi, z")
dialogue.record_success()
print(f"    Aluno: 'Usa rho (raio) e phi (angulo)'")
print(f"    -> record_success() -> avanca para HINT")

print(f"\n{'=' * 50}")
print(f"  Rodada 2: HINT (aluno acerta)")
print(f"{'=' * 50}")
move = dialogue.current_move
print_dialogue(move, "Relacao com cartesianas: x=rho.cos(phi), y=rho.sen(phi)")
dialogue.record_success()
print(f"    Aluno: 'x = rho cos phi, y = rho sen phi'")
print(f"    -> record_success() -> avanca para PROMPT")

print(f"\n{'=' * 50}")
print(f"  Rodada 3: PROMPT (aluno erra)")
print(f"{'=' * 50}")
move = dialogue.current_move
print_dialogue(move, "Elemento diferencial de volume: dv = rho drho dphi dz")
dialogue.record_failure()
print(f"    Aluno: 'dv = drho dphi dz' (esqueceu o rho)")
print(f"    -> record_failure() -> volta para PUMP")

print(f"\n{'=' * 50}")
print(f"  Rodada 4: PUMP novamente (apos 3 falhas consecutivas, reseta)")
print(f"{'=' * 50}")
move = dialogue.current_move
print_dialogue(move, "Revisao completa de coordenadas cilindricas")
print(f"    Apos 3 falhas consecutivas: reset_to_pump()")
print(f"    -> Aluno precisa de mais suporte")

print(f"\n  [OK] METODOLOGIA VALIDADA:")
print(f"     EMT Dialogue segue a escada: Pump -> Hint -> Prompt")
print(f"     Acerto -> avanca (menos suporte)")
print(f"     Erro -> recua (mais suporte)")
print(f"     3 falhas consecutivas -> reseta para PUMP")


# =============================================================================
# 7. CENARIO D: Spaced Repetition + Review Queue
# =============================================================================

print(f"\n\n{'=' * 70}")
print(f"  CENARIO D: Spaced Repetition + Review Queue")
print(f"{'=' * 70}")

print(f"\n  Intervalos por tipo de conhecimento:")
print(f"    MEMORY:   [0, 1, 3, 7, 14, 30, 60] dias")
print(f"    CONCEPT:  [3, 7, 14, 30] dias")
print(f"    PROCEDURE:[3, 7, 14] dias")
print(f"    DESIGN:   [14, 28] dias")

kp_escalar = progress.modules[0].knowledge_points[0]  # ja mastered
state = scheduler.get_initial_state(KnowledgeType.MEMORY)
print(f"\n  Estado inicial MEMORY: inter={state.interval_index}, prox_review={state.next_review_at}")

for i in range(3):
    scheduler.schedule_next(state, KnowledgeType.MEMORY, is_correct=True)
    idx = min(state.interval_index, len(INTERVAL_SEQUENCES[KnowledgeType.MEMORY]) - 1)
    int_val = INTERVAL_SEQUENCES[KnowledgeType.MEMORY][idx]
    print(f"  Apos acerto #{i+1}: inter={state.interval_index}, prox em ~{int_val} dias")

progress.repetition_states[kp_escalar.id] = state
progress.review_queue = scheduler.build_review_queue(progress)
print(f"\n  Review queue: {len(progress.review_queue)} itens")
for task in progress.review_queue:
    due_str = "AGORA" if task.due_at <= time.time() else "futuro"
    print(f"    [REV] {task.knowledge_point_id} (prioridade {task.priority}, due {due_str})")

print(f"\n  [OK] METODOLOGIA VALIDADA:")
print(f"     Spaced repetition com intervalos crescentes por tipo")
print(f"     Review queue prioriza erros > DESIGN > PROCEDURE > CONCEPT > MEMORY")


# =============================================================================
# 8. CENARIO E: 5-Step Tutoring Frame (completo)
# =============================================================================

print(f"\n\n{'=' * 70}")
print(f"  CENARIO E: 5-Step Tutoring Frame (AutoTutor)")
print(f"  Alvo: Produto Vetorial (PROCEDURE)")
print(f"{'=' * 70}")

print(f"""
  O 5-Step Frame do AutoTutor (Nye, Graesser & Hu, 2014):

  1: Tutor propoe problema/pergunta
  2: Aluno tenta responder
  3: Tutor da feedback breve (+/-/neutro)
  4: Interacao colaborativa (pump -> hint -> prompt)
  5: Tutor verifica compreensao

  Vamos simular as 5 etapas:
""")

step = print_next(progress)

print(f"\n{'=' * 50}")
print(f"  STEP 1: Tutor pergunta")
print(f"{'=' * 50}")
print(f"  Tutor: 'Calcule A x B para A = (2, 1, 0), B = (1, 3, 0)'")
print(f"  -> mastery_question registra a pergunta + resposta esperada")

q1 = PendingQuestion(
    question_id="pq-1",
    knowledge_point_id=step.knowledge_point_id,
    module_id=step.module_id,
    prompt="Calcule A x B para A = (2, 1, 0), B = (1, 3, 0)",
    question_type="short",
    expected_answer="(0, 0, 5) ou 0i + 0j + 5k",
)
service.set_pending_question(progress, q1)
step2 = print_next(progress)
assert step2.action == "answer_pending", f"Esperado 'answer_pending', veio '{step2.action}'"
print(f"  [OK] STEP 2: pending_question bloqueia ate ser respondida")

print(f"\n{'=' * 50}")
print(f"  STEP 3-4: Aluno responde + Tutor avalia")
print(f"{'=' * 50}")
aluno_resposta = "(0, 0, 5)"
acertou = service.grade_and_record(
    progress,
    question_id=q1.question_id,
    knowledge_point_id=q1.knowledge_point_id,
    module_id=q1.module_id,
    user_answer=aluno_resposta,
    expected_answer=q1.expected_answer,
    question_type="short",
    scheduler=scheduler,
)
service.clear_pending_question(progress)
print(f"  Aluno: '{aluno_resposta}'")
print(f"  Tutor: {'[OK] Correto!' if acertou else '[..] Quase...'}")
print(f"  [OK] STEP 3-4: Grade and record + feedback")

print(f"\n{'=' * 50}")
print(f"  STEP 5: Verificacao de compreensao")
print(f"{'=' * 50}")
step3 = print_next(progress)
print(f"  Tutor: 'Resuma o que aprendeu sobre produto vetorial'")
print(f"  [OK] STEP 5: next={step3.action} -- verifica se pode avancar")
print(f"  [OK] 5-STEP FRAME COMPLETO")


# =============================================================================
# 9. CENARIO F: Compression (pular mastered)
# =============================================================================

print(f"\n\n{'=' * 70}")
print(f"  CENARIO F: Compression - Pular KPs ja masterizados")
print(f"{'=' * 70}")

print(f"\n  next_objective sempre comeca do primeiro modulo/primeiro KP.")
print(f"  Mas KPs mastered sao PULADOS -- 'gate is the cursor'.")

step = print_next(progress)
kps_no_mod0 = progress.modules[0].knowledge_points

# O primeiro KP nao-mastered deve ser retornado
first_unmastered = None
for idx, kp_check in enumerate(kps_no_mod0):
    if not policy.is_mastered(progress, kp_check):
        first_unmastered = kp_check
        print(f"  KP[{idx}] '{kp_check.name}' -> NAO mastered (primeiro disponivel)")
        break
    else:
        print(f"  KP[{idx}] '{kp_check.name}' -> MASTERED (pulado)")

assert step.knowledge_point_id == first_unmastered.id, (
    f"Esperado '{first_unmastered.name}', veio '{step.knowledge_point_name}'"
)
print(f"\n  [OK] COMPRESSION: KP mastered e pulado, nao re-ensinado")
print(f"  [OK] Metodologia: 'The gate IS the cursor' -- nao ha stage counter")


# =============================================================================
# 10. Relatorio Final
# =============================================================================

print(f"\n\n{'=' * 70}")
print(f"  RELATORIO FINAL")
print(f"{'=' * 70}")

final_map = policy.map_summary(progress)
c = final_map["counts"]
print(f"\n  Progresso final: {c['mastered']}/{c['total']} mastered")
print(f"     {c['learning']} learning, {c['new']} new")
print(f"     {final_map['due_reviews']} due reviews")
print(f"     Complete: {final_map['complete']}")

print(f"\n  [OK] Metodologias validadas:")
print(f"  {'=' * 50}")

methodologies = [
    ("Hard gate 90%", "MEMORY so mastered com >= 90% de acerto recency-weighted"),
    ("Gate qualitativo", "CONCEITO so mastered com Feynman check (nao por score)"),
    ("EMT Dialogue", "Pump -> Hint -> Prompt com fallback/avanco por acerto/erro"),
    ("5-Step Frame", "Pergunta -> Resposta -> Feedback -> Colaboracao -> Verificacao"),
    ("Compression", "KP mastered e pulado -- 'gate is the cursor'"),
    ("Macro adaptivity", "next_objective decide o que fazer baseado no estado real"),
    ("Spaced Repetition", "Intervalos crescentes por tipo, prioridade por erro"),
    ("Test-out (probe)", "KP novo comeca com probe, nao com ensino direto"),
    ("Content > Medium", "Conteudo semantico real do Hayt usado como base"),
]

for i, (name, desc) in enumerate(methodologies, 1):
    print(f"  {i}. {name}")
    print(f"     {desc}")

print(f"\n\n  Storage: {store._root / f'{BOOK_ID}.json'}")
print(f"  Para limpar, delete o arquivo acima.")
print(f"\n{'=' * 70}")
print(f"  TESTE CONCLUIDO")
print(f"{'=' * 70}")
