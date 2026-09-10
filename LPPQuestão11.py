numeros = []

for i in range(10):
    while True:
        entrada = input(f"Digite o {i + 1}º número: ").strip()

        if entrada == "":
            print("Erro: nenhum valor foi informado. Tente novamente.")
            continue

        try:
            numero = int(entrada)
            numeros.append(numero)
            break
        except ValueError:
            print("Erro: digite apenas números inteiros.")

pares = []
impares = []

soma = 0
quantidade = 0
maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    soma += numero
    quantidade += 1

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

media = soma / quantidade
# Relatório
print("\n=== RELATÓRIO ANALÍTICO ===")
print("Números informados:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
print("Soma dos valores:", soma)
print(f"Média dos valores: {media:.2f}")
print("Maior valor:", maior)
print("Menor valor:", menor)