from codigo.faculdade import *
from codigo.faculdade import Aluno


def test_deve_matricular_aluno():
    aluno = Aluno()
    curso = Curso()
    curso.matricular(aluno)
    assert curso.verificar_matricula(aluno) == True

def test_nao_deve_matricular_aluno():
    aluno = Aluno()
    curso = Curso()
    assert curso.verificar_matricula(aluno) == False

def test_deve_desmatricular_aluno():
    aluno = Aluno()
    curso = Curso()
    curso.matricular(aluno)
    curso.desmatricular(aluno)
    assert curso.verificar_matricula(aluno) == False

def test_deve_retornar_alunos_curso():
    aluno1 = Aluno()
    aluno2 = Aluno()
    curso = Curso()
    curso.matricular(aluno1)
    curso.matricular(aluno2)
    assert curso.get_alunos() == [aluno1, aluno2]

def test_deve_retornar_nomes_alunos_curso():
    aluno1 = Aluno()
    aluno1.set_nome("Kayke")
    aluno2 = Aluno()
    aluno2.set_nome("Heryqui")
    aluno3 = Aluno()
    aluno3.set_nome("Hartur")
    aluno4 = Aluno()
    aluno4.set_nome("Dyegu")
    curso = Curso()
    curso.matricular(aluno1)
    curso.matricular(aluno2)
    curso.matricular(aluno3)
    curso.matricular(aluno4)
    assert curso.get_nomes_alunos() == ["Kayke", "Heryqui", "Hartur", "Dyegu"]

def test_deve_retornar_quantidade_alunos_curso():
    aluno1 = Aluno()
    aluno2 = Aluno()
    aluno3 = Aluno()
    aluno4 = Aluno()
    curso = Curso()
    curso.matricular(aluno1)
    curso.matricular(aluno2)
    curso.matricular(aluno3)
    curso.matricular(aluno4)
    assert curso.get_quantidade_alunos_curso() == 4

def test_deve_retornar_nome_professor_turma():
    professor = Professor()
    professor.set_nome("Thacyu")
    turma = Turma()
    turma.set_professor(professor)
    assert turma.get_nome_professor() == "Thacyu"

def test_deve_retornar_turma_sem_professor():
    turma = Turma()
    assert turma.get_nome_professor() == "Turma sem professor"

def test_deve_retornar_nomes_alunos_turma():
    aluno1 = Aluno()
    aluno1.set_nome("Kayke")
    aluno2 = Aluno()
    aluno2.set_nome("Heryqui")
    turma = Turma()
    turma.matricular(aluno1)
    turma.matricular(aluno2)
    assert turma.get_nomes_alunos() == ["Kayke", "Heryqui"]

def test_deve_retornar_nomes_professores_turmas_curso():
    curso = Curso()
    turma1 = Turma()
    turma2 = Turma()
    curso.criar_turma(turma1)
    curso.criar_turma(turma2)
    professor1 = Professor()
    professor2 = Professor()
    turma1.set_professor(professor1)
    turma2.set_professor(professor2)
    professor1.set_nome("Thacyu")
    professor2.set_nome("Phabyu")
    assert curso.get_nomes_professores() == ["Thacyu", "Phabyu"]

def test_deve_retornar_nomes_professores_turmas_curso2():
    curso = Curso()
    turma1 = Turma()
    turma2 = Turma()
    curso.criar_turma(turma1)
    curso.criar_turma(turma2)
    professor1 = Professor()
    turma1.set_professor(professor1)
    professor1.set_nome("Thacyu")
    assert curso.get_nomes_professores() == ["Thacyu"]

def test_deve_retornar_nomes_alunos_turmas_curso():
    curso = Curso()
    turma1 = Turma()
    turma2 = Turma()
    curso.criar_turma(turma1)
    curso.criar_turma(turma2)
    aluno1 = Aluno()
    aluno2 = Aluno()
    aluno3 = Aluno()
    aluno4 = Aluno()
    turma1.matricular(aluno1)
    turma1.matricular(aluno2)
    turma2.matricular(aluno3)
    turma2.matricular(aluno4)
    aluno1.set_nome("Kayke")
    aluno2.set_nome("Heryqui")
    aluno3.set_nome("Dyegu")
    aluno4.set_nome("Kayke")
    assert curso.get_nomes_alunos_turmas() == ["Kayke", "Heryqui", "Dyegu"]

def test_deve_retornar_nome_disciplina_turma():
    disciplina = Disciplina()
    disciplina.set_nome("Algoritmos")
    turma = Turma()
    turma.set_disciplina(disciplina)
    assert turma.get_nome_disciplina() == "Algoritmos"

def test_deve_retornar_nomes_disciplinas_turmas_curso():
    curso = Curso()
    turma1 = Turma()
    turma2 = Turma()
    turma3 = Turma()
    curso.criar_turma(turma1)
    curso.criar_turma(turma2)
    curso.criar_turma(turma3)
    disciplina1 = Disciplina()
    disciplina2 = Disciplina()
    turma1.set_disciplina(disciplina1)
    turma2.set_disciplina(disciplina2)
    disciplina1.set_nome("Algoritmos")
    disciplina2.set_nome("Engenharia de requisitos")
    assert curso.get_nomes_disciplinas_turmas() == ["Algoritmos", "Engenharia de requisitos"]

def test_deve_vericar_presenca_aluno_turma():
    aluno = Aluno()
    turma = Turma()
    turma.matricular(aluno)
    assert turma.verificar_aluno(aluno) == True

def test_deve_vericar_ausencia_aluno_turma():
    aluno = Aluno()
    turma = Turma()
    assert turma.verificar_aluno(aluno) == False

def test_deve_vericar_presenca_turma_curso():
    curso = Curso()
    turma = Turma()
    curso.criar_turma(turma)
    assert curso.verificar_turma(turma) == True

def test_deve_vericar_ausencia_turma_curso():
    curso = Curso()
    turma = Turma()
    assert curso.verificar_turma(turma) == False

def test_deve_desmatricular_aluno_turma():
    aluno = Aluno()
    aluno.set_nome("Kayke")
    turma = Turma()
    turma.matricular(aluno)
    turma.desmatricular(aluno)
    assert turma.verificar_aluno(aluno) == False

def test_deve_fechar_turma_curso():
    curso = Curso()
    turma = Turma()
    curso.criar_turma(turma)
    curso.excluir_turma(turma)
    assert curso.verificar_turma(turma) == False

def test_nao_deve_matricular_aluno_turma_repetido():
    aluno = Aluno()
    aluno.set_nome("Kayke")
    turma = Turma()
    turma.matricular(aluno)
    turma.matricular(aluno)
    assert turma.get_nomes_alunos() == ["Kayke"]

def test_nao_deve_matricular_aluno_curso_repetido():
    aluno = Aluno()
    aluno.set_nome("Kayke")
    curso = Curso()
    curso.matricular(aluno)
    curso.matricular(aluno)
    assert curso.get_nomes_alunos() == ["Kayke"]

def test_nao_deve_abrir_turma_curso_repetido():
    turma = Turma()
    curso = Curso()
    curso.criar_turma(turma)
    curso.criar_turma(turma)
    assert curso.get_turmas() == [turma]

def test_deve_encontrar_nome_aluno_curso():
    aluno = Aluno()
    aluno.set_nome("Kayke")
    curso = Curso()
    curso.matricular(aluno)
    assert curso.verificar_nome_aluno("Kayke") == True

def test_nao_deve_encontrar_nome_aluno_curso():
    curso = Curso()
    assert curso.verificar_nome_aluno("Kayke") == False
