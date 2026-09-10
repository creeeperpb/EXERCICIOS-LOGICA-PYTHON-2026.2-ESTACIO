import math


numero = float(input("Digite um número real: "))


if numero >= 0:
    print(f"Raiz quadrada: {math.sqrt(numero)}")
else:
    print("Raiz quadrada: não existe nos números reais.")


print(f"Valor absoluto: {math.fabs(numero)}")


print(f"Arredondamento para cima (teto): {math.ceil(numero)}")


print(f"Arredondamento para baixo (piso): {math.floor(numero)}")


if numero >= 0 and numero.is_integer():
    print(f"Fatorial: {math.factorial(int(numero))}")
else:
    print("Fatorial: disponível apenas para números inteiros e não negativos.")
