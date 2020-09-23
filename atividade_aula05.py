class Pilha:
    def __init__(self):
        self.itens = []

    def isVazio(self):
        return self.itens == []

    def push(self, item):
        self.itens.insert(0,item)

    def pop(self):
        return self.itens.pop(0)

    def peek(self):
        return self.itens[0]

    def size(self):
        return len(self.itens)

s = Pilha()
s.push('Primeiro') #Adiciona o Primeiro item na Pilha
s.push('Segundo') #Adiciona o Segundo item na Pilha
s.push('Terceiro') #Adiciona o Terceiro item na Pilha
s.push('Quarto') #Adiciona o Quarto item na Pilha
s.push('Ultimo/Quinto') #Adiciona o Quinto/Ultimo item na Pilha
print(s.pop()) #Exibe o último item adicionado na Pilha em primeiro lugar
print(s.pop()) #Exibe o item seguinte
print(s.pop()) #Exibe o item seguinte
print(s.pop()) #Exibe o item seguinte
print(s.pop()) #Exibe o item seguinte