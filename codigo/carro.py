class Carro:

    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.ano = 0
        self.velocidade_atual = 0.0
        self.ligado = False

    def set_marca(self, marca):
        self.marca = marca

    def get_marca(self):
        return self.marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo
    def set_ano(self, ano):
        self.ano = ano

    def get_ano(self):
        return self.ano

    def set_velocidade_atual(self, velocidade_atual):
        self.velocidade_atual = velocidade_atual

    def get_velocidade_atual(self):
        return self.velocidade_atual

    def get_ligado(self):
        return self.ligado

    def set_ligado(self, ligado):
        self.ligado = ligado

    def acelerar(self, quantidade):
        if self.ligado:
            self.velocidade_atual = self.velocidade_atual + quantidade

    def frear(self, quantidade):
        if self.ligado:
            self.velocidade_atual = self.velocidade_atual - quantidade
            if self.velocidade_atual < 0:
                self.velocidade_atual = 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade_atual = 0