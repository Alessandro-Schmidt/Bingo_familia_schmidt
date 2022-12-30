from random import shuffle
from tabulate import tabulate
import pyfiglet

titulo_bingo = pyfiglet.figlet_format('Bingo\nFamília\nSchmidt', font="standard")
click_to_beggin = pyfiglet.figlet_format('Clique para iniciar', font="bubble")
print(titulo_bingo)

input(click_to_beggin)

numeros = []
for i in range(1,100):
    numeros.append(i)
   
shuffle(numeros) 
#for a in numeros:

print(numeros)