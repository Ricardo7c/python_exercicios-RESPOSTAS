num = int(input("Digite um número para calcular seu fatorial: "))
if num < 0:
    print("Número invalido")
else:
    fatorial = 1
    print(f'{num}! = ',end='')
    for i in range(num, 0, -1):
        fatorial *= i
        if i == 1:
            print(f'{i} = ', end='')
        else:
            print(f'{i} x ', end='')

    print(fatorial)