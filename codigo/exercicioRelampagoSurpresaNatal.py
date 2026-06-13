from datetime import date
from datetime import datetime
class Pessoa:
    def __init__(self):
        self.nome = ""
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome

class Funcionario(Pessoa):
    def __init__(self):
        super().__init__()
        self.cargo = None
        self.dependentes = []
        self.ocorrencias = []
    def set_cargo(self, cargo):
        self.cargo = cargo
    def get_cargo(self):
        return self.cargo
    def set_dependentes(self, dependentes):
        self.dependentes = dependentes
    def get_dependentes(self):
        return self.dependentes
    def set_ocorrencias(self, ocorrencias):
        self.ocorrencias = ocorrencias
    def get_ocorrencias(self):
        return self.ocorrencias
    def associar_dependente(self, dependente):
        self.dependentes.append(dependente)
    def registrar_ocorrencia(self, ocorrencia):
        self.ocorrencias.append(ocorrencia)
    def calcular_salario_liquido(self, mes, ano):
        if self.cargo == None:
            salario_liquido = 0.0
        else:
            salario_liquido = self.cargo.get_salario_bruto()
            for ocorrencia in self.ocorrencias:
                if ocorrencia.get_mes_ocorrencia() == mes and ocorrencia.get_ano_ocorrencia() == ano:
                    if ocorrencia.get_descricao_ocorrencia() == "acrescimo":
                        salario_liquido += ocorrencia.get_valor_acrescimo()
                    else:
                        salario_liquido -= ocorrencia.get_valor_desconto()
            for dependente in self.dependentes:
                if dependente.calcular_idade() < 18:
                    salario_liquido += 100
        return salario_liquido
    def obter_nomes_dependentes(self):
        nomes = []
        for dependente in self.dependentes:
            nomes.append(f"{dependente.get_nome()} - {dependente.get_data_nascimento()}")
        return nomes

class Dependente(Pessoa):
    def __init__(self):
        super().__init__()
        self.data_nascimento = ""
    def set_data_nascimento(self, data_nascimento):
        self.data_nascimento = data_nascimento
    def get_data_nascimento(self):
        return self.data_nascimento
    def calcular_idade(self):
        data_atual = date.today()
        data = datetime.strptime(self.data_nascimento, "%d/%m/%Y")
        idade = data_atual.year - data.year
        return idade
    def calcular_proximo_aniversario(self):
        data_atual = date.today()
        dia_data_atual = data_atual.day
        mes_data_atual = data_atual.month
        ano_data_atual = data_atual.year
        data_atual = str(dia_data_atual) + "/" + str(mes_data_atual) + "/" + str(ano_data_atual)
        data_atual = datetime.strptime(data_atual, "%d/%m/%Y")
        ano_data_atual = data_atual.year
        data = datetime.strptime(self.data_nascimento, "%d/%m/%Y")
        dia_data_nascimento = data.day
        mes_data_nascimento = data.month
        ano_data_nascimento = data.year
        proximo_aniversario = str(dia_data_nascimento) + "/" + str(mes_data_nascimento) + "/" + str(ano_data_atual)
        proximo_aniversario_date = datetime.strptime(proximo_aniversario, "%d/%m/%Y")
        if proximo_aniversario_date < data_atual:
            proximo_aniversario = str(dia_data_nascimento) + "/" + str(mes_data_nascimento) + "/" + str(ano_data_atual + 1)
        return proximo_aniversario
    def calcular_nome_dia_semana(self):
        dia_semana = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
        data = datetime.strptime(self.calcular_proximo_aniversario(), "%d/%m/%Y")
        return dia_semana[data.weekday()]

class Cargo:
    def __init__(self):
        self.salario_bruto = 0.0
    def get_salario_bruto(self):
        return self.salario_bruto
    def set_salario_bruto(self, salario_bruto):
        self.salario_bruto = salario_bruto

class Ocorrencia:
    def __init__(self):
        self.data_ocorrencia = ""
        self.valor_acrescimo = 0.0
        self.valor_desconto = 0.0
        self.descricao_ocorrencia = ""
    def set_data_ocorrencia(self, data_ocorrencia):
        self.data_ocorrencia = data_ocorrencia
    def get_data_ocorrencia(self):
        return self.data_ocorrencia
    def set_valor_acrescimo(self, valor_acrescimo):
        self.valor_acrescimo = valor_acrescimo
    def get_valor_acrescimo(self):
        return self.valor_acrescimo
    def set_valor_desconto(self, valor_desconto):
        self.valor_desconto = valor_desconto
    def get_valor_desconto(self):
        return self.valor_desconto
    def get_descricao_ocorrencia(self):
        return self.descricao_ocorrencia
    def set_desricao_ocorrencia(self, desricao_ocorrencia):
        self.descricao_ocorrencia = desricao_ocorrencia
    def converter_data_ocorrencia(self):
        return datetime.strptime(self.data_ocorrencia, "%d/%m/%Y")
    def get_mes_ocorrencia(self):
        return self.converter_data_ocorrencia().month
    def get_ano_ocorrencia(self):
        return self.converter_data_ocorrencia().year

