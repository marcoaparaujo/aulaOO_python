class Funcionario:
    def __init__(self):
        self.cpf = 0
        self.salario = 0

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_salario(self):
        return self.salario

    def calcular_salario(self):
        self.salario = 1000
class Administrativo(Funcionario):
    def __init__(self):
        super().__init__()
        self.nome = ""
        self.cargo = ""
        self.salario = 0.0
        self.departamento = ""

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_cargo(self, cargo):
        self.cargo = cargo

    def set_salario(self, salario):
        self.salario = salario

    def set_departamento(self, departamento):
        self.departamento = departamento

    def exibir_dados(self):
        return f"{self.nome}, {self.cargo}, {self.salario}, {self.departamento}"

class Docente(Funcionario):
    def __init__(self):
        super().__init__()
        self.titulacao = ""
    def set_titulacao(self, titulacao):
        self.titulacao = titulacao
    def get_titulacao(self):
        return self.titulacao

class Professor(Docente):
    def __init__(self):
        super().__init__()

    def calcular_salario(self):
        self.salario = 2000

class Diretor(Docente):
    def __init__(self):
        super().__init__()

    def calcular_salario(self):
        self.salario = 5000

class Vigia(Funcionario):

    def __init__(self):
        super().__init__()

