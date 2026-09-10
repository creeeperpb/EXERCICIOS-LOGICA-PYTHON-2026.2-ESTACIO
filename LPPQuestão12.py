produtos = []


for i in range(5):
    print(f"\nCadastro do produto {i + 1}")

    nome = input("Nome do produto: ")
    preco = float(input("Preço unitário: "))
    quantidade = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)


print("\n=== PRODUTOS CADASTRADOS ===")
for produto in produtos:
    print(f"Nome: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Quantidade: {produto['quantidade']}")
    print("-" * 30)


valor_total = 0
for produto in produtos:
    valor_total += produto["preco"] * produto["quantidade"]

print(f"\nValor total do estoque: R$ {valor_total:.2f}")


produto_mais_caro = produtos[0]

for produto in produtos:
    if produto["preco"] > produto_mais_caro["preco"]:
        produto_mais_caro = produto

print("\n=== PRODUTO COM MAIOR PREÇO UNITÁRIO ===")
print(f"Nome: {produto_mais_caro['nome']}")
print(f"Preço: R$ {produto_mais_caro['preco']:.2f}")