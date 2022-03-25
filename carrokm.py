
km_anterior = float (input("Coloque aqui a quilometragem anterior: "))
km_atual = float (input("Coloque aqui a sua quilometragem atual: "))
gasto_litro = float (input("Qual a quantidade de combustivel gasto para percorrer esse percurso: "))

km_atual = km_atual - km_anterior
km_percorrida = km_atual
gasto = km_atual / gasto_litro

print("Você está a "+ str(km_percorrida) +"km de distância do ponto anterior e o gasto foi de: " + str(gasto) + "km/l")

#print("Você está a", km_percorrida,"km de distância do ponto anterior e o gasto foi de: ", gasto,"km/l")

#dist = float (input("Coloque aqui a distância percorrida: "))
#gas = float (input("Coloque aqui o gasto em litros: "))

#gasto = dist / gas

#print(gasto)