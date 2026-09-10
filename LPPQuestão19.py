
frase = input("Digite uma frase: ").strip()


palavras = frase.split()


letra = input("Digite uma letra para contar as ocorrências: ").strip()


total_caracteres = len(frase)
quantidade_palavras = len(palavras)
primeira_palavra = palavras[0]
ultima_palavra = palavras[-1]


ocorrencias = frase.lower().count(letra.lower())


print("\n=== ANÁLISE DA FRASE ===")
print(f"Total de caracteres: {total_caracteres}")
print(f"Quantidade de palavras: {quantidade_palavras}")
print(f"Primeira palavra: {primeira_palavra}")
print(f"Última palavra: {ultima_palavra}")
print(f"Ocorrências da letra '{letra}': {ocorrencias}")
print(f"Em maiúsculas: {frase.upper()}")
print(f"Em minúsculas: {frase.lower()}")