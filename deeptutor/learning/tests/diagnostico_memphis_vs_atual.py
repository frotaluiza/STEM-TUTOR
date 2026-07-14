"""
DIAGNOSTICO: Comportamento do Tutor Atual vs Estrategias Memphis.

Mostra:
  1. Aluno ERRANDO -> hard gate bloqueando progresso
  2. O que o prompt atual do tutor faz vs o que deveria fazer
  3. Gap analysis: Memphis recommendations nao implementadas
"""

import os, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
if sys.platform == "win32":
    sys.stdout = open(sys.stdout.fileno(), mode="w", encoding="utf-8", buffering=1, closefd=False)

from deeptutor.learning import policy
from deeptutor.learning.models import (
    KnowledgePoint, KnowledgeType, LearningModule, QuizAttempt,
)
from deeptutor.learning.service import LearningService
from deeptutor.learning.storage import LearningStore
from deeptutor.learning.scheduler import SpacedRepetitionScheduler

BOOK_ID = "hayt-diagnostico"
store = LearningStore()
service = LearningService(store)
store_path = store._root / f"{BOOK_ID}.json"
if store_path.exists(): store_path.unlink()

modulo = LearningModule(
    id=f"{BOOK_ID}_m0", name="Cap.1: Analise Vetorial", order=0, pass_threshold=0.9,
    knowledge_points=[
        KnowledgePoint(id=f"{BOOK_ID}_kp0", name="Escalares e Vetores", type=KnowledgeType.MEMORY, module_id=f"{BOOK_ID}_m0"),
        KnowledgePoint(id=f"{BOOK_ID}_kp1", name="Coordenadas Cartesianas", type=KnowledgeType.CONCEPT, module_id=f"{BOOK_ID}_m0"),
        KnowledgePoint(id=f"{BOOK_ID}_kp2", name="Produto Vetorial", type=KnowledgeType.PROCEDURE, module_id=f"{BOOK_ID}_m0"),
    ],
)

progress = service.get_or_create(BOOK_ID)
service.init_modules(progress, [modulo])
progress.current_module_id = modulo.id
service.save(progress)

scheduler = SpacedRepetitionScheduler()
kp0 = modulo.knowledge_points[0]
kp1 = modulo.knowledge_points[1]
kp2 = modulo.knowledge_points[2]

def mastery_str(progress, kp):
    return f"{policy.display_mastery(progress, kp):.0%}"

def status_str(progress, kp):
    return policy.objective_status(progress, kp)

def registrar(progress, kp, correta, resposta=""):
    attempt = QuizAttempt(
        question_id=f"q_{kp.id}_{int(time.time()*1e6)%100000}",
        knowledge_point_id=kp.id, module_id=kp.module_id,
        is_correct=correta, user_answer=resposta,
    )
    service.record_quiz_attempt(progress, attempt)
    service.update_mastery(progress, kp.id, service.calculate_mastery(progress, kp.id))
    service.save(progress)


# =====================================================================
print("=" * 70)
print("  DIAGNOSTICO: Tutor Atual vs Estrategias Memphis")
print("=" * 70)

# =====================================================================
# PARTE 1: Aluno errando MOSTRADO -> hard gate bloqueia
# =====================================================================
print("\n" + "=" * 70)
print("  PARTE 1: HARD GATE BLOQUEANDO (aluno errando)")
print("=" * 70)

step = policy.next_objective(progress)
print(f"\n  Objetivo: {step.knowledge_point_name}")
print(f"  Gate: {step.gate}")
print(f"  Threshold: {step.threshold:.0%}")
print()

tentativas = 0
while tentativas < 12:
    step = policy.next_objective(progress)
    if step.action == "complete" or step.knowledge_point_id != kp0.id:
        break
    tentativas += 1

    if tentativas <= 3:
        errou = True
        resp = "vetor tem magnitude"
    elif tentativas <= 6:
        errou = (tentativas % 2 == 0)
        resp = "escalar: magnitude; vetor: magnitude e direcao" if not errou else "escalar e vetor sao a mesma coisa"
    else:
        errou = (tentativas % 2 == 1)
        resp = "correto" if not errou else "nao lembro"

    registrar(progress, kp0, not errou, resp)
    m = mastery_str(progress, kp0)
    s = status_str(progress, kp0)
    status_icon = {"mastered":"OK","learning":"..","new":"  "}.get(s, "??")
    marca = "x" if errou else "+"
    pref = "ALUNO ERROU" if errou else "ALUNO ACERTOU"
    print(f"  #{tentativas:2d} [{marca}] {pref:14s} | mastery: {m:>4s} | status: [{status_icon}]")

    if s == "mastered":
        print(f"\n  >>> GATE ATINGIDO apos {tentativas} tentativas! <<<")
        break

if status_str(progress, kp0) != "mastered":
    print(f"\n  >>> HARD GATE BLOQUEANDO apos {tentativas} tentativas! <<<")
    print(f"  >>> Mastery: {mastery_str(progress, kp0)} / Threshold: 90% <<<")
    print(f"  >>> Isso e CORRETO! O aluno NAO deve passar sem mastery >= 90% <<<")

