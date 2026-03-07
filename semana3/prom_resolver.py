# ALGORITMO
# 1. Solicitar al usuario el valor de la base del triangulo en metros 
# 2. Solicitar al usuario el valor de la altura del triamgulo en metros
# 3. calcular el area calculada 
# 4. mostrar el area calculada 
# 5. evaluar la siquiente 

# PSEUDOCODIGO
# INICIO 
# leer el primer valor de la base del triangulo en metros 
# leer el segundo valor de la altura del triangulo en metros 
# calcular la (base * altura)/2
# escribir si el area 
# escribir si area > 100
# escribir si elarea es igual a 100

base= int(input("ingresa el valor de la base:" ))
altura= int(input("ingresa el valor de la altura:"))

print((base*altura)/2)
print ("El area es mayor que 100?", base>altura)
