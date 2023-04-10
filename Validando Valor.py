import random

def checagem(texto):
    while True:
        num = input(texto)
        if num.isdigit():
            num = int(num)
            return num
        else:
            print('Valor invalido!')

num = checagem('Digite um numero: ')

print(f'{num} é um numero!')  