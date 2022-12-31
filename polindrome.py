#Create a program that reads a phrase from the user and determines if it is a palindrome (i.e., it reads the same forwards and backwards).


#creamos una funcion

def es_palindromo(cadena):
  # Eliminamos los espacios y ponemos la cadena en minúsculas
  cadena = cadena.replace(" ", "").lower()

  # Invertimos la cadena
  cadena_invertida = cadena[::-1]

  # Comparamos la cadena original con la invertida
  if cadena == cadena_invertida:
    return True
  else:
    return False

print ("""---------------------------------------------
		Escriba un palindromo
---------------------------------------------""")



print (es_palindromo(input("")))

