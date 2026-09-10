num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\n===== RESULTADOS =====")
print(f"Adição (+): {num1 + num2}")
print(f"Subtração (-): {num1 - num2}")
print(f"Multiplicação (×): {num1 * num2}")
print(f"Potenciação (**): {num1 ** num2}")


if num2 != 0:
    print(f"Divisão (/): {num1 / num2}")
    print(f"Divisão inteira (//): {num1 // num2}")
    print(f"Resto da divisão (%): {num1 % num2}")
else:
    print("Divisão por zero não permitida para as operações de divisão.")
print("="*21)