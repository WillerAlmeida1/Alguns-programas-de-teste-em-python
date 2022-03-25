popa = int(input('coloque aqui popa: '))
popb = int(input('coloque aqui popa: '))
tempo = 0
while(popb < popa):
    popa = (popa * 0.01) + popa
    popb = (popb * 0.0125) + popb
    tempo = tempo + 1

print('levou', tempo, 'para ultrapassar')
   


