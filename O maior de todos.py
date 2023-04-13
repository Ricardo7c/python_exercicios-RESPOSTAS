maior = 0
while True:
    num = int(input('Digite um numero inteiro: '))
    if num > maior:
        maior = num
    elif num == 0:
        break
print(f'O maior numero digitado foi: {maior}')

    
    