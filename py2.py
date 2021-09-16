print("----CALCULADORA LAST VERSION----")

sair = False

while sair == False:

    num1 = input("digite o primeiro numero:")
    num1 = int(num1)
    operador = input("digite um operador(**+-/*):")
    num3 = input("digite o segundo numero:")
    num3 = int(num3)

    #soma
    if operador == "+":
        operação = num1 + num3
    #subtração
    if operador == "-":
        operação = num1 - num3
    #divisão
    if operador == "/":
        operação = num1 / num3
    #multiplicação
    if operador == "*":
        operação = num1 * num3
    #potenciação
    if operador == "**":
        operação = num1 ** num3
        
    print("resultado:")
    print(operação)

    test = input("deseja sair? s/n:")
    if test == "s":
        print("Obrigado por utilizar minha calculadora! :D")
        sair = True

        
