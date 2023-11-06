from Cartas import Carta

user_input = int(input("Digite o número de cartas a serem produzidas: "))

cartas = Carta()
cartas.criarCartas(user_input)

print("Cartas desordenadas:", cartas._cartas)

cartas.insertionSort()
print("Cartas ordenadas:", cartas._cartas_atualizadas)

''' Demonstração

def insertionSort(fila):                    # na pratica: [3, 1] -> [3, 3] -> [1, 3]

    for i in range(1, len(fila)):           # um FOR inicia com valor de i inicial setado para 1
    
        chave = fila[i]                     # chave = fila[i]; se i for 1, entao chave = segundo valor, no caso de [3,1] é o 1
        
        j = i - 1                           # j é a posicao do valor anterior, no caso de i ser 1, entao j = 0

        while j >= 0 and chave < fila[j]:   # um while inicia se j for maior ou igual a zero (nao podendo ser negativo) e se, no nosso caso, o segundo valor é menor que o primeiro

            fila[j + 1] = fila[j]           # se o segundo valor for menor que o primeiro, novamente em [3,1], entao o valor atual 1, no caso i, será substituido pelo valor anterior 3 

            j -= 1                          # a posicao anterior decrementa-se, caso estejamos no primeiro elemento, entao ele encerra o loop com j = -1

        fila[j + 1] = chave                 # o elemento 0, ou (-1 + 1 = 0) no nosso caso, passa a ser o menor valor armazenado, chave = 1
'''
