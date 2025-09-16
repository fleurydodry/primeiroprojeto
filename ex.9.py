num = int(input("DIgite um numero: "))
i = 2 
eh_primo = True

while i < num:
    if num % 1 == 0:
        eh_primo = false 
        break
    i += 1

if num > 1 and eh_primo:
    print(num, "é primo")
else:
    print(num, "nao é primo")