###1

# cadastro = {}
# print(type(cadastro))
# print(cadastro)

# cadastro = {
#     "nome": "Lucas",
#     "idade": 25,
#     "email": "lucas@email.com",
# }
# print(cadastro)

###2

# cliente = {
#     "nome": "Amanda",
#     "idade": 31,
# }

# telefone = cliente.get("telefone", "não informado")
# print(telefone)

###3

# livro = {
#     "título": "1984",
#     "autor": "George Orwell",
#     "ano": 1949,
# }

# for chave in livro:
#     print(chave)

###4

# livro["disponivel"] = "True"
# print(livro)

###5

#livro.pop("ano")
#print(livro)

###6

# compras = {
#     "leite": 5.50,
#     "arroz": 4.30,
#     "sal": 2.30,
# }

# total = sum(compras.values())
# print(total)

###7

# frutas = {
#     "maça": 3,
#     "banana": 5,
#     "larnaja": 2,
# }

# for fruta, quantidade in frutas.items():
#     if quantidade > 2:
#         print(fruta)

###8

usuario = {
    "login": "joaosilva",
}

senha = usuario.get("senha", "nao informado")
print(senha)

usuario["senha"] = "123456"
print(usuario)

###9

