class TipoEnsino:
    def __init__(self):
        self.nome = ""
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
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
        self.nome = ""
    def get_estado(self):
        return self.estado
    def set_estado(self, estado):
        if estado != None:
            self.estado = estado
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome
    def get_nome_estado(self):
        return self.estado.get_nome()
class Pessoa:
    def __init__(self):
        self.escolaridade = None
        self.naturalidade = None
        self.nome = ""
    def set_escolaridade(self, escolaridade):
        self.escolaridade = escolaridade
    def get_escolaridade(self):
        return self.escolaridade
    def set_naturalidade(self, naturalidade):
        self.naturalidade = naturalidade
    def get_naturalidade(self):
        return self.naturalidade
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
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
    def get_nome_cidade_naturalidade(self):
        if self.naturalidade == None:
            return "Pessoa sem naturalidade"
        else:
            return self.naturalidade.get_nome()

class Professor (Pessoa):
    def __init__(self):
        super().__init__()
        self.curso = None
    def set_curso(self, curso):
        self.curso = curso
    def get_curso(self):
        return self.curso
    def get_nome_tipo_ensino(self):
        if self.curso == None:
            return "Professor sem curso"
        else:
            return self.curso.get_nome_tipo_ensino()
    def get_nome_diretor(self):
        if self.curso == None:
            return "Professor sem curso"
        else:
            return self.curso.get_nome_diretor()
    def get_nome_coordenador(self):
        if self.curso == None:
            return "Professor sem curso"
        else:
            return self.curso.get_nome_coordenador()

class Aluno(Pessoa):
    def __init__(self, curso):
        super().__init__()
        self.set_curso(curso)
    def get_curso(self):
        return self.curso
    def set_curso(self, curso):
        if curso != None:
            self.curso = curso
    def get_nome_estado(self):
        return self.curso.get_nome_estado()
    def get_nome_coordenador(self):
        return self.curso.get_nome_coordenador()

class Escolaridade:
    def __init__(self):
        self.descricao = ""
    def get_descricao(self):
        return self.descricao
    def set_descricao(self, descricao):
        self.descricao = descricao

class Curso:
    def __init__(self, tipo_ensino):
        self.coordenador = None
        self.escola = None
        self.set_tipo_ensino(tipo_ensino)
    def get_coordenador(self):
        return self.coordenador
    def set_coordenador(self, coordenador):
        self.coordenador = coordenador
    def set_escola(self, escola):
        self.escola = escola
    def get_escola(self):
        return self.escola
    def set_tipo_ensino(self, tipo_ensino):
        if tipo_ensino != None:
            self.tipo_ensino = tipo_ensino
    def get_tipo_ensino(self):
        return self.tipo_ensino
    def get_descricao_escolaridade_coordenador(self):
        if self.coordenador == None:
            return "Curso sem coordenador"
        else:
            return self.coordenador.get_descricao_escolaridade()
    def get_nome_estado(self):
        if self.escola == None:
            return "Curso sem escola"
        else:
            return self.escola.get_nome_estado()
    def get_nome_tipo_ensino(self):
        return self.tipo_ensino.get_nome()
    def get_nome_coordenador(self):
        if self.coordenador == None:
            return "Curso sem coordenador"
        else:
            return self.coordenador.get_nome()
    def get_nome_diretor(self):
        if self.escola == None:
            return "Curso sem escola"
        else:
            return self.escola.get_nome_diretor()

class Escola:
    def __init__(self):
        self.cidade = None
        self.diretor = None
    def get_cidade(self):
        return self.cidade
    def set_cidade(self, cidade):
        self.cidade = cidade
    def get_diretor(self):
        return self.diretor
    def set_diretor(self, diretor):
        self.diretor = diretor
    def get_nome_estado(self):
        if self.cidade == None:
            return "Escola sem cidade"
        else:
            return self.cidade.get_nome_estado()
    def get_descricao_escolaridade_diretor(self):
        if self.diretor == None:
            return "Escola sem diretor"
        else:
            return self.diretor.get_descricao_escolaridade()
    def get_nome_diretor(self):
        if self.diretor == None:
            return "Escola sem diretor"
        else:
            return self.diretor.get_nome()
