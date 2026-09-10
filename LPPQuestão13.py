# Lista para armazenar os contatos
agenda = []

# Cadastro de 5 contatos
for i in range(5):
    print(f"\nCadastro do contato {i + 1}")

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    agenda.append(contato)

# Consulta de contato
nome_consulta = input("\nDigite o nome do contato que deseja consultar: ")

encontrado = False

for contato in agenda:
    if contato["nome"].lower() == nome_consulta.lower():
        print("\n=== CONTATO ENCONTRADO ===")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"E-mail: {contato['email']}")
        encontrado = True
        break

if not encontrado:
    print("Contato não encontrado.")