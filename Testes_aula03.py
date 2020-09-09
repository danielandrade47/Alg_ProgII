from atividade_aula03 import No
from random import randint

no1 = No(randint(0, 100))
no2 = No(randint(0, 100))
no3 = No(randint(0, 100))
no4 = No(randint(0, 100))
no5 = No(randint(0, 100))

no1.proximo = no2

no2.anterior = no1
no2.proximo = no3

no3.anterior = no2
no3.proximo = no4

no4.anterior = no3
no4.proximo = no5

print(no1)
print(no2)
print(no3)
print(no4)
print(no5)