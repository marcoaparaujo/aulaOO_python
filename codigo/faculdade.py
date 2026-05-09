class Aluno:
    def __init__(self):
        self.nome = ""
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome

class Curso:
    def __init__(self):
        self.alunos = []
    def matricular(self, aluno):
        self.alunos.append(aluno)
    def verificar_matricula(self, aluno):
        return aluno in self.alunos
    def desmatricular(self, aluno):
        self.alunos.remove(aluno)
    def get_alunos(self):
        return self.alunos
    def get_nomes_alunos(self):
        nomes = []
        for aluno in self.alunos:
            nomes.append(aluno.get_nome())
        return nomes
    def get_quantidade_alunos_curso(self):
        return len(self.alunos)




