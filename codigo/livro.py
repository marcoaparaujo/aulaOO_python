class Livro:

    def __init__(self):
        self.titulo = ""
        self.autor = ""
        self.ano_publicacao = 0
        self.numero_paginas = 0
        self.genero = ""
        self.aberto = False
        self.pagina_atual = 0
        self.pagina_marcada = 0

    def get_numero_paginas(self):
        return self.numero_paginas

    def set_numero_paginas(self, numero_paginas):
        if numero_paginas > 0:
            self.numero_paginas = numero_paginas
    def get_pagina_atual(self):
        return self.pagina_atual

    def set_pagina_atual(self, pagina_atual):
        if pagina_atual >= 0:
            if pagina_atual <= self.numero_paginas:
                self.pagina_atual = pagina_atual

    def set_pagina_marcada(self, pagina_marcada):
        if pagina_marcada > 0 and pagina_marcada <= self.numero_paginas:
            self.pagina_marcada = pagina_marcada

    def get_pagina_marcada(self):
        return self.pagina_marcada
    def abrir(self):
        self.aberto = True
        self.pagina_atual = 1

    def fechar(self):
        self.aberto = False
        self.pagina_atual = 0

    def marcar_pagina(self, pagina_marcada):
        if pagina_marcada >= 0 and pagina_marcada <= self.numero_paginas:
            self.pagina_marcada = pagina_marcada

    def avancar_pagina(self):
        if self.aberto:
            if self.pagina_atual < self.numero_paginas:
                self.pagina_atual = self.pagina_atual + 1

    def retroceder_pagina(self):
        if self.aberto:
            if self.pagina_atual > 1:
                self.pagina_atual = self.pagina_atual - 1
