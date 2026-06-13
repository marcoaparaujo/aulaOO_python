from codigo.exercicioRelampagoSurpresaNatal import *

def test_deve_calcular_salario_liquido_sem_ocorrencias_sem_dependente():
    cargo = Cargo()
    cargo.set_salario_bruto(1000)
    funcionario = Funcionario()
    funcionario.set_cargo(cargo)
    assert funcionario.calcular_salario_liquido(6, 26) == 1000

def test_nao_deve_calcular_salario_liquido_sem_cargo():
    funcionario = Funcionario()
    assert funcionario.calcular_salario_liquido(6, 26) == 0

def test_deve_calcular_salario_liquido_com_ocorrencias():
    cargo = Cargo()
    cargo.set_salario_bruto(1000)
    funcionario = Funcionario()
    funcionario.set_cargo(cargo)
    ocorrencia_acrescimo = Ocorrencia()
    ocorrencia_acrescimo.set_desricao_ocorrencia("acrescimo")
    ocorrencia_acrescimo.set_data_ocorrencia("01/06/2026")
    ocorrencia_acrescimo.set_valor_acrescimo(30)
    funcionario.registrar_ocorrencia(ocorrencia_acrescimo)
    ocorrencia_desconto = Ocorrencia()
    ocorrencia_desconto.set_desricao_ocorrencia("desconto")
    ocorrencia_desconto.set_data_ocorrencia("05/06/2026")
    ocorrencia_desconto.set_valor_desconto(10)
    funcionario.registrar_ocorrencia(ocorrencia_desconto)

    ocorrencia_acrescimo2 = Ocorrencia()
    ocorrencia_acrescimo2.set_desricao_ocorrencia("acrescimo")
    ocorrencia_acrescimo2.set_data_ocorrencia("01/05/2026")
    ocorrencia_acrescimo2.set_valor_acrescimo(30)
    funcionario.registrar_ocorrencia(ocorrencia_acrescimo2)
    ocorrencia_desconto2 = Ocorrencia()
    ocorrencia_desconto2.set_desricao_ocorrencia("desconto")
    ocorrencia_desconto2.set_data_ocorrencia("05/06/2025")
    ocorrencia_desconto2.set_valor_desconto(10)
    funcionario.registrar_ocorrencia(ocorrencia_desconto2)

    assert funcionario.calcular_salario_liquido(6, 2026) == 1020

def test_deve_obter_mes_ocorrencia():
    ocorrencia = Ocorrencia()
    ocorrencia.set_data_ocorrencia("13/06/2026")
    assert ocorrencia.get_mes_ocorrencia() == 6

def test_deve_obter_ano_ocorrencia():
    ocorrencia = Ocorrencia()
    ocorrencia.set_data_ocorrencia("13/06/2026")
    assert ocorrencia.get_ano_ocorrencia() == 2026

def test_deve_calcular_salario_liquido_com_dependentes():
    cargo = Cargo()
    cargo.set_salario_bruto(1000)
    funcionario = Funcionario()
    funcionario.set_cargo(cargo)
    dependente1 = Dependente()
    dependente1.set_data_nascimento("10/01/1990")
    dependente2 = Dependente()
    dependente2.set_data_nascimento("01/01/2026")
    funcionario.associar_dependente(dependente1)
    funcionario.associar_dependente(dependente2)
    assert funcionario.calcular_salario_liquido(6, 2026) == 1100

def test_calcular_idade():
    dependente = Dependente()
    dependente.set_data_nascimento("10/01/1990")
    assert dependente.calcular_idade() == 36

def test_deve_retornar_nomes_dependentes():
    dependente1 = Dependente()
    dependente1.set_nome("Deivid")
    dependente1.set_data_nascimento("10/01/1990")
    dependente2 = Dependente()
    dependente2.set_nome("Gabryel")
    dependente2.set_data_nascimento("09/08/2005")
    funcionario = Funcionario()
    funcionario.associar_dependente(dependente1)
    funcionario.associar_dependente(dependente2)
    assert funcionario.obter_nomes_dependentes() == ["Deivid - 10/01/1990", "Gabryel - 09/08/2005"]

def test_deve_calcular_proximo_aniversario():
    dependente = Dependente()
    dependente.set_data_nascimento("08/09/2001")
    assert dependente.calcular_proximo_aniversario() == "8/9/2026"

def test_deve_calcular_proximo_aniversario_ano_seguinte():
    dependente = Dependente()
    dependente.set_data_nascimento("10/01/1990")
    assert dependente.calcular_proximo_aniversario() == "10/1/2027"

def test_deve_obter_dia_semana_proximo_aniversario():
    dependente = Dependente()
    dependente.set_data_nascimento("10/01/1990")
    assert dependente.calcular_nome_dia_semana() == "Domingo"