print(f"\n  Resumo: {tentativas} tentativas, mastery final {mastery_str(progress, kp0)}")
print(f"  Conclusao: Gate funciona. Aluno precisa de mais repeticoes para passar.")

# =====================================================================
# PARTE 2: O que o prompt ATUAL faz quando o aluno erra
# =====================================================================
print("\n\n" + "=" * 70)
print("  PARTE 2: O que o PROMPT ATUAL diz ao tutor quando o aluno erra?")
print("=" * 70)

print(f"""
  Prompt atual do sistema (system.md - linhas 6-12):

    6: Then act on the objective:
    7: - No objectives yet? Design a path...
    8: - 'probe' (untouched): briefly check...
    9: - memory / procedure objectives: register the question...
         ...'Keep working the same objective until mastery_grade reports mastered: true'
    10: - concept / design objectives: ask the learner to explain...
    11: - 'review': a spaced-repetition item is due...
    12: - 'complete': congratulate...

  PROBLEMA: Quando o aluno ERRA, o prompt diz apenas:
    "Keep working the same objective until mastery_grade reports mastered: true"

  Isso DELEGA toda a estrategia pedagogica para o LLM, sem estrutura.
  O LLM pode:
  - Repetir a mesma pergunta (chato)
  - Dar a resposta sem ensinar
  - Nunca variar a abordagem
  - Ignorar misconceptions especificas
    
  MEMPHIS diria: use PUMP -> HINT -> PROMPT -> ASSERTION.
  A cada erro, de MAIS suporte. A cada acerto, de MENOS.
""")

# =====================================================================
# PARTE 3: Demonstrar o que FALTA - EMT Scaffolding
# =====================================================================
print("=" * 70)
print("  PARTE 3: EMT Scaffolding - O que DEVERIA acontecer")
print("=" * 70)

from deeptutor.noteblocks.dialogue_engine import DialogueState, DialogueMove

print(f"""
  Quando o aluno erra, o tutor DEVERIA seguir a escada EMT:

  Expectativa: "O aluno sabe que vetor tem magnitude e direcao"
  Resposta do aluno: "vetor tem magnitude" (faltou direcao)

  Tutor atual                        Tutor com EMT
  ───────────────────────────        ───────────────────────────
  'Errou. Tente de novo.'     ->     PUMP: "Me fale mais sobre as
                                      propriedades de um vetor"
                                      HINT: "Pense: o que diferencia
                                      um vetor de um escalar?"
                                      PROMPT: "Complete: um vetor
                                      tem magnitude e ___"
                                      ASSERT: "Na verdade, vetor
                                      tem magnitude E direcao."
""")

# Demonstrar EMT com aluno errando MUITO
print("  Simulacao EMT com aluno com dificuldade:\n")

dialogue = DialogueState(student_id="demo", skill="Produto Vetorial")
expectations = [
    "Produto vetorial A x B = |A||B|sen(theta) n",
    "Componentes: (AyBz-AzBy, AzBx-AxBz, AxBy-AyBx)",
]
erros_seguidos = 0

for exp in expectations:
    for _ in range(4):
        move = dialogue.current_move
        if move is None:
            print(f"  >> ASSERT: {exp}")
            break

        move_name = move.value.upper()
        if move == DialogueMove.PUMP:
            msg = f"Explique {exp[:40]}... com suas palavras."
        elif move == DialogueMove.HINT:
            msg = f"Dica: {exp[:40]}..."
        else:
            msg = f"Complete: {exp[:40]}..."

        # Simula aluno errando nas primeiras, acertando depois
        aluno_errou = erros_seguidos < 1
        if aluno_errou:
            dialogue.record_failure()
            erros_seguidos += 1
            feedback = "ALUNO: nao sei / resposta incompleta"
            dial_effect = "-> ERROU: sobe suporte"
        else:
            dialogue.record_success()
            erros_seguidos = 0
            feedback = "ALUNO: resposta correta"
            dial_effect = "-> ACERTOU: diminui suporte"

        print(f"   TUTOR [{move_name:7s}]: {msg}")
        print(f"   {feedback}")
        print(f"   Efeito: {dial_effect}")
        print()
        if not aluno_errou:
            break

# =====================================================================
# PARTE 4: O que precisa ser implementado
# =====================================================================
print("\n" + "=" * 70)
print("  PARTE 4: GAP ANALYSIS - Memphis vs Atual")
print("=" * 70)

