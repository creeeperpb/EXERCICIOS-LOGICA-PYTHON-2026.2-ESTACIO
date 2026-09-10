estudantes = []


# Funções auxiliares

def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def definir_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


# Cadastrar estudante

def cadastrar_estudante():
    print("\n=== CADASTRAR ESTUDANTE ===")

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    media = calcular_media(nota1, nota2, nota3)
    situacao = definir_situacao(media)

    estudante = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "notas": [nota1, nota2, nota3],
        "media": round(media, 2),
        "situacao": situacao
    }

    estudantes.append(estudante)

    print("Estudante cadastrado com sucesso!")



def listar_estudantes():
    print("\n=== LISTA DE ESTUDANTES ===")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    for i, aluno in enumerate(estudantes, start=1):
        print(f"\nEstudante {i}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")
        print(f"Notas: {aluno['notas']}")
        print(f"Média: {aluno['media']}")
        print(f"Situação: {aluno['situacao']}")



# Consultar estudante

def consultar_estudante():
    print("\n=== CONSULTAR ESTUDANTE ===")

    nome = input("Digite o nome do estudante: ")

    for aluno in estudantes:
        if aluno["nome"].lower() == nome.lower():
            print("\nDados encontrados:")
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Curso: {aluno['curso']}")
            print(f"Notas: {aluno['notas']}")
            print(f"Média: {aluno['media']}")
            print(f"Situação: {aluno['situacao']}")
            return

    print("Estudante não encontrado.")



# Alterar dados

def alterar_dados():
    print("\n=== ALTERAR DADOS ===")

    nome = input("Nome do estudante: ")

    for aluno in estudantes:
        if aluno["nome"].lower() == nome.lower():

            aluno["nome"] = input(
                f"Novo nome ({aluno['nome']}): "
            ) or aluno["nome"]

            idade = input(
                f"Nova idade ({aluno['idade']}): "
            )

            if idade:
                aluno["idade"] = int(idade)

            aluno["curso"] = input(
                f"Novo curso ({aluno['curso']}): "
            ) or aluno["curso"]

            print("Digite as novas notas:")

            n1 = float(input("Nota 1: "))
            n2 = float(input("Nota 2: "))
            n3 = float(input("Nota 3: "))

            aluno["notas"] = [n1, n2, n3]

            media = calcular_media(n1, n2, n3)

            aluno["media"] = round(media, 2)
            aluno["situacao"] = definir_situacao(media)

            print("Dados atualizados com sucesso!")
            return

    print("Estudante não encontrado.")



# Remover estudante

def remover_estudante():
    print("\n=== REMOVER ESTUDANTE ===")

    nome = input("Nome do estudante: ")

    for aluno in estudantes:
        if aluno["nome"].lower() == nome.lower():

            confirmar = input(
                f"Confirma exclusão de {aluno['nome']}? (s/n): "
            )

            if confirmar.lower() == "s":
                estudantes.remove(aluno)
                print("Estudante removido com sucesso!")
            else:
                print("Operação cancelada.")

            return

    print("Estudante não encontrado.")



# Relatório da turma

def gerar_relatorio():
    print("\n=== RELATÓRIO DA TURMA ===")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    medias = [aluno["media"] for aluno in estudantes]

    maior_media = max(medias)
    menor_media = min(medias)
    media_geral = sum(medias) / len(medias)

    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for aluno in estudantes:
        if aluno["situacao"] == "Aprovado":
            aprovados += 1
        elif aluno["situacao"] == "Recuperação":
            recuperacao += 1
        else:
            reprovados += 1

    print(f"Total de estudantes: {len(estudantes)}")
    print(f"Maior média: {maior_media:.2f}")
    print(f"Menor média: {menor_media:.2f}")
    print(f"Média geral da turma: {media_geral:.2f}")
    print(f"Aprovados: {aprovados}")
    print(f"Recuperação: {recuperacao}")
    print(f"Reprovados: {reprovados}")



# Menu principal

while True:

    print("\n" + "=" * 45)
    print("             SISTEMA ACADÊMICO")
    print("=" * 45)

    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("3 - Consultar estudante")
    print("4 - Alterar dados")
    print("5 - Remover estudante")
    print("6 - Gerar relatório da turma")
    print("0 - Encerrar sistema")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_estudante()

    elif opcao == "2":
        listar_estudantes()

    elif opcao == "3":
        consultar_estudante()

    elif opcao == "4":
        alterar_dados()

    elif opcao == "5":
        remover_estudante()

    elif opcao == "6":
        gerar_relatorio()

    elif opcao == "0":
        print("Sistema encerrado. Tenha uma ótima viagem no caminho!")
        print("|||| Sistema criado por Carlos Eduardo. ||||")
        break

    else:
        print("Opção inválida!")
