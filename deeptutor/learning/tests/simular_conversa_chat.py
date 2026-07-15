"""
Simulacao de conversa de chat entre Tutor e Aluno via Mastery Path.
Usa o livro Hayt - Eletromagnetismo 7a Ed como conteudo.
"""

import os, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

if sys.platform == "win32":
    sys.stdout = open(sys.stdout.fileno(), mode="w", encoding="utf-8", buffering=1, closefd=False)

from deeptutor.learning import policy
from deeptutor.learning.models import (
    KnowledgePoint, KnowledgeType, LearningModule, LearningProgress,
    PendingQuestion, QuizAttempt, RepetitionState,
)
from deeptutor.learning.service import LearningService
from deeptutor.learning.storage import LearningStore
from deeptutor.learning.scheduler import SpacedRepetitionScheduler, INTERVAL_SEQUENCES
from deeptutor.noteblocks.dialogue_engine import DialogueState, DialogueMove

BOOK_ID = "hayt-eletromagnetismo"
store = LearningStore()
service = LearningService(store)

# Limpar dados de execucao anterior
store_path = store._root / f"{BOOK_ID}.json"
if store_path.exists():
    store_path.unlink()

# ============================================
# 1. Configurar o mastery path
# ============================================

modulo = LearningModule(
    id=f"{BOOK_ID}_m0",
    name="Cap.1: Analise Vetorial",
    order=0,
    pass_threshold=0.9,
    knowledge_points=[
        KnowledgePoint(id=f"{BOOK_ID}_m0_kp0", name="Escalares e Vetores", type=KnowledgeType.MEMORY, module_id=f"{BOOK_ID}_m0"),
        KnowledgePoint(id=f"{BOOK_ID}_m0_kp1", name="Algebra Vetorial", type=KnowledgeType.PROCEDURE, module_id=f"{BOOK_ID}_m0"),
        KnowledgePoint(id=f"{BOOK_ID}_m0_kp2", name="Produto Escalar (ponto)", type=KnowledgeType.PROCEDURE, module_id=f"{BOOK_ID}_m0"),
        KnowledgePoint(id=f"{BOOK_ID}_m0_kp3", name="Produto Vetorial (cruz)", type=KnowledgeType.PROCEDURE, module_id=f"{BOOK_ID}_m0"),
        KnowledgePoint(id=f"{BOOK_ID}_m0_kp4", name="Coordenadas Cartesianas", type=KnowledgeType.CONCEPT, module_id=f"{BOOK_ID}_m0"),
        KnowledgePoint(id=f"{BOOK_ID}_m0_kp5", name="Coordenadas Cilindricas", type=KnowledgeType.CONCEPT, module_id=f"{BOOK_ID}_m0"),
        KnowledgePoint(id=f"{BOOK_ID}_m0_kp6", name="Coordenadas Esfericas", type=KnowledgeType.CONCEPT, module_id=f"{BOOK_ID}_m0"),
    ],
)

progress = service.get_or_create(BOOK_ID)
service.init_modules(progress, [modulo])
progress.current_module_id = modulo.id
service.save(progress)

scheduler = SpacedRepetitionScheduler()


def step_str(step):
    return f"[{step.action.upper()}] {step.knowledge_point_name} (mastery {step.mastery:.0%}/{step.threshold:.0%})"


def tutor(msg):
    print(f"  TUTOR: {msg}")

def aluno(msg):
    print(f"  ALUNO: {msg}")


# ============================================
print("=" * 66)
print("  CHAT: Sessao de Aprendizado - Eletromagnetismo (Hayt Cap.1)")
print("  Tutor: IA STEM Tutor | Modo: Mastery Path")
print("=" * 66)

# ============================================
# SESSAO 1: MEMORIA - Escalares e Vetores
# ============================================
print("\n" + "=" * 66)
print("  SESSAO 1: Gate quantitativo - 'Escalares e Vetores' (MEMORIA)")
print("=" * 66)

step = policy.next_objective(progress)
print(f"\n  Tutor inicia sessao. Proximo objetivo: {step.knowledge_point_name}")
print(f"  Acao: {step.action}")
print(f"  Mastery: {step.mastery:.0%} / Threshold: {step.threshold:.0%}")
print()

