from random import sample
import time
l = int(input("Quantos jogos da Mega-Sena vossa majestade deseja? "))
print('='*30)
time.sleep(1.5)
for c in range(0, l):
    lista = sample(range(1, 60), 6)
    lista.sort()
    print(lista)
    time.sleep(1)
    lista.clear()