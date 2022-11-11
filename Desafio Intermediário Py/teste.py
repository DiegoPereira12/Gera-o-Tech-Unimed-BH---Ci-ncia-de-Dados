letra = input()
# letra = input("Digite uma letra de A a Z: ")  # Mais um vez, fica mais bonitinho mas o desafio não aceita e retorna erro
letra = letra.upper()                           # Garantindo que a entrada do usuário seja uma letra maiuscula pois a lista ASCII usada abaixo para comparação é maiuscula

import string

alfabeto = list(string.ascii_uppercase)         # Poderia ser usado também .ascii_lowcase mas a letra recebida precisaria ser lowcase tb

# print (alfabeto)                              # Remover primeiro comentário dessa linha se quiser ver o alfabeto impresso

# print("A posição da sua letra no alfabeto é: ") dá uma saida mais bonitinha visualmente de novo mas no desafio não aceita outra saida que não seja só o número
print(alfabeto.index(letra)+1)                  # Vale notar que a posição da letra na lista começa em 0, logo A = 0 portanto o +1 garante a resposta na posição correta do alfabeto