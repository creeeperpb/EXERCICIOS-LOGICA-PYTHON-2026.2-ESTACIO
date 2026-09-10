def coletar_dados():

    nome = input("Digite seu nome completo: ")


    while True:
        try:
            idade = int(input("Digite sua idade (em anos): "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número inteiro válido para a idade.")


    while True:
        try:
            altura = float(input("Digite sua altura (em metros): "))
            if altura <= 0:
                print("A altura deve ser um valor positivo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um valor numérico válido para a altura.")


    cidade = input("Digite a cidade onde reside: ")


    print("\n" + "="*40)
    print("      CARTÃO DE IDENTIFICAÇÃO PESSOAL")
    print("="*40)
    print(f"Nome   : {nome}")
    print(f"Idade  : {idade} anos")
    print(f"Altura : {altura:.2f} m")
    print(f"Cidade : {cidade}")
    print("="*40)



coletar_dados()