num_alunos = 10
medias = []

aprovados = 0
reprovados = 0

for i in range(num_alunos):
    print(f"Aluno {i+1}:")
    n1 = float(input("Digite a nota n1: "))
    n2 = float(input("Digite a nota n2: "))
    n3 = float(input("Digite a nota n3: "))
    media = (n1 + n2 + n3) / 3
    medias.append(media)
    if media >= 6:
        aprovados += 1
    else:
        reprovados += 1

maior_media = max(medias)
menor_media = min(medias)

print(f"\nMaior média: {maior_media:.2f}")
print(f"Menor média: {menor_media:.2f}")
print(f"Alunos aprovados: {aprovados}")
print(f"Alunos reprovados: {reprovados}")