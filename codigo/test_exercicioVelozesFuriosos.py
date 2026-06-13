from codigo.exercicioVelozesFuriosos import *

def test_deve_alugar_veiculo():
    carro = Carro("Fiat Uno", "ABC1234", 100)
    assert carro.alugar(Cliente("Marcelo"), 10) == True

def test_nao_deve_alugar_veiculo():
    carro = Carro("Fiat Uno", "ABC1234", 100)
    carro.alugar(Cliente("Marcelo"), 10)
    assert carro.alugar(Cliente("Marcelo"), 10) == False

def test_deve_retornar_historico():
    carro = Carro("Fiat Uno", "ABC1234", 100)
    carro.alugar(Cliente("Marcelo"), 10)
    carro.devolver()
    assert carro.get_historico() == ["Veiculo placa ABC1234 alugado pelo cliente Marcelo no valor de R$ 1000.00", "Veiculo placa ABC1234 devolvido"]

def test_deve_devolver_veiculo():
    carro = Carro("Fiat Uno", "ABC1234", 100)
    carro.alugar(Cliente("Marcelo"), 10)
    assert carro.devolver() == True

def test_nao_deve_devolver_veiculo():
    carro = Carro("Fiat Uno", "ABC1234", 100)
    assert carro.devolver() == False

def test_deve_calcular_aluguel_carro():
    carro = Carro("Fiat Uno", "ABC1234", 100)
    assert carro.calcular_aluguel(10) == 1000

def test_deve_calcular_aluguel_moto_acrescimo_10():
    moto = Moto("ABC2345", 20)
    assert moto.calcular_aluguel(30) == 660

def test_deve_calcular_aluguel_moto_acrescimo_20():
    moto = Moto("ABC2345", 20)
    assert moto.calcular_aluguel(29) == 696