# --- TURNO 1 ---
tutor("Vamos comecar com conceitos basicos. O que diferencia uma grandeza")
tutor("escalar de uma grandeza vetorial? De exemplos de cada.")
print()
aluno("Escalar tem magnitude, vetor tem direcao. Ex: massa e temperatura sao")
aluno("escalares, forca e velocidade sao vetoriais.")
print()

# Registrar tentativa - respondeu corretamente
attempt = QuizAttempt(
    question_id=f"q_escalar_1",
    knowledge_point_id=step.knowledge_point_id,
    module_id=step.module_id,
    is_correct=True,
    user_answer="Escalar: magnitude apenas. Vetor: magnitude e direcao.",
)
service.record_quiz_attempt(progress, attempt)
service.update_mastery(progress, step.knowledge_point_id,
                       service.calculate_mastery(progress, step.knowledge_point_id))
service.save(progress)

kp = modulo.knowledge_points[0]
m = policy.display_mastery(progress, kp)
tutor("Correto! Escalares tem apenas magnitude (massa, temperatura),")
tutor(f"vetores tem magnitude E direcao (forca, velocidade). Mastery: {m:.0%}")
print()

# --- TURNO 2 ---
tutor("Como se representa a magnitude de um vetor A?")
print()
aluno("|A| ou simplesmente A.")
print()
attempt = QuizAttempt(
    question_id=f"q_escalar_2",
    knowledge_point_id=step.knowledge_point_id,
    module_id=step.module_id,
    is_correct=True,
    user_answer="|A| ou A",
)
service.record_quiz_attempt(progress, attempt)
service.update_mastery(progress, step.knowledge_point_id,
                       service.calculate_mastery(progress, step.knowledge_point_id))
service.save(progress)

m = policy.display_mastery(progress, kp)
tutor(f"Exato! A notacao |A| ou A representa a magnitude. Mastery: {m:.0%}")
print()

# --- TURNO 3 ---
tutor("Questao: Se A = (3, 4), qual a magnitude de A?")
print()
aluno("|A| = sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5.")
print()
attempt = QuizAttempt(
    question_id=f"q_escalar_3",
    knowledge_point_id=step.knowledge_point_id,
    module_id=step.module_id,
    is_correct=True,
    user_answer="|A| = sqrt(9+16) = 5",
)
service.record_quiz_attempt(progress, attempt)
service.update_mastery(progress, step.knowledge_point_id,
                       service.calculate_mastery(progress, step.knowledge_point_id))
service.save(progress)

m = policy.display_mastery(progress, kp)
tutor(f"Perfeito! |A| = 5. Mastery: {m:.0%}")

step = policy.next_objective(progress)
tutor(f"Gate atingido! Objetivo '{kp.name}' MASTERED.")
tutor(f"Proximo: {step.knowledge_point_name} ({step.action})")
print()

# ============================================
# SESSAO 2: PROCEDURE - Produto Vetorial
# ============================================
print("\n" + "=" * 66)
print("  SESSAO 2: Gate quantitativo - 'Produto Vetorial' (PROCEDURE)")
print("=" * 66)

# Avancar ate o Produto Vetorial (kp3)
kp_prod_vet = modulo.knowledge_points[3]
# Precisamos masterizar rapidamente kp1 e kp2
for kp_skip in [modulo.knowledge_points[1], modulo.knowledge_points[2]]:
    for i in range(5):
        attempt = QuizAttempt(
            question_id=f"q_{kp_skip.id}_{i}",
            knowledge_point_id=kp_skip.id,
            module_id=kp_skip.module_id,
            is_correct=True,
            user_answer="ok",
        )
        service.record_quiz_attempt(progress, attempt)
        service.update_mastery(progress, kp_skip.id,
                               service.calculate_mastery(progress, kp_skip.id))
service.save(progress)

step_next = policy.next_objective(progress)
while step_next.knowledge_point_id != kp_prod_vet.id and step_next.action != "complete":
    step_next = policy.next_objective(progress)
    if step_next.action in ("complete",):
        break

print(f"\n  Proximo objetivo: {step_next.knowledge_point_name}")
print()

