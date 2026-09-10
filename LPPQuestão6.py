while True:
    try:
        numero1 = int(input("Digite o primeiro número inteiro: "))
        numero2 = int(input("Digite o segundo número inteiro: "))
        numero3 = int(input("Digite o terceiro número inteiro: "))

        if numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
            print("Erro: os três números devem ser distintos. Tente novamente.\n")
        else:
            break

    except ValueError:
        print("Erro: digite apenas números inteiros. Tente novamente.\n")



if numero1 > numero2:
    if numero1 > numero3:
        maior = numero1

        if numero2 > numero3:
            intermediario = numero2
            menor = numero3
        else:
            intermediario = numero3
            menor = numero2
    else:
        maior = numero3
        intermediario = numero1
        menor = numero2

else:
    if numero2 > numero3:
        maior = numero2

        if numero1 > numero3:
            intermediario = numero1
            menor = numero3
        else:
            intermediario = numero3
            menor = numero1
    else:
        maior = numero3
        intermediario = numero2
        menor = numero1


print("\nResultado:")
print("="*36)
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Número intermediário (mediana): {intermediario}")
print("="*36)
