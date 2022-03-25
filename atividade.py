frase = 'um dois tres quatro'

frase_separada = frase.split()[0:4] 
#frase_capitalizada = str.capitalize(frase_separada).capitalize()


frase = "um dois tres quatro"
print('Old String: ', frase)
print('Capitalized String:', frase.capitalize())
frase = frase.split(frase[0:4].capitalize)
print(frase)

print(frase_separada)
#frase_separada1 = frase.split()[0].capitalize()
#frase_separada2 = frase.split()[1].capitalize()
#frase_separada3 = frase.split()[2].capitalize()
#frase_separada4 = frase.split()[3].capitalize()
#nova_frase = frase_separada1 +' '+ frase_separada2 +' '+ frase_separada3 +' '+ frase_separada4

#print(nova_frase)
#print(frase_separada1 +' '+frase_separada2+' '+frase_separada3+' '+frase_separada4)