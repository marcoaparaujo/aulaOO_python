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
    aluno = Aluno()
    estado = Estado()
    estado.set_nome("MG")
    cidade = Cidade(estado)
    aluno.set_naturalidade(cidade)
    assert aluno.get_nome_estado_naturalidade() == "MG"

def test_deve_retornar_pessoa_sem_naturalidade():
    aluno = Aluno()
    assert aluno.get_nome_estado_naturalidade() == "Pessoa sem naturalidade"