# Algoritmo para somar todos os números inteiros de 1 a N

N = int(input("Digite um número inteiro N: "))
soma = 0

for i in range(1, N + 1):
    soma += i

print("A soma de todos os números de 1 a", N, "é:", soma)