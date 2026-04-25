from codigo.exercicioRelampagoSurpresaPi import *

def test_deve_retornar_pessoa_sem_escolaridade():
    professor = Professor()
    assert professor.get_descricao_escolaridade() == "Pessoa sem escolaridade"

def test_deve_retornar_escolaridade_professor():
    professor = Professor()
    escolaridade = Escolaridade()
    escolaridade.set_descricao("Doutorado")
    professor.set_escolaridade(escolaridade)
    assert professor.get_descricao_escolaridade() == "Doutorado"

def test_deve_retornar_nome_estado_cidade():
    estado = Estado()
    estado.set_nome("MG")
    cidade = Cidade(estado)
    assert cidade.get_nome_estado() == "MG"

def test_deve_retornar_estado_naturalidade_aluno():
    curso = Curso()
    aluno = Aluno(curso)
    estado = Estado()
    estado.set_nome("MG")
    cidade = Cidade(estado)
    aluno.set_naturalidade(cidade)
    assert aluno.get_nome_estado_naturalidade() == "MG"

def test_deve_retornar_pessoa_sem_naturalidade():
    curso = Curso()
    aluno = Aluno(curso)
    assert aluno.get_nome_estado_naturalidade() == "Pessoa sem naturalidade"

def test_deve_retornar_escolaridade_coordenador_curso():
    coordenador = Professor()
    escolaridade = Escolaridade()
    curso = Curso()
    coordenador.set_escolaridade(escolaridade)
    curso.set_coordenador(coordenador)
    escolaridade.set_descricao("Doutorado")
    assert curso.get_descricao_escolaridade_coordenador() == "Doutorado"

def test_deve_retornar_curso_sem_coordenador():
    curso = Curso()
    assert curso.get_descricao_escolaridade_coordenador() == "Curso sem coordenador"


def test_deve_retornar_nome_estado_escola():
    estado = Estado()
    estado.set_nome("MG")
    cidade = Cidade(estado)
    escola = Escola()
    escola.set_cidade(cidade)
    assert escola.get_nome_estado() == "MG"

def test_deve_retonar_escola_sem_cidade():
    escola = Escola()
    assert escola.get_nome_estado() == "Escola sem cidade"

def test_deve_retornar_nome_estado_curso():
    estado = Estado()
    estado.set_nome("MG")
    cidade = Cidade(estado)
    escola = Escola()
    escola.set_cidade(cidade)
    curso = Curso()
    curso.set_escola(escola)
    assert curso.get_nome_estado() == "MG"

def test_deve_retornar_curso_sem_escola():
    curso = Curso()
    assert curso.get_nome_estado() == "Curso sem escola"

def test_deve_retonar_nome_estado_aluno():
    estado = Estado()
    estado.set_nome("MG")
    cidade = Cidade(estado)
    escola = Escola()
    escola.set_cidade(cidade)
    curso = Curso()
    curso.set_escola(escola)
    aluno = Aluno(curso)
    assert aluno.get_nome_estado() == "MG"