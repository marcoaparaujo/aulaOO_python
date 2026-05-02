from codigo.exercicioRelampagoSurpresaPi import *
from codigo.funcionario import Diretor


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
    curso = Curso(TipoEnsino())
    aluno = Aluno(curso)
    estado = Estado()
    estado.set_nome("MG")
    cidade = Cidade(estado)
    aluno.set_naturalidade(cidade)
    assert aluno.get_nome_estado_naturalidade() == "MG"

def test_deve_retornar_pessoa_sem_naturalidade():
    curso = Curso(TipoEnsino())
    aluno = Aluno(curso)
    assert aluno.get_nome_estado_naturalidade() == "Pessoa sem naturalidade"

def test_deve_retornar_escolaridade_coordenador_curso():
    coordenador = Professor()
    escolaridade = Escolaridade()
    curso = Curso(TipoEnsino())
    coordenador.set_escolaridade(escolaridade)
    curso.set_coordenador(coordenador)
    escolaridade.set_descricao("Doutorado")
    assert curso.get_descricao_escolaridade_coordenador() == "Doutorado"

def test_deve_retornar_curso_sem_coordenador():
    curso = Curso(TipoEnsino())
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
    curso = Curso(TipoEnsino())
    curso.set_escola(escola)
    assert curso.get_nome_estado() == "MG"

def test_deve_retornar_curso_sem_escola():
    curso = Curso(TipoEnsino())
    assert curso.get_nome_estado() == "Curso sem escola"

def test_deve_retonar_nome_estado_aluno():
    estado = Estado()
    estado.set_nome("MG")
    cidade = Cidade(estado)
    escola = Escola()
    escola.set_cidade(cidade)
    curso = Curso(TipoEnsino())
    curso.set_escola(escola)
    aluno = Aluno(curso)
    assert aluno.get_nome_estado() == "MG"

def test_deve_retornar_nome_diretor_escola():
    escolaridade = Escolaridade()
    escolaridade.set_descricao("Doutorado")
    professor = Professor()
    professor.set_escolaridade(escolaridade)
    escola = Escola()
    escola.set_diretor(professor)
    assert escola.get_descricao_escolaridade_diretor() == "Doutorado"

def test_deve_retornar_escola_sem_diretor():
    escola = Escola()
    assert escola.get_descricao_escolaridade_diretor() == "Escola sem diretor"

def test_deve_retornar_nome_tipo_ensino_curso():
    tipo_ensino = TipoEnsino()
    tipo_ensino.set_nome("Superior")
    curso = Curso(tipo_ensino)
    assert curso.get_nome_tipo_ensino() == "Superior"

def test_deve_retornar_tipo_ensino_professor():
    tipo_ensino = TipoEnsino()
    tipo_ensino.set_nome("Superior")
    curso = Curso(tipo_ensino)
    professor = Professor()
    professor.set_curso(curso)
    assert professor.get_nome_tipo_ensino() == "Superior"

def test_deve_retornar_professor_sem_tipo_ensino():
    professor = Professor()
    assert professor.get_nome_tipo_ensino() == "Professor sem curso"

def test_deve_retornar_cidade_naturalidade_professor():
    cidade = Cidade(Estado())
    professor = Professor()
    professor.set_naturalidade(cidade)
    cidade.set_nome("Vassouras")
    assert professor.get_nome_cidade_naturalidade() == "Vassouras"

def test_deve_retornar_professor_sem_cidade_naturalidade():
    professor = Professor()
    assert professor.get_nome_cidade_naturalidade() == "Pessoa sem naturalidade"

def test_deve_retornar_nome_coordenador_curso():
    professor = Professor()
    professor.set_nome("Marina")
    curso = Curso(TipoEnsino())
    curso.set_coordenador(professor)
    assert curso.get_nome_coordenador() == "Marina"

def test_deve_retornar_curso_sem_coordenador():
    curso = Curso(TipoEnsino())
    assert curso.get_nome_coordenador() == "Curso sem coordenador"

def test_deve_retornar_nome_coordenador_aluno():
    curso = Curso(TipoEnsino())
    aluno = Aluno(curso)
    professor = Professor()
    professor.set_nome("Julia")
    curso.set_coordenador(professor)
    assert aluno.get_nome_coordenador() == "Julia"

def test_deve_retornar_nome_diretor_escola():
    professor = Professor()
    professor.set_nome("Marina")
    escola = Escola()
    escola.set_diretor(professor)
    assert escola.get_nome_diretor() == "Marina"

def test_deve_retornar_escola_sem_diretor():
    escola = Escola()
    assert escola.get_nome_diretor() == "Escola sem diretor"

def test_deve_retornar_nome_diretor_curso():
    professor = Professor()
    professor.set_nome("Marina")
    escola = Escola()
    escola.set_diretor(professor)
    curso = Curso(TipoEnsino())
    curso.set_escola(escola)
    assert curso.get_nome_diretor() == "Marina"

def test_deve_retornar_curso_sem_diretor():
    curso = Curso(TipoEnsino())
    assert curso.get_nome_diretor() == "Curso sem escola"

def test_deve_retornar_nome_diretor_professor():
    professor = Professor()
    diretor = Professor()
    diretor.set_nome("Marina")
    curso = Curso(TipoEnsino())
    escola = Escola()
    curso.set_escola(escola)
    escola.set_diretor(diretor)
    professor.set_curso(curso)
    assert professor.get_nome_diretor() == "Marina"

def test_deve_retornar_professor_sem_diretor():
    professor = Professor()
    assert professor.get_nome_diretor() == "Professor sem curso"

def test_deve_retornar_nome_coordeenador_professor():
    professor = Professor()
    coordenador = Professor()
    coordenador.set_nome("Julia")
    curso = Curso(TipoEnsino())
    professor.set_curso(curso)
    curso.set_coordenador(coordenador)
    assert professor.get_nome_coordenador() == "Julia"

def test_deve_retornar_professor_sem_coordenador():
    professor = Professor()
    assert professor.get_nome_coordenador() == "Professor sem curso"
