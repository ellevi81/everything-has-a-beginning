#Crea un programa que callcue el promedio de una lista de 5 numeros que el usuario quiera

#lista vacia :D

numeros = []

#funcion de 5 vueltitas

for i in range (5):
	valor=int(input("Enter an integer: "))
	numeros.append(valor)
#Mostramos la lista

print ("The numbers are: " + str(numeros))

#calculamos el promedio

suma = sum(numeros)

print ("The sum is: " + str(suma))

print ("The average is:: " + str(suma/5))
