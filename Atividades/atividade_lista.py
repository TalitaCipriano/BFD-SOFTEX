#Atividade - Listas

#1111111111111111111111111111111111111111111111

#livros = ["Iracema", "Senhora", "O guarani"]
#print(livros)

#2222222222222222222222222222222222222222222222

#livros.pop(1)
#print(livros)

#3333333333333333333333333333333333333333333333

#livros2 = ("A viuvinha", "Cinco minutos")
#livros.extend(livros2) 
#print(livros)

#4444444444444444444444444444444444444444444444

#livros.insert(1,"Duna")
#print(livros)

#5555555555555555555555555555555555555555555555

#if "O silencio dos inocentes" in livros:
    #livros.remove("O silencio dos inocentes")
#else:
    #print("Livro não encontrado")

#6666666666666666666666666666666666666666666666

#numeros = [1,2,3,2,4,2,5]
#qtd = numeros.count(2)
#print(qtd)

#7777777777777777777777777777777777777777777777

#for lista in livros:
    #print(f"O livro {lista} é interessante")

#8888888888888888888888888888888888888888888888

#idades = [12, 18, 25, 14, 30]
#for lista in idades:
    #if lista >= 18:
        #print(lista)

#9999999999999999999999999999999999999999999999

#valores = [10, 20, 30, 40]
#total = sum(valores)
#print(total)

#1010101010101010101010101010101010101010101010



#nota1_aluno2 = float(input("Digite a nota 1 do aluno 2: "))
#nota2_aluno2 = float(input("Digite a nota 2 do aluno 2: "))
#nota3_aluno2 = float(input("Digite a nota 3 do aluno 2: "))

# notas_aluno1 = [nota1_aluno1, nota2_aluno1, nota3_aluno1]
# print(notas_aluno1)
#notas_aluno2 = [nota1_aluno2, nota2_aluno2, nota3_aluno2]

#notas = [notas_aluno1, notas_aluno2]
#git print(notas)

#media_aluno1 = (nota1_aluno1 + nota2_aluno1 + nota3_aluno1) / 3
#print("A media do aluno 1 é" (media_aluno1))


#11#11#11#11#11#11#11#11#11#11#11#11#11#11#11#11#11#11#11

#tabuleiro_vazio = [["[ ]" for coluna in range(8)] for linha in range(8)]
# for linha in tabuleiro_vazio:
#         print(linha)

# tabuleiro_vazio[0][0] = "tor"
# tabuleiro_vazio[0][-1] = "tor"
# tabuleiro_vazio[0][1] = "cav"
# tabuleiro_vazio[0][-2] = "cav"
# tabuleiro_vazio[0][2] = "bis"
# tabuleiro_vazio[0][-3] = "bis"
# tabuleiro_vazio[0][3] = "rei"
# tabuleiro_vazio[0][4] = "rai"
# tabuleiro_vazio[1] = ["pea"] * 8

# tabuleiro_vazio[-1][0] = "TOR"
# tabuleiro_vazio[-1][-1] = "TOR"
# tabuleiro_vazio[-1][1] = "CAV"
# tabuleiro_vazio[-1][-2] = "CAV"
# tabuleiro_vazio[-1][2] = "BIS"
# tabuleiro_vazio[-1][-3] = "BIS"
# tabuleiro_vazio[-1][3] = "REI"
# tabuleiro_vazio[-1][4] = "RAI"
# tabuleiro_vazio[-2] = ["PEA"] * 8

# for linha in tabuleiro_vazio:
#     print(linha)

# tabuleiro_vazio = [["[ ]" for coluna in range(8)] for linha in range(8)]
# linha_peoes = ["pea"] * 8
# lista_pecas = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]
# tabuleiro_vazio[0] = lista_pecas.copy()
# tabuleiro_vazio[1] = linha_peoes.copy()
# tabuleiro_vazio[-1] = lista_pecas.copy()
# tabuleiro_vazio[-2] = linha_peoes.copy()

# tabuleiro_vazio[5][5] = tabuleiro_vazio[6][5]
# tabuleiro_vazio[6][5] = "[ ]"
# for linha in tabuleiro_vazio:
#     print(linha)