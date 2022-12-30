from random import shuffle
from tabulate import tabulate
import pyfiglet

num_shuffle = []
for i in range(1,100):
    num_shuffle.append(i)
    
shuffle(num_shuffle)
print(num_shuffle)