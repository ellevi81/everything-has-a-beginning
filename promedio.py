#Crea un programa que callcue el promedio de una lista de 5 numeros que el usuario quiera

#lista vacia :D

numeros = []

#funcion de 5 vueltitas

for i in range (5):
	valor=int(input("Ingrese un numero entero: "))
	numeros.append(valor)
#Mostramos la lista

print ("Los numeros son: " + str(numeros))

#calculamos el promedio

suma = sum(numeros)

print ("La suma es: " + str(suma))

print ("El promedio es: " + str(suma/5))
