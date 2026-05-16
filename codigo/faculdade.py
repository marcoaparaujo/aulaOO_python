class Pessoa:
    def __init__(self):
        self.nome = ""
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome

class Disciplina:
    def __init__(self):
        self.nome = ""
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome

class Turma:
    def __init__(self):
        self.disciplina = None
        self.professor = None
        self.alunos = []
    def set_disciplina(self, disciplina):
        self.disciplina = disciplina
    def get_disciplina(self):
        return self.disciplina
    def get_professor(self):
        return self.professor
    def set_professor(self, professor):
        self.professor = professor
    def get_alunos(self):
        return self.alunos
    def matricular(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
    def desmatricular(self, aluno):
        self.alunos.remove(aluno)
    def get_nome_professor(self):
        if self.professor == None:
            return "Turma sem professor"
        else:
            return self.professor.get_nome()
    def get_nomes_alunos(self):
        nomes = []
        for aluno in self.alunos:
            nomes.append(aluno.get_nome())
        return nomes
    def get_nome_disciplina(self):
        if self.disciplina == None:
            return "Turma sem disciplina"
        else:
            return self.disciplina.get_nome()
    def verificar_aluno(self, aluno):
        return aluno in self.alunos

class Professor(Pessoa):
    def __init__(self):
        super().__init__()

class Aluno(Pessoa):
    def __init__(self):
        super().__init__()

class Curso:
    def __init__(self):
        self.alunos = []
        self.turmas = []
    def get_alunos(self):
        return self.alunos
    def get_turmas(self):
        return self.turmas
    def matricular(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
    def criar_turma(self, turma):
        if turma not in self.turmas:
            self.turmas.append(turma)
    def excluir_turma(self, turma):
        self.turmas.remove(turma)
    def verificar_matricula(self, aluno):
        return aluno in self.alunos
    def verificar_nome_aluno(self, nome):
        i = 0
        achou = False
        while not achou and i < len(self.alunos):
            if self.alunos[i].get_nome() == nome:
                achou = True
            i += 1
        return achou
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
    def get_nomes_professores(self):
        nomes = []
        for turma in self.turmas:
            if turma.get_professor() != None:
                nomes.append(turma.get_nome_professor())
        return nomes
    def get_nomes_alunos_turmas(self):
        nomes = []
        for turma in self.turmas:
            for nome in turma.get_nomes_alunos():
                if nome not in nomes:
                    nomes.append(nome)
        return nomes
    def get_nomes_disciplinas_turmas(self):
        nomes = []
        for turma in self.turmas:
            if turma.get_disciplina() != None:
                nomes.append(turma.get_nome_disciplina())
        return nomes
    def verificar_turma(self, turma):
        return turma in self.turmas


