print("média de vendas")

mes1 = int(input('Quais foram as suas vendas em janeiro?: '))
mes2 =int(input('Quais foram as suas vendas em fevereiro?: '))
mes3 = int(input('Quais foram as suas vendas em março?: '))
mes4 = int(input('Quais foram as suas vendas em abril?: '))

média = (mes1+mes2+mes3+mes4) / 4

print(média)

if média >= 5000:
    print("Você ganhou um abono salarial de 10%, Parabéns!!!")
else:
     print("Você infelizmente não bateu a meta de vendas.")



nome = input("Qual seu nome: ")
sobrenome = input("Qual seu sobrenome?: ")

print(nome + " " + sobrenome)