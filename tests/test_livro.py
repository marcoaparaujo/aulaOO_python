from codigo.livro import *

def test_deve_atribuir_numero_paginas():
    livro = Livro()
    livro.set_numero_paginas(100)
    assert livro.get_numero_paginas() == 100

def test_nao_deve_atribuir_numero_paginas():
    livro = Livro()
    livro.set_numero_paginas(-1)
    assert livro.get_numero_paginas() == 0

def test_deve_atribuir_pagina_marcada():
    livro = Livro()
    livro.set_numero_paginas(100)
    livro.set_pagina_marcada(1)
    assert livro.get_pagina_marcada() == 1

def test_nao_deve_atribuir_pagina_marcada_negativa():
    livro = Livro()
    livro.set_numero_paginas(100)
    livro.set_pagina_marcada(-1)
    assert livro.get_pagina_marcada() == 0

def test_nao_deve_atribuir_pagina_marcada_alem_limite():
    livro = Livro()
    livro.set_numero_paginas(100)
    livro.set_pagina_marcada(101)
    assert livro.get_pagina_marcada() == 0

def test_deve_abrir_livro():
    livro = Livro()
    livro.abrir()
    assert livro.get_pagina_atual() == 1

def test_deve_fechar_livro():
    livro = Livro()
    livro.fechar()
    assert livro.get_pagina_atual() == 0

def test_nao_deve_alterar_pagina_negativa():
    livro = Livro()
    livro.set_numero_paginas(100)
    livro.set_pagina_atual(10)
    livro.set_pagina_atual(-1)
    assert livro.get_pagina_atual() == 10

def test_nao_deve_alterar_pagina_alem_limite():
    livro = Livro()
    livro.abrir()
    livro.set_numero_paginas(100)
    livro.set_pagina_atual(101)
    assert livro.get_pagina_atual() == 1

def test_deve_marcar_pagina():
    livro = Livro()
    livro.set_numero_paginas(100)
    livro.marcar_pagina(5)
    assert livro.get_pagina_marcada() == 5

def test_nao_deve_marcar_pagina_negativa():
    livro = Livro()
    livro.set_numero_paginas(100)
    livro.marcar_pagina(-1)
    livro.get_pagina_marcada() == 0

def test_nao_deve_marcar_pagina_alem_limite():
    livro = Livro()
    livro.set_numero_paginas(100)
    livro.marcar_pagina(101)
    livro.get_pagina_marcada() == 0


def test_deve_avancar_pagina():
    livro = Livro()
    livro.abrir()
    livro.set_numero_paginas(100)
    livro.set_pagina_atual(99)
    livro.avancar_pagina()
    assert livro.get_pagina_atual() == 100

def test_nao_deve_avancar_pagina():
    livro = Livro()
    livro.abrir()
    livro.set_numero_paginas(100)
    livro.set_pagina_atual(100)
    livro.avancar_pagina()
    assert livro.get_pagina_atual() == 100

def test_nao_deve_avancar_pagina_livro_fechado():
    livro = Livro()
    livro.set_numero_paginas(100)
    livro.fechar()
    livro.avancar_pagina()
    assert livro.get_pagina_atual() == 0


def test_nao_deve_retroceder_pagina():
    livro = Livro()
    livro.abrir()
    livro.retroceder_pagina()
    assert livro.get_pagina_atual() == 1

def test_nao_deve_retroceder_pagina_livro_fechado():
    livro = Livro()
    livro.abrir()
    livro.fechar()
    livro.retroceder_pagina()
    assert livro.get_pagina_atual() == 0



