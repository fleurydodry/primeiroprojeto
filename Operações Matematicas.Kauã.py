print("--OPERAÇÕES MATEMATICAS--")
print("1- soma")
print("2- subtração")
print("3- multiplicação")
print("4- divisão")
print("5- par ou impar")
print("6- primo") 
print("7- fatorial")
opcao = input("Escolha uma das opções acima (digite o número). Para encerrar digite 'sair': ")
if opcao == "1":
    numero1 = int(input("digite o primeiro valor:  "))
    numero2 = int(input("digite o segundo valor:  "))
    print("o resultado da soma entre", numero1, "e", numero2, "é:", numero1 + numero2)
elif opcao == "2":
    numero1 = int(input("digite o primeiro valor:  "))
    numero2 = int(input("digite o segundo valor:  "))
    print("o resultado da subtração entre", numero1, "e", numero2, "é:", numero1 - numero2)
elif opcao == "3":
    numero1 = int(input("digite o primeiro valor:  "))
    numero2 = int(input("digite o segundo valor:  "))
    print("o resultado da multiplicação entre", numero1, "e", numero2, "é:", numero1 * numero2)
elif opcao == "4":
    numero1 = int(input("digite o primeiro valor:  "))
    numero2 = int(input("digite o segundo valor:  "))
    if numero2 != 0:
        print("o resultado da divisão entre", numero1, "e", numero2, "é:", numero1 / numero2)
    else:
        print("Não é possível dividir por zero.")
elif opcao == "5":
    numero = int(input("digite um número para saber se é par ou impar:  "))
    if numero % 2 == 0:
        print("o número", numero, "é par")
    else:
        print("o número", numero, "é impar")
elif opcao == "6":
    numero = int(input("digite um número para saber se é primo:  "))
    if numero > 1:
        for i in range(2, int(numero/2)+1):
            if (numero % i) == 0:
                print("o número", numero, "não é primo")
                break
        else:
            print("o número", numero, "é primo")
    else:
        print("o número", numero, "não é primo")
elif opcao == "7":
    numero = int(input("digite um número para saber o fatorial:  "))
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial = fatorial * i
    print("o fatorial de", numero, "é:", fatorial)
elif opcao.lower() == "sair":
    print("Encerrando o programa.")
else:
    print("Opção inválida.")



