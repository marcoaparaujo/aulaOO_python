class Produto:

    def __init__(self, nome="", preco=0.0, quantidade_estoque=0, categoria=""):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.categoria = categoria

    def get_nome(self):
        return self.nome

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.quantidade_estoque = self.quantidade_estoque + quantidade
            return "Foram adicionadas " + str(quantidade) + " unidades. Estoque atual: " + str(self.quantidade_estoque)
        return "Valor inválido para adicionar estoque"

    def remover_estoque(self, quantidade):
        if quantidade > 0 and quantidade <= self.quantidade_estoque:
            self.quantidade_estoque = self.quantidade_estoque - quantidade
            saida = "Foram removidas " + str(quantidade) + " unidades. Estoque atual: " + str(self.quantidade_estoque)
        else:
            saida = "Valor inválido para remover estoque"
        return saida

    def aplicar_desconto(self, percentual):
        if percentual > 0 and percentual < 100:
            desconto = self.preco * (percentual/100)
            novo_preco = self.preco - desconto
            self.preco = novo_preco
            saida = "Preço com desconto de " + str(percentual) + " %: R$ " + "{:.2f}".format(self.preco)
            saida = f"Preço com desconto de {str(percentual)}%: R$ {self.preco:.2f}"

        else:
            saida = "Percentual de desconto inválido"
        return saida