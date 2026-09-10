import random

# Parte 1 - Lançamento único
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

soma = dado1 + dado2

print("=== LANÇAMENTO ÚNICO ===")
print()
print(f"🎲|Dado 1: {dado1}")
print(f"🎲|Dado 2: {dado2}")
print(f"Soma: {soma}")

# Parte 2 - 10 lançamentos
contador_soma7 = 0

print("\n==== 10 LANÇAMENTOS ====")

for i in range(1, 11):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2

    print(f"Lançamento {i}: {dado1} + {dado2} = {soma}")
    print("="*24)
    if soma == 7:
        contador_soma7 += 1
print("↓"*38)
print(f"\nA soma foi igual a 7 em {contador_soma7} lançamentos.")
print()
print("↑"*38)