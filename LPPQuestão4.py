

notas = []

for numero in range(1, 4):
      while True:
        nota = float(input(f"Digite a {numero}ª nota: "))

        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print("Erro: a nota deve estar entre 0 e 10. Digite novamente.")


media = sum(notas) / 3


if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"


print("\n===== RESULTADO ACADÊMICO =====")
print(f"Notas informadas: {notas[0]:.2f}, {notas[1]:.2f} e {notas[2]:.2f}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
print("============= FIM =============")