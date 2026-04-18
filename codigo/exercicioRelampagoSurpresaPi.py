class Estado:
    def __init__(self):
        self.nome = ""
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome

class Cidade:
    def __init__(self, estado):
        self.set_estado(estado)
    def get_estado(self):
        return self.estado
    def set_estado(self, estado):
        if estado != None:
            self.estado = estado
    def get_nome_estado(self):
        return self.estado.get_nome()
class Pessoa:
    def __init__(self):
        self.escolaridade = None
        self.naturalidade = None
    def set_escolaridade(self, escolaridade):
        self.escolaridade = escolaridade
    def get_escolaridade(self):
        return self.escolaridade
    def set_naturalidade(self, naturalidade):
        self.naturalidade = naturalidade
    def get_naturalidade(self):
        return self.naturalidade
    def get_descricao_escolaridade(self):
        if self.escolaridade == None:
            return "Pessoa sem escolaridade"
        else:
            return self.escolaridade.get_descricao()
    def get_nome_estado_naturalidade(self):
        if self.naturalidade == None:
            return "Pessoa sem naturalidade"
        else:
            return self.naturalidade.get_nome_estado()


class Professor (Pessoa):
    def __init__(self):
        super().__init__()

class Aluno(Pessoa):
    def __init__(self):
        super().__init__()

class Escolaridade:
    def __init__(self):
        self.descricao = ""
    def get_descricao(self):
        return self.descricao
    def set_descricao(self, descricao):
        self.descricao = descricao


