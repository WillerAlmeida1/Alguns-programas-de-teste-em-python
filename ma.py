print("Sua Média")

nota1 = input("Insira Sua Nota 1:")
nota1 = int(nota1)
nota2 = input("Insira Sua Nota 2:")
nota2 = int(nota2)
nota3 = input("Insira Sua Nota 3:")
nota3 = int(nota3)
nota4 = input("Insira Sua Nota 4:")
nota4 = int(nota4)

média = nota1 + nota2 + nota3 + nota4
resultado =  média / 4

print("Sua Média é:")
print(resultado)

if resultado > 10:
    print("Valor Inexistente")
elif resultado >= 7.5:
    print("Aprovado")
else:
	print("Reprovado")



 