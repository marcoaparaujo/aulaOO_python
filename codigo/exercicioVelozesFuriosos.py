class Veiculo:
    def __init__(self, placa, valor):
        self.placa = placa
        self.valor = valor
        self.alugado = False
        self.historico = []
    def get_placa(self):
        return self.placa
    def set_placa(self, placa):
        self.placa = placa
    def get_valor(self):
        return self.valor
    def set_valor(self, valor):
        self.valor = valor
    def get_alugado(self):
        return self.alugado
    def set_alugado(self, alugado):
        self.alugado = alugado
    def get_historico(self):
        return self.historico
    def set_historico(self, historico):
        self.historico = historico
    def registrar_historico(self, historico):
        self.historico.append(historico)
    def alugar(self, cliente, dias):
        if self.alugado:
            return False
        else:
            self.alugado = True
            self.registrar_historico(f"Veiculo placa {self.placa} alugado pelo cliente {cliente.get_nome()} no valor de R$ {self.calcular_aluguel(dias):.2f}")
            return True
    def devolver(self):
        if not self.alugado:
            return False
        else:
            self.alugado = False
            self.registrar_historico(f"Veiculo placa {self.placa} devolvido")
            return True
    def listar_historico(self):
        for historico in self.historico:
            print(historico)

class Carro(Veiculo):
    def __init__(self, modelo, placa, valor):
        super().__init__(placa, valor)
        self.modelo = modelo
    def get_modelo(self):
        return self.modelo
    def set_modelo(self, modelo):
        self.modelo = modelo
    def calcular_aluguel(self, dias):
        return self.valor * dias

class Moto(Veiculo):
    def __init__(self, placa, valor):
        super().__init__(placa, valor)
    def calcular_aluguel(self, dias):
        if dias >= 30:
            return self.valor * dias * 1.1
        else:
            return self.valor * dias * 1.2

class Cliente:
    def __init__(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome
