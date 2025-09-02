somaAltura=0
n_jogador = int(input("digite o números de jogaders:"))
for i in range(1,n_jogador+1):
    m_altura = float(input("digite a altura dos jogadores:"))
    somaAltura+=m_altura
    print("a média de altura dos jogadores é de:",somaAltura/n_jogador)