# --- TURNO 1 ---
tutor("O produto vetorial e uma operacao fundamental em eletromagnetismo.")
tutor("Como se calcula A x B para vetores genericos A e B?")
print()
aluno("A x B = |A||B|sen(theta) n, onde n e o vetor unitario perpendicular")
aluno("ao plano formado por A e B. Em componentes:")
aluno("A x B = (AyBz - AzBy)i + (AzBx - AxBz)j + (AxBy - AyBx)k")
print()

attempt = QuizAttempt(
    question_id="q_prod_vet_1",
    knowledge_point_id=kp_prod_vet.id,
    module_id=kp_prod_vet.module_id,
    is_correct=True,
    user_answer="A x B = |A||B|sen(theta)n. Componentes: (AyBz-AzBy)i + ...",
)
service.record_quiz_attempt(progress, attempt)
service.update_mastery(progress, kp_prod_vet.id,
                       service.calculate_mastery(progress, kp_prod_vet.id))
service.save(progress)

tutor("Excelente! Voce acertou a formula geral e a forma componente.")
print()

# --- TURNO 2 ---
tutor("Calcule A x B para A = (2, 1, 0), B = (1, 3, 0). Dica: como z=0")
tutor("nos dois vetores, o resultado estara no eixo z.")
print()
aluno("A x B = (1*0 - 0*3)i + (0*1 - 2*0)j + (2*3 - 1*1)k")
aluno("= 0i + 0j + (6 - 1)k = (0, 0, 5)")
print()

attempt = QuizAttempt(
    question_id="q_prod_vet_2",
    knowledge_point_id=kp_prod_vet.id,
    module_id=kp_prod_vet.module_id,
    is_correct=True,
    user_answer="(0, 0, 5)",
)
service.record_quiz_attempt(progress, attempt)
service.update_mastery(progress, kp_prod_vet.id,
                       service.calculate_mastery(progress, kp_prod_vet.id))
service.save(progress)

m = policy.display_mastery(progress, kp_prod_vet)
tutor(f"Correto! A x B = (0, 0, 5). Mastery: {m:.0%}")
print()

# --- TURNO 3 ---
tutor("O que significa geometricamente |A x B|?")
print()
aluno("|A x B| representa a area do paralelogramo formado por A e B.")
print()

attempt = QuizAttempt(
    question_id="q_prod_vet_3",
    knowledge_point_id=kp_prod_vet.id,
    module_id=kp_prod_vet.module_id,
    is_correct=True,
    user_answer="Area do paralelogramo formado por A e B",
)
service.record_quiz_attempt(progress, attempt)
service.update_mastery(progress, kp_prod_vet.id,
                       service.calculate_mastery(progress, kp_prod_vet.id))
service.save(progress)

m = policy.display_mastery(progress, kp_prod_vet)
status = policy.objective_status(progress, kp_prod_vet)
tutor(f"Exato! |A x B| = area do paralelogramo. Mastery: {m:.0%}")
tutor(f"Status: {status}")
print()

# ============================================
# SESSAO 3: CONCEITO - Feynman
# ============================================
print("\n" + "=" * 66)
print("  SESSAO 3: Gate qualitativo - 'Coordenadas Cartesianas' (CONCEITO)")
print("=" * 66)

kp_cart = modulo.knowledge_points[4]

tutor("Vamos usar a tecnica de Feynman. Explique coordenadas cartesianas")
tutor("em suas proprias palavras, como se estivesse ensinando alguem.")
print()
aluno("Coordenadas cartesianas usam tres eixos perpendiculares x, y, z.")
aluno("Cada ponto no espaco e representado por (x, y, z).")
aluno("O vetor posicao e R = xi + yj + zk.")
print()

# Tutor avalia - passou
service.record_qualitative(progress, kp_cart.id, passed=True,
    evidence="Explicou eixos ortogonais, representacao (x,y,z), vetor posicao")
status = policy.objective_status(progress, kp_cart)
tutor("Muito bem! Voce mencionou eixos ortogonais, a representacao (x,y,z)")
tutor("e o vetor posicao. CONCEITO APROVADO!")
tutor(f"Status: {status}")
print()

