try:
    numero = int(input("Digite um número inteiro: "))

    print(f"\nTabuada de {numero}:")

    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")

except ValueError:
    print("Erro: digite apenas um número inteiro.")