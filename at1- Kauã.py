soma_positivos = 0
quantidade_negativos = 0

for i in range(20):
    valor = int(input(f"Digite o {i+1}º valor inteiro: "))
    if valor > 0:
        soma_positivos += valor
    elif valor < 0:
        quantidade_negativos += 1

print("Soma dos números positivos:", soma_positivos)
print("Quantidade de valores negativos:", quantidade_negativos)