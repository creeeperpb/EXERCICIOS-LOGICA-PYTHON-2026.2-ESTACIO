while True:
    try:
        idade = int(input("Digite a idade da pessoa: "))

        if idade < 0:
            print("Erro: a idade não pode ser negativa. Tente novamente.")
        else:
            break

    except ValueError:
        print("Erro: informe a idade usando um número inteiro.")
if idade <= 3:
    classificacao = "Recém Nascido"
elif idade <= 12:
    classificacao = "Criança"
elif idade <= 17:
    classificacao = "Adolescente"
elif idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"
print("#"*36)
print(f"Classificação etária: {classificacao}")
print("#"*36)
