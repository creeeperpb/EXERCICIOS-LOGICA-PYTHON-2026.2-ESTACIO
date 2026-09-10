temperaturas = []


for i in range(7):
    temp = float(input(f"Digite a temperatura do dia {i + 1}: "))
    temperaturas.append(temp)


maior = max(temperaturas)
menor = min(temperaturas)
media = sum(temperaturas) / len(temperaturas)


acima_media = 0
for temp in temperaturas:
    if temp > media:
        acima_media += 1


print("\n====> Temperaturas registradas:")
for temp in temperaturas:
    print(temp)

print("="*30)

print(f'\nMaior temperatura: {maior:.2f} °C')
print(f'Menor temperatura: {menor:.2f} °C')
print(f"Temperatura média: {media:.2f} °C")
print(f"Quantidade de dias acima da média: {acima_media}")