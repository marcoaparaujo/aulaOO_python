from codigo.funcionario import *

def test_deve_exibir_dados():
    funcionario = Administrativo()
    funcionario.set_nome("Pedro")
    funcionario.set_cargo("Estagiario")
    funcionario.set_departamento("Limpeza")
    funcionario.set_salario(0)
    assert funcionario.exibir_dados() == "Pedro, Estagiario, 0, Limpeza"

def test_deve_alocar_cpf():
    funcionario = Administrativo()
    assert funcionario.get_cpf() == 0

def test_deve_calcular_salario_administrativo():
    funcionario = Administrativo()
    funcionario.calcular_salario()
    assert funcionario.get_salario() == 1000

def test_deve_calcular_salario_professor():
    funcionario = Professor()
    funcionario.calcular_salario()
    assert funcionario.get_salario() == 2000

def test_deve_calcular_salario_diretor():
    funcionario = Diretor()
    funcionario.calcular_salario()
    assert funcionario.get_salario() == 5000

def test_deve_calcular_salario_vigia():
    funcionario = Vigia()
    funcionario.calcular_salario()
    assert funcionario.get_salario() == 1000

def test_deve_obter_titulacao_professor():
    funcionario = Professor()
    funcionario.set_titulacao("Doutor")
    assert funcionario.get_titulacao() == "Doutor"