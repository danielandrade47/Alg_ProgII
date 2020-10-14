class AlunoGraduacao(Aluno):
    def __init__(self, semestre):
        self.semestre = semestre

    def imprimir(self):
        print("Semestre: ", self.semestre)