tutor("Agora, e as coordenadas cilindricas? Como se relacionam com as cartesianas?")
print()
aluno("Coordenadas cilindricas usam rho (raio), phi (angulo) e z (altura).")
aluno("x = rho cos phi, y = rho sen phi, z = z.")
aluno("O elemento de volume e dv = rho drho dphi dz.")
print()

kp_cil = modulo.knowledge_points[5]
service.record_qualitative(progress, kp_cil.id, passed=True,
    evidence="Explicou rho/phi/z, relacao com cartesianas, elemento de volume")
status = policy.objective_status(progress, kp_cil)
tutor("Perfeito! Voce cobriu as variaveis, a transformacao e o elemento")
tutor("de volume. CONCEITO APROVADO!")
print()

# ============================================
# SESSAO 4: EMT Dialogue - Coordenadas Esfericas
# ============================================
print("\n" + "=" * 66)
print("  SESSAO 4: EMT Dialogue - 'Coordenadas Esfericas' (CONCEITO)")
print("  Tecnica: Pump -> Hint -> Prompt -> Assertion")
print("=" * 66)

kp_esf = modulo.knowledge_points[6]
dialogue = DialogueState(student_id="hayt", skill=kp_esf.name)
expectations = [
    "Coordenadas esfericas usam r (raio), theta (polar), phi (azimutal)",
    "Relacao com cartesianas: x = r sen theta cos phi",
    "Elemento de volume: dv = r^2 sen theta dr dtheta dphi",
]

print()
for exp in expectations:
    move = dialogue.current_move
    if move == DialogueMove.PUMP:
        tutor(f"Me explique {kp_esf.name} nas suas palavras.")
    elif move == DialogueMove.HINT:
        tutor(f"Pense na relacao com as coordenadas cartesianas.")
    elif move == DialogueMove.PROMPT:
        tutor(f"Complete: o elemento de volume em esfericas e dv = ___")

    print()

    if move == DialogueMove.PUMP:
        aluno("Usam r, theta e phi. r e a distancia da origem, theta e o")
        aluno("angulo do eixo z, phi e o angulo no plano xy.")
        dialogue.record_success()
        print(f"           >> EMT: Acertou -> avanca para HINT\n")
    elif move == DialogueMove.HINT:
        aluno("x = r sen theta cos phi, y = r sen theta sen phi, z = r cos theta")
        dialogue.record_success()
        print(f"           >> EMT: Acertou -> avanca para PROMPT\n")
    elif move == DialogueMove.PROMPT:
        aluno("dv = r^2 sen theta dr dtheta dphi")
        dialogue.record_success()
        print(f"           >> EMT: Acertou! Resposta completa.\n")

# Registrar conceito como mastered
service.record_qualitative(progress, kp_esf.id, passed=True,
    evidence="Explicou r/theta/phi, transformacao cartesiana, elemento de volume")

# ============================================
# RESUMO DA SESSAO
# ============================================
print("\n" + "=" * 66)
print("  RESUMO DA SESSAO DE APRENDIZADO")
print("=" * 66)

final_map = policy.map_summary(progress)
c = final_map["counts"]
print(f"\n  Modulo: {modulo.name}")
print(f"  Progresso: {c['mastered']}/{c['total']} mastered")
status_counts = {"mastered": 0, "learning": 0, "new": 0}
for mod in final_map["modules"]:
    for kp in mod["knowledge_points"]:
        s = kp["status"]
        status_counts[s] = status_counts.get(s, 0) + 1
        icon = {"mastered": " [OK]", "learning": " [..]", "new": " [  ]"}.get(s, " ???")
        print(f"  {icon} {kp['name']} (mastery {kp['mastery']:.0%})")

print(f"\n  Sessoes realizadas: 4")
print(f"    1. Escalares e Vetores (MEMORIA) - gate quantitativo 90%")
print(f"    2. Produto Vetorial (PROCEDURE) - gate quantitativo 90%")
print(f"    3. Coordenadas Cartesianas/Cilindricas (CONCEITO) - Feynman")
print(f"    4. Coordenadas Esfericas (CONCEITO) - EMT Dialogue")

# Limpeza
if store_path.exists():
    store_path.unlink()

print(f"\n  Dados de aprendizado persistidos e limpos.")
print(f"  Para manter os dados, remova a linha de limpeza ao final do script.")
