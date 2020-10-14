class AluEnsMedio(Aluno):
    def __init__(self, ano):
        self.ano = ano

    def imprimir(self):
        print("Ano: ", self.ano)