gaps = [
    ("5-Step Tutoring Frame", False,
     "AutoTutor: pergunta -> resposta -> feedback -> colaboracao -> verificacao",
     "Prompt atual nao estrutura os turnos. O LLM decide sozinho."),
    ("EMT Dialogue Scaffolding", False,
     "Pump -> Hint -> Prompt -> Assertion. Progression CLARA de suporte.",
     "dialogue_engine.py existe mas NAO esta ligado ao sistema de prompt."),
    ("Expectation Coverage", False,
     "Tutor define EXPECTATIVAS (o que uma boa resposta contem) e mede cobertura",
     "Prompt atual nao menciona expectativas. So 'registre a resposta esperada'."),
    ("Misconception Handling", False,
     "AutoTutor tem banco de MISCONCEPTIONS conhecidas. Tutor compara e corrige.",
     "Prompt atual nao tem banco de erros comuns."),
    ("Face-Saving Feedback", False,
     "'Muita gente confunde X com Y' - erro atribuido ao peer, nao ao aluno.",
     "Prompt atual: 'be warm and encouraging'. Nao ha estrategia de face-saving."),
    ("Test-out com Probe", True,
     "KP novo: testar se aluno ja sabe (compression path).",
     "Implementado! Action='probe' ja existe no policy."),
    ("Hard Gate 90%", True,
     "Nao avanca sem mastery >= 90% (Alpha Schools).",
     "Implementado! QUANTITATIVE_GATE = 0.9 no policy."),
    ("Gate Qualitativo (Feynman)", True,
     "CONCEITO/DESIGN: so passa com explicacao do aluno, nao por score.",
     "Implementado! QUALITATIVE_TYPES + mastery_assess."),
    ("Spaced Repetition", True,
     "Intervalos crescentes por tipo de conhecimento.",
     "Implementado! scheduler.py com INTERVAL_SEQUENCES."),
    ("Macro/Micro Adaptivity", True,
     "Outer loop: next_objective decide o que fazer. Inner loop: ferramentas.",
     "Implementado! next_objective + tools mastery_quiz/grade/assess."),
]

print(f"\n  {'Status':8s} {'Praticas':30s} {'Memphis':40s} {'Implementado':30s}")
print(f"  {'-'*8} {'-'*30} {'-'*40} {'-'*30}")
for practice, ok, memphis_desc, atual_desc in gaps:
    status = "[OK]" if ok else "[..]"
    nome = practice[:28]
    print(f"  {status:8s} {nome:30s} {memphis_desc[:38]:40s} {atual_desc[:28]:30s}")

total_ok = sum(1 for _, ok, _, _ in gaps if ok)
total = len(gaps)
print(f"\n  Implementado: {total_ok}/{total} ({total_ok*100//total}%)")
print(f"  GAP: {total - total_ok} praticas Memphis NAO implementadas")

# =====================================================================
# PARTE 5: Proposta de novo system prompt (com EMT)
# =====================================================================
print("\n\n" + "=" * 70)
print("  PARTE 5: Proposta de Novo System Prompt (com EMT Memphis)")
print("=" * 70)

print("""
  [Mastery Tutor mode - with Memphis EMT Dialogue]

  You are a one-on-one mastery tutor based on the AutoTutor framework.

  STRUCTURED TURN:
    1. QUESTION: Pose a problem or question
    2. RESPONSE: Let the learner answer (use ask_user)
    3. FEEDBACK: Brief (+/neutral/-)
    4. SCAFFOLD: If wrong, use EMT dialogue progression
    5. VERIFY: Ask learner to summarise understanding

  EMT SCAFFOLDING (escalate when stuck):
    PUMP  -> "Tell me more about..." (most open)
    HINT  -> "Think about the relationship between..." 
    PROMPT -> "What specific term describes...?" (most specific)
    ASSERT -> "Actually, the correct answer is..." (tutor provides)
    
    After a correct answer, step DOWN (toward pump).
    After a wrong answer, step UP (toward assert).
    After 3 consecutive failures, reset to PUMP.

  FACE-SAVING: Attribute common errors to "many students" or a peer
    agent, never directly blame the learner.
  EXPECTATION COVERAGE: Track which parts of a complete answer the
    learner has provided. Scaffold toward the missing parts.
  MISCONCEPTIONS: When you spot a specific error pattern, name it
    and contrast it with the correct understanding.

  HARD GATE: Call mastery_status first. Never advance past an
    objective the engine hasn't marked mastered.
""")

# =====================================================================
# FINAL: Recomendacao
# =====================================================================
print("=" * 70)
print("  RECOMENDACAO")
print("=" * 70)
print(f"""
  O que fazer:

  1. URGENTE: Substituir system.md (14 linhas) por prompt com
     estrutura EMT + 5-Step Frame + face-saving

  2. INTEGRAR: dialogue_engine.py no loop do mastery_path
     (nao so no Runner do Conhecimento)

  3. TESTAR: simulacoes com aluno ERRANDO para validar que
     o scaffolding EMT funciona na conversa real

  4. CRIAR: sistema de EXPECTATIVAS por KP (o que uma resposta
     completa deve conter) para medir coverage

  Arquivos a modificar:
    - deeptutor/capabilities/mastery/prompts/en/system.md
    - deeptutor/capabilities/mastery/prompts/zh/system.md
    - deeptutor/capabilities/mastery/loop.py (integrar dialogue_engine)
""")

# Limpeza
if store_path.exists(): store_path.unlink()
