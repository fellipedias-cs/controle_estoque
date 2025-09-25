
estoque = []

while True:
    print("\n1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar quantidade")
    print("4 - Remover produto")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        qtd = int(input("Digite a quantidade: "))
        estoque.append([nome, qtd])
        print("Produto adicionado com sucesso!")

    elif opcao == "2":
        print("\n--- ESTOQUE ---")
        for i, p in enumerate(estoque):
            print(f"ID {i} | Nome {p[0]} | Qtd {p[1]}")
        print("----------------")

    elif opcao == "3":
        id_p = int(input("Digite o ID do produto: "))
        nova_qtd = int(input("Digite a nova quantidade: "))
        estoque[id_p][1] = nova_qtd
        print("Quantidade atualizada!")

    elif opcao == "4":
        id_p = int(input("Digite o ID do produto: "))
        estoque.pop(id_p)
        print("Produto removido!")

    elif opcao == "5":
        break

    else:
        print("Opção inválida.")