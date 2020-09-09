class No:
    def __init__(self, valor):
        self.dado = valor
        self.proximo = None
        self.anterior = None
        self.pulo_indice = None
    
    def __str__(self):
        if self.proximo is None and self.anterior is None:
            return f"Anterior: {self.anterior} \n Nó: {self.dado} \n Próximo: {self.proximo}"
        elif self.proximo is None:
            return f"Anterior: {self.anterior.dado} \n Nó: {self.dado} \n Próximo: {self.proximo}"
        elif self.anterior is None:
            return f"Anterior: {self.anterior} \n Nó: {self.dado} \n Próximo: {self.proximo}" 
        else:
            return f"Anterior: {self.anterior.dado} \n Nó: {self.dado} \n Próximo: {self.proximo.dado}" 