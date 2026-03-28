from codigo.carro import *

def test_deve_associar_marca():
    carro = Carro()
    carro.set_marca("Mitsubishi")
    assert carro.get_marca() == "Mitsubishi"

def test_deve_associar_ano():
    carro = Carro()
    carro.set_ano(2020)
    assert carro.get_ano() == 2020

def test_deve_acelerar_carro():
    carro = Carro()
    carro.ligar()
    carro.set_velocidade_atual(50)
    carro.acelerar(60)
    assert carro.get_velocidade_atual() == 110

def test_nao_deve_acelerar_carro_desligado():
    carro = Carro()
    carro.desligar()
    carro.acelerar(10)
    assert carro.get_velocidade_atual() == 0

def test_deve_frear_carro():
    carro = Carro()
    carro.ligar()
    carro.set_velocidade_atual(50)
    carro.frear(30)
    assert carro.get_velocidade_atual() == 20

def test_nao_deve_ter_velocidade_negativa():
    carro = Carro()
    carro.ligar()
    carro.set_velocidade_atual(50)
    carro.frear(51)
    assert carro.get_velocidade_atual() == 0

def test_nao_deve_frear_carro_desligado():
    carro = Carro()
    carro.desligar()
    carro.acelerar(10)
    carro.frear(9)
    assert carro.get_velocidade_atual() == 0


def test_deve_ligar_carro_desligado():
    carro = Carro()
    carro.desligar()
    carro.ligar()
    assert carro.get_ligado()


def test_nao_deve_ligar_carro_ligado():
    carro = Carro()
    carro.ligar()
    carro.ligar()
    assert carro.get_ligado()


def test_deve_desligar_carro_ligado():
    carro = Carro()
    carro.ligar()
    carro.acelerar(10)
    carro.desligar()
    assert carro.get_velocidade_atual() == 0


def test_nao_deve_desligar_carro_desligado():
    carro = Carro()
    carro.desligar()
    carro.desligar()
    assert not carro.get_ligado()