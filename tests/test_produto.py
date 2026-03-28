from codigo.produto import *

def test_deve_instanciar_produto():
    produto = Produto()
    produto = Produto("Relogio")
    produto = Produto("Relogio", 100)
    produto = Produto("Relogio", 100, 10)
    produto = Produto("Relogio", 100, 10, "Social")
    assert produto.get_nome() == "Relogio"