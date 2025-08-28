### TUPLA - CONJUNTO - DICIONÁRIO
#tupla - necessario a ',' para ser uma tupla, caso não tenha, ela é uma str

# tupla_vazia = ()
# print(type(tupla_vazia))
# print(tupla_vazia)

# tupla = ("casa", 2, [1,2,3], tupla_vazia)
# tupla[2].append(6)
# print(tupla)

# tupla_nomes = ("joão", "Pedro", "Sara")
# print(type(tupla_nomes))
# lista_nomes = list(tupla_nomes) #transformanso a tupla em lista
# lista_nomes

#####    MATCH

#criando um menu com match (CRUD)

while True:
    opcao = input("Escola uma opção: \n "
                 "1 - Adicionar um livro \n"
                 "2 - Editar informaçoes \n"
                 "3 - Pesquisar um livro \n"
                 "4 - Deletar um livro \n"
                 "0 - Sair \n")
 
    match opcao:
        case "1":
            print("adicionando livro")
        case "2":
            print("editando livro")
        case "3":
            print("pesquisando livro")
        case "4":
            print("deletando livro")
        case "0":
            break
        case _:
            print("opcao invalida")