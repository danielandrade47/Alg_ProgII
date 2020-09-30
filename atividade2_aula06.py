nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

nota_final = (nota1 + nota2) / 2

aluno = {
    "Nome " : nome,
    "Nota 1 " : nota1,
    "Nota 2 " : nota2,
    "Nota final " : nota_final
}

print(aluno)