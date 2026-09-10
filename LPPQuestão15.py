# Lista para armazenar os dados das cidades
cidades = []

# Cadastro de 5 cidades
for i in range(5):
    print(f"\n=== Cadastro da cidade {i + 1} ===")

    nome = input("Nome da cidade: ")

    # Validação da sigla do estado
    while True:
        estado = input("Estado, com duas letras: ").strip().upper()

        if len(estado) == 2 and estado.isalpha():
            break

        print("Estado inválido! Digite uma sigla com duas letras.")

    # Validação da população
    while True:
        try:
            populacao = int(input("População estimada: "))

            if populacao >= 0:
                break

            print("A população não pode ser negativa.")

        except ValueError:
            print("Valor inválido! Digite um número inteiro.")

    # Criação do dicionário da cidade
    cidade = {
        "nome": nome,
        "estado": estado,
        "populacao": populacao
    }

    # Adiciona o dicionário à lista
    cidades.append(cidade)


# Encontrar as cidades com maior e menor população
maior_cidade = max(cidades, key=lambda cidade: cidade["populacao"])
menor_cidade = min(cidades, key=lambda cidade: cidade["populacao"])

# Calcular a população total
populacao_total = sum(cidade["populacao"] for cidade in cidades)

# Calcular a média populacional
media_populacional = populacao_total / len(cidades)


# Exibição dos resultados
print("\n=== RESULTADOS ===")

print("\nCidade com maior população:")
print(f"{maior_cidade['nome']} - {maior_cidade['estado']}")
print(f"População: {maior_cidade['populacao']} habitantes")

print("\nCidade com menor população:")
print(f"{menor_cidade['nome']} - {menor_cidade['estado']}")
print(f"População: {menor_cidade['populacao']} habitantes")

print(f"\nPopulação total: {populacao_total} habitantes")
print(f"Média populacional: {media_populacional:.2f} habitantes")
print("="*17)

# Exibição de todas as cidades cadastradas
print("\n=== CIDADES CADASTRADAS ===")

for cidade in cidades:
    print(f"\nNome: {cidade['nome']}")
    print(f"Estado: {cidade['estado']}")
    print(f"População estimada: {cidade['populacao']} habitantes")
    print("="*27)