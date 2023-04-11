palavra = list('PYTHON')
escondida = list('_'*len(palavra))

while palavra != escondida:
    print('A palavra é: ', *escondida)
    resp = input('Digite uma letra: ').upper().strip()[0]
    for i, cada in enumerate(palavra):
        if resp == cada:
            escondida[i] = cada
    
print('Parabéns, você conseguiu!')
print('A palavra é: ', *escondida)