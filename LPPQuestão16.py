numeros = []

while True:
    print("\n==============================")
    print("   GERENCIAMENTO DE NÚMEROS")
    print("==============================")
    print("1 - Cadastrar número")
    print("2 - Listar números")
    print("3 - Exibir maior número")
    print("4 - Exibir menor número")
    print("5 - Calcular média")
    print("0 - Encerrar programa")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        numero = float(input("Digite um número: "))
        numeros.append(numero)
        print("Número cadastrado com sucesso!")

    elif opcao == 2:
        if numeros:
            print("Números cadastrados:")
            for n in numeros:
                print(n)
        else:
            print("Nenhum número cadastrado.")

    elif opcao == 3:
        if numeros:
            print("Maior número:", max(numeros))
        else:
            print("Nenhum número cadastrado.")

    elif opcao == 4:
        if numeros:
            print("Menor número:", min(numeros))
        else:
            print("Nenhum número cadastrado.")

    elif opcao == 5:
        if numeros:
            media = sum(numeros) / len(numeros)
            print("Média dos números:", media)
        else:
            print("Nenhum número cadastrado.")

    elif opcao == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
