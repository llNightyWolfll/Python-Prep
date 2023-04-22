#Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
var_1 = 1 
var_2 = 4
var_tot = var_2 + var_1

var_const = 8.5

print(var_const)

print(type(var_const))

var_name = "Edgar Paul Ramirez Sanchez"

var_complex = complex(2,3) # Numero complejo, se puede graficar dentro de dos dimensiones.

print(type(var_complex))

## pi redondeado
pi_rounded = round(3.141592,4)

#var 2 true
 #Si son lo mismo, o mas bien ambas se encuetran en el mismo estado, pero son variables independientes.
 
var_t1 = True
var_t2 = True

#Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

print(type(var_t1))
print(type(var_t2))

# Asignar a una variable, la suma de un número entero y otro decimal

var_1 = 10
var_2 = 1.2
sum = var_1 + var_2
print(sum)

#Realizar una operación de suma de números complejos

num_com_1 = complex(1,2)
num_com_2 = complex(2,3)
print(num_com_1 + num_com_2)

#Realizar una operación de suma de un número real y otro complejo
real_num = 3

print(sum+real_num)
 
#Realizar una operación de multiplicación

prod = 10
prod_2 = 2 

producto = prod * prod_2

#Mostrar el resultado de elevar 2 a la octava potencia

print(2**8)

#Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

di_vi = 27
di_de = 4

resul = di_vi / di_de


print(resul)
rest_1 = int(resul)
#De la división anterior solamente mostrar la parte entera
print(int(resul))

#De la división de 27 entre 4 mostrar solamente el resto
division = int(di_vi%di_de)
print(division)


#Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
op1 = 4
print(type(rest_1) ,type(division))
resul_18 = (rest_1 *op1 + division)
print(resul_18)


 # 6 3 y 4 para obtener 27

 #Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
alph_1 = 'Que mamalon'
alph_2 = 'Apoco no'

#Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

fist_2 = 2
second_2 = '2'

conditional = fist_2 == second_2
print(conditional)

#No es lo mismo, debido a que son diferentes tipo de dato. Uno es una cadena de caracteres y el otro es valor entero

# 20 - Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

second_2 = int(second_2)

conditional = fist_2 == second_2


#¿Por qué arroja error el siguiente cambio de tipo de datos? 
 # a = float('3,8') # No se puede leer un float como tipo str


#23 Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

var_23 = 3
var_23 -=2
print(var_23)

# 24 Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

var_24 = 1 << 2
print(var_24)
   ## Dado que es un desplazamiento de bits hacia la izquierda sobre el valor uno por 2 desplazamientos.
   ## 1 * 2 * 2, uno por la potencia dos, dado que solo hay dos estados elevado a la cantidad de casillas que se movio


#25 Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

    # No esta permitido dado que no son el mismo tipo de dato,uno es una caracter mientras que el otro es un numero entero

# 26 Realizar una operación válida entre valores de tipo entero y string

print(f'Hola a todos mido {1.76 } metros y peso {79}  kg' )

"""Si son lo mismo"""