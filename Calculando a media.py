nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1+nota2+nota3)/3
print(f'Média: {media}')

if media >= 7:
    print('Situação: Aprovado!')
else:
    print('Situação: Reprovado!')
