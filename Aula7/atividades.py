#Atividade - Listas

#1111111111111111111111111111111111111111111111

livros = ["Iracema", "Senhora", "O guarani"]
print(livros)

#2222222222222222222222222222222222222222222222

livros.pop(1)
print(livros)

#3333333333333333333333333333333333333333333333

livros2 = ("A viuvinha", "Cinco minutos")
livros.extend(livros2) 
print(livros)

#4444444444444444444444444444444444444444444444

livros.insert(1,"Duna")
print(livros)

#5555555555555555555555555555555555555555555555

if "O silencio dos inocentes" in livros:
    livros.remove("O silencio dos inocentes")
else:
    print("Livro não encontrado")

#6666666666666666666666666666666666666666666666

numeros = [1,2,3,2,4,2,5]
qtd = numeros.count(2)
print(qtd)

#7777777777777777777777777777777777777777777777

for lista in livros:
    print(f"O livro {lista} é interessante")

#8888888888888888888888888888888888888888888888

idades = [12, 18, 25, 14, 30]
for lista in idades:
    if lista >= 18:
        print(lista)

#9999999999999999999999999999999999999999999999

valores = [10, 20, 30, 40]
total = sum(valores)
print(total)

#1010101010101010101010101010101010101010101010

nota1_aluno1 = float(input("Digite a nota 1 do aluno 1: "))
nota2_aluno1 = float(input("Digite a nota 2 do aluno 1: "))
nota3_aluno1 = float(input("Digite a nota 3 do aluno 1: "))

nota1_aluno2 = float(input("Digite a nota 1 do aluno 2: "))
nota2_aluno2 = float(input("Digite a nota 2 do aluno 2: "))
nota3_aluno2 = float(input("Digite a nota 3 do aluno 2: "))

notas_aluno1 = [nota1_aluno1, nota2_aluno1, nota3_aluno1]
print(notas_aluno1)
notas_aluno2 = [nota1_aluno2, nota2_aluno2, nota3_aluno2]
print(notas_aluno2)

notas = [notas_aluno1, notas_aluno2]
print(notas)

media_aluno1 = (nota1_aluno1 + nota2_aluno1 + nota3_aluno1) / 3
print(media_aluno1)

media_aluno2 = (nota1_aluno2 + nota2_aluno2 + nota3_aluno2) / 3
print(media_aluno2)

#11#11#11#11#11#11#11#11#11#11#11#11#11#11#11#11#11#11#11

