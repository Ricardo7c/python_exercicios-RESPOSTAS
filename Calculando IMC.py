peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso/altura**2
print(f'Seu IMC é: {imc:.2f}')
