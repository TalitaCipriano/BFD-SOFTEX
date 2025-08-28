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

        
    