# ATIVIDADES DICIONÁRIO

#1111111111111111111111111111111111111

# aluno = {
#     "nome": "Talita",
#     "idade": 36,
#     "nota": 8.75,
# }

#2222222222222222222222222222222222222

# produto = { "nome": "Caneta", "preço": 2.5, "estoque": 100}
# print(produto["nome"])
# print(produto["estoque"])

#3333333333333333333333333333333333333

# pessoa = {"nome": "Carlos", "idade": 30}
# pessoa["Cidade"] = "São Paulo"
# print(pessoa)

#4444444444444444444444444444444444444

# carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
# carro.pop("ano")

#5555555555555555555555555555555555555

# contato = {"nome": "Ana", "email": "ana@email.com"}

# if "telefone" in contato:
#     print("Telefone cadastrado")
# else:
#     print("Telefone não cadastrado")

#6666666666666666666666666666666666666

# palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

# contagem = {}
# for item in palavras:
#     if item in contagem:
#         contagem[item] += 1
#     else:
#         contagem[item] = 1

# print(contagem)

#77777777777777777777777777777777777777

# dict = {"a": 1, "b": 2, "c": 3}

# dict2 = dict.copy

# dict_invertido = {valor: chave for chave, valor in dict.items()}
 
# dict2 = dict_invertido

# print(dict)
# print(dict2)

#888888888888888888888888888888888888888

# nota1aluno1 = 8.5
# nota2aluno1 = 9
# nota3aluno1 = 9

# nota1aluno2 = 7.75
# nota2aluno2 = 10
# nota3aluno2 = 8.5

# nota1aluno3 = 8.5
# nota2aluno3 = 8.5
# nota3aluno3 = 9

# notasaluno1 = [[nota1aluno1], [nota2aluno1], [nota3aluno1]]
# notasaluno2 = [[nota1aluno2], [nota2aluno2], [nota3aluno2]]
# notasaluno3 = [[nota1aluno3], [nota2aluno3], [nota3aluno3]]

# notas = {
#     "Guilherme": notasaluno1,
#     "Thiago": notasaluno2,
#     "Laís": notasaluno3,
# }
# print(notas)

# soma1 = nota1aluno1 + nota2aluno1 + nota3aluno1
# mediaaluno1 = soma1 / 3

# soma2 = nota1aluno2 + nota2aluno2 + nota3aluno2
# mediaaluno2 = soma2 / 3

# soma3 = nota1aluno3 + nota2aluno3 + nota3aluno3
# mediaaluno3 = soma3 / 3

# print(mediaaluno1)
# print(mediaaluno2)
# print(mediaaluno3)

#99999999999999999999999999999999999999999999999

# ESSE EU ENTENDI EM PARTE COMO FAZER, UTILIZEI A BOA E VELHA INTERNET PARA FINALIZAR

# dictA = {"camisa": "M","short": 40,"calça": 42,}
# dictB = {"sapato": 39, "casaco": "G", "calça": 40,}

# def mesclar_dicionarios(dictA, dictB):
#     resultado = dictA.copy()   
#     resultado.update(dictB)    # Atualiza com os pares do segundo, deixando como correto o ultimo valor da chave repetida
#     return resultado

# dictAB = mesclar_dicionarios(dictA, dictB)
# print(dictAB)

#10101010101010101010101010101010101010101010101010

# ESSE EU NÃO ENTENDI COMO FAZER, UTILIZEI A BOA E VELHA INTERNET

# pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

# def mostrar_pontuacoes_ordenadas(dicionario):
#     itens_ordenados = sorted(dicionario.items(), key=lambda item: item[1], reverse=True)
#     for nome, pontuacao in itens_ordenados:
#         print(f"{nome}: {pontuacao}")

# pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

# mostrar_pontuacoes_ordenadas(pontuacoes)