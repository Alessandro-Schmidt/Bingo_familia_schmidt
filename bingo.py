from random import shuffle
from tabulate import tabulate
import pyfiglet

titulo_bingo = pyfiglet.figlet_format('Bingo\nFamília\nSchmidt', font="standard")
click_to_beggin = pyfiglet.figlet_format('Clique para iniciar', font="bubble")
print(titulo_bingo)
input(click_to_beggin)
print('\033[0;30;41mDigite "bingo" para encerrar\033[m')

numeros = []
for i in range(1,100):
    numeros.append(i)
   
shuffle(numeros) 

parada = ''
i = 0
mostrados = []

while (i<len(numeros)) and parada!='bingo':
    mostrados.append(numeros[i])
    num = pyfiglet.figlet_format(str(numeros[i]), font="standard")
    print(num)
    print('Números já sorteados: '+ str(mostrados))
    i+=1
    parada = str(input('\033[0;30;42mAperte enter ou digite "bingo"\033[m'))

vencedor = str(input())
print(numeros)