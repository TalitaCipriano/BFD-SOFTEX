Agora vocês vão botar a mão na massa de fato no CRUD.

A ideia é usar tudo que aprendemos até agora para construir essa ferramenta. O objetivo dessa segunda parte é:

Criar o menu da aplicação
Criar função para adicionar itens
Criar função para pesquisar itens
Criar função para editar itens
Criar função para remover itens
Tentem criar arquivos separados para cada função, facilitando a organização do código e evitando incompatibilidades ao trabalhar em equipe.

Ao fim da atividade, todos os membros dos grupos, devem enviar aqui o link do repositório para registrar que a atividade foi feita.

#ADICIONAR ITENS

from database import cursos
def alterar_curso(cursos, id_curso, novo_nome=None, nova_descricao=None, nova_carga=None):
    for curso in cursos:
        if curso["id"] == id_curso:
            if novo_nome is not None:
                curso["nome"] = novo_nome
            if nova_descricao is not None:
                curso["descrição"] = nova_descricao
            if nova_carga is not None:
                curso["carga"] = nova_carga
            print(f"Curso com ID {id_curso} alterado com sucesso!")
            return
    print(f"Curso com ID {id_curso} não encontrado.")


#REMOVER ITENS

from database import cursos

def remover_curso(cursos, id_curso):
    for i, curso in enumerate(cursos):
        if curso["id"] == id_curso:
            curso_removido = cursos.pop(i)
            print(f"Curso '{curso_removido['nome']}' (ID {id_curso}) removido com sucesso!")
            return
    print(f"Curso com ID {id_curso} não encontrado.")

#PESQUISAR ITENS

def pesquisar_curso(cursos, termo_busca):
    resultados = []

    for curso in cursos:
        if termo_busca.lower() in curso["nome"].lower():
            resultados.append(curso)

    if resultados:
        print(f"\nResultados da pesquisa por '{termo_busca}':")
        print("-" * 50) #apenas estético, é uma linha separadora, entre um curso e outro
        for curso in resultados:
            print(f"ID: {curso['id']}")
            print(f"Nome: {curso['nome']}")
            print(f"Descrição: {curso['descrição']}")
            print(f"Carga Horária: {curso['carga']}h")
            print("-" * 50) 
    else:
        print(f"Nenhum curso encontrado com o termo '{termo_busca}'.")

#FUNÇÃO MENU

def menu():
    while True:
        print("\n====== MENU DE CURSOS ======")
        print("[1] Listar cursos")
        print("[2] Adicionar curso")
        print("[3] Remover curso")
        print("[4] Pesquisar curso")
        print("[0] Sair")
        print("============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_cursos(cursos)

        elif opcao == "2":
            nome = input("Nome do curso: ")
            descricao = input("Descrição do curso: ")
            carga = int(input("Carga horária (horas): "))
            adicionar_curso(cursos, nome, descricao, carga)

        elif opcao == "3":
            try:
                id_remover = int(input("ID do curso a remover: "))
                remover_curso(cursos, id_remover)
            except ValueError:
                print("Digite um ID válido.")

        elif opcao == "4":
            termo = input("Digite o nome ou parte do nome do curso: ")
            pesquisar_curso(cursos, termo)

        elif opcao == "0":
            print("\n👋 Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione ENTER para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')  # limpa a tela

#INICIAR MENU

if __name__ == "__main__":
    menu()

#FUNÇÃO EDITAR

def editar_curso(cursos, id_curso, novo_nome=None, nova_descricao=None, nova_carga=None):
    for curso in cursos:
        if curso["id"] == id_curso:
            if novo_nome is not None:
                curso["nome"] = novo_nome
            if nova_descricao is not None:
                curso["descrição"] = nova_descricao
            if nova_carga is not None:
                curso["carga"] = nova_carga
            print(f"Curso com ID {id_curso} editado com sucesso!")
            return
    print(f"Curso com ID {id_curso} não encontrado.")