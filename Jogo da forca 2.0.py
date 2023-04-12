import random
import os

def palavras():          # Escolhe e retorna uma das palavras na lista para iniciar o jogo
    frutas = ["BANANA", "LARANJA",
              "ABACAXI", "UVA", "MORANGO",
              "MANGA", "KIWI", "MELANCIA"]
    
    fruta = list(*random.choices(frutas))   
    return fruta                             

def verificartentativas(resp, tentativas):     # Recebe a lista de tentativas e a resposta do usuario,
    if resp not in tentativas:                 # Adiciona a resposta a lista se ele ainda não estiver lá
        tentativas.append(resp)          
    return sorted(tentativas)                  # Retorna a lista em ordem

def desmembrar(vitima):                        # Recebe a vitima e retira uma parte da vitima
    vitima = vitima.rstrip()[:-1]    
    return vitima                    

def morreu(vitima):                            # Verifica se a vitima já morreu
    if '0' not in vitima:            
        return True                  



palavra = palavras()                 # palavra recebe a palavra escolhida pela função
escondida = list('_'*len(palavra))   # escondida recebe _ multiplicados pela quantidade de letras na palavra
vitima = ' 0\n/|\ \n/ \ '            # vitima recebe o desenho
tentativas = []                      # A lista de tentativas é criada



while True:                          
    print(vitima)                              
    print('Letras que você já tentou: ', *tentativas)   
    

    if morreu(vitima) or palavra == escondida:              # Quebra o laço caso a vitima morra ou acerte a palavra
        break

    print('A palavra é: ', *escondida)
    resp = input('Digite uma letra: ').upper().strip()[0]
    tentativas = verificartentativas(resp, tentativas)
    

    #Esse é o core do jogo, onde um for compara a resposta do jogador com cada letra da palavra
    corte = True                        # Corte é iniciado como True
    for i, cada in enumerate(palavra):
        if resp == cada:                # Se a letra existir na palabra
            escondida[i] = cada         # Adiciona a letra em escondida no exato mesmo indice em que ela se encontra na palavra.
            corte = False                # Se a execução chegar até aqui, corte recebe None se não, ele permanece como True, como foi iniciado.

    if corte == True:                   # Verifica se corte é True ou False, se for false, a função desmembar não é chamada
        vitima = desmembrar(vitima)
    
    
    os.system("cls")                    # O metodo system do modulo os está sendo usado pra limpar a tela do console no fim de cada laço


print (f'A Palavra é: ', *palavra)
if morreu(vitima):                      # Ao fim do jogo quando o laço é quebrado, verifica se a vitima sobreviveu.
    print('Mas a vitima morreu!')
else:
    print('Parabéns, a vitima sobreviveu!')