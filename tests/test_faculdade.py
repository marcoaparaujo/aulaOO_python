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

