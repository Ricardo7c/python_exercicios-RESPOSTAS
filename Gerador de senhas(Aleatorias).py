import random

tamanho = int(input('Digite o tamanho da senha: '))

# Adiciona cada grupo de caractere a uma variavel
maiuscula = 'ABCDEFGHIJKLMNOPQRSTWUVXYZ'       
menuscula = 'abcdefghijklmnopkrstwuvxyz'     
numero = '0123456789'                        
simbolo =  '!"#$%&*+?@_'

# Como as os dois grupos de letras juntos somam um numero muito superior de caracteres
# extraio apenas metade da mistura dos dois pra usar no comando final.
letras = ''.join(random.choices((maiuscula+menuscula), k=26)) 

# junta todos os caracteres
todos = letras + numero + simbolo

# Escolhe aleatoriamente o numero de caracteres digitado para formar a senha
senha = ''.join(random.choices(todos, k=tamanho))

print(senha)