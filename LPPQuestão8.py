soma = 0
positivos = 0
negativos = 0
pares = 0
impares = 0

for posicao in range(1, 11):
    while True:
        try:
            numero = int(input(f"Digite o {posicao}º número inteiro: "))
            break
        except ValueError:
            print("Entrada inválida. Digite apenas um número inteiro.")

    soma += numero

    # Verifica se o número é positivo ou negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Calcula a média dos 10 valores
media = soma / 10

print("\n===== RELATÓRIO ESTATÍSTICO =====")
print(f"Soma de todos os números: {soma}")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Média aritmética: {media:.2f}")
print("="*32)