

'''Issues

-Recuerda el uso de gerarquia de parentesis , corchetes y se me olvido el nonbre de los que parecen casita, hahahaha...

'''
import random


# 1 Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

var = [0,-2,-10,-45,19,19]
var_pass = len(var)
print(type(var_pass))
print(type(var))
print(var)
for n in range (0,var_pass):
    print(var[n])
    if(var[n]>0):
        print(f'el valor {var[n]} es mayor que cero')
    elif(var[n]<0):
        print(f'el valor {var[n]} es menor que cero')

#  2 Crear dos variables y un condicional que informe si son del mismo tipo de dato
var2_1 = random.randint(0,20)
var2_2 = random.randbytes

print(type(var2_1))
print(var2_2)
if(type(var2_1) == type(var2_2)):
    print(f'el valor {var2_2} y {var2_1} son del mismo tipo de dato')
else:
    print('No jalo compa')

# 3 Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for n in range(0,21):
    if(n % 2 == 0 and n != 0):
        print(f'el numero {n} es par')
    elif(n == 0):
        print(f'el numero 0, no entra es un caso especial, ya que no es divisible, es una buena investigacion, dado que si tiene mitad, que es .9')
    else:
        print(f'el numero {n} es impar')
# 4 En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for n in range(0,6):
    print(n ** 3)

# 5 Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

var3 = random.randint(0,20)

for n in range(0,var3):
    print(n)

# 6 Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
# var4 = random.randint(1,24)

# if type(var4) == int and var4 > 0:
#     factor = 2

# while var4 > 1:
#     if var4 % factor == 0:
#         print(factor)
#     else: 
#         factor += 1

# else:

#     print(f'el valor {var4} debe contener un numero entero positivo')

# 7 Crear un ciclo for dentro de un ciclo while

n = 0
while n != 10:
    if(n < 10):
        print(f'el valor actual de n es: {n}')
        n += 1

    else:
        break    
    


# 8 Crear un ciclo while dentro de un ciclo for
for n in range(0,10):
    print(n)
while n != 9:
    print(f'esto es un while anidado con un for, vamos en la vuelta{n+1}')
    if(n == 9):
        break

# 9 Imprimir los números primos existentes entre 0 y 30
for n in range(0,30):
    if(n % 2 != 0):
        print(f'el valor, {n} es un numero primo')

# 10 ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

for n in range(0,30):
    

    if(n % 2 != 0):
        print(f'el valor, {n} es un numero primo')
    
    elif(n == 0):
        continue
   

        
    


# En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

    #Deveria de revisar el tiempo de respuesta y la cantidad de memoria que se esta destinando para los procesos, desconozco al momento como hacerlo.



# Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
    #No por el contrario, es menos optimo.

# Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

va = True
while va ==  True:

    break
# Utilizar la función input() que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
 
con = True
while con == True:
    val_k = int(input('Digita el un numero entre el 0 y 100'))

    if(type(val_k) != int):
        print('Por favor ingresa un numero valido')
    
    elif(val_k % 2 == 0):
        print(f'el valor {val_k} es no es primo, y el siguiente valor primo seria {val_k+1}')
        break
    
    elif(val_k % 2 == 0):
        print(f'el valor, {val_k} es primo, el siguiente numero primo es {val_k + 2}')
        break
# Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

con_dition =  100

while con_dition < 300:

    if(con_dition%3 == 0 and  con_dition%6 == 0):
        print(f'el valor que cumple con lo requerido es: {con_dition}')
    else:
        con_dition +1






'''Comentarios

1. CTRL + / : Comentar codigo, seleccionado
2. Diferencia entre tupla y lista
3. Valores alfanumericos, y diferencia entre el elif, else. >>>> Aparentemente el elif, necesita una condicion para usarse.



Revisar con detenimiento el ejersicio 6 y 7
    En el caso del 7, por que la jerarquia de estructura debe ser de esa manera.

    10>     #Deveria de revisar el tiempo de respuesta y la cantidad de memoria que se esta destinando para los procesos, desconozco al momento como hacerlo.


'''