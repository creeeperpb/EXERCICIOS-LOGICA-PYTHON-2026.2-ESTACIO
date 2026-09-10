def calcular_media(notas):
    return sum(notas) / len(notas)


def ler_nota(numero):
    while True:
        try:
            nota = float(input(f"Nota {numero} (de 0 a 10): "))

            if 0 <= nota <= 10:
                return nota

            print("Nota inválida! Digite um valor entre 0 e 10.")

        except ValueError:
            print("Entrada inválida! Digite apenas números.")


def cadastrar_estudantes():
    turma = []

    for i in range(5):
        print(f"\n=== Cadastro do estudante {i + 1} ===")

        nome = input("Nome: ")

        notas = []

        for numero in range(1, 4):
            nota = ler_nota(numero)
            notas.append(nota)

        media = calcular_media(notas)

        estudante = {
            "nome": nome,
            "notas": notas,
            "media": media
        }

        turma.append(estudante)

    return turma


def exibir_resultados(turma):
    aprovados = 0
    recuperacao = 0
    reprovados = 0

    print("\n=== MÉDIAS DOS ESTUDANTES ===")

    for estudante in turma:
        print(
            f"{estudante['nome']} - "
            f"Notas: {estudante['notas']} - "
            f"Média: {estudante['media']:.2f}"
        )

        if estudante["media"] >= 7:
            aprovados += 1
        elif estudante["media"] >= 5:
            recuperacao += 1
        else:
            reprovados += 1

    maior_media = max(turma, key=lambda estudante: estudante["media"])
    menor_media = min(turma, key=lambda estudante: estudante["media"])

    print("\n=== ESTATÍSTICAS DA TURMA ===")
    print(
        f"Maior média: {maior_media['nome']} "
        f"({maior_media['media']:.2f})"
    )
    print(
        f"Menor média: {menor_media['nome']} "
        f"({menor_media['media']:.2f})"
    )
    print(f"Quantidade de aprovados: {aprovados}")
    print(f"Quantidade em recuperação: {recuperacao}")
    print(f"Quantidade de reprovados: {reprovados}")
    print("="*29)

# Programa principal
turma = cadastrar_estudantes()
exibir_resultados(turma)