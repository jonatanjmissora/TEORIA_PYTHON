if (TEST EXPRESIONS):
    (STATEMENTS)
elif (TEST EXPRESIONS):
    (STATEMENTS)
else: (STATEMENTS)

for (VARIABLE) in (SEQUENCIA):
    (STATEMENTS)

while (TEST EXPRESIONS):
    (STATEMENTS)

double = lambda x: x * 2
print(double(5))            #   10

lst = filter((lambda x: x < 0), range(-5, 5))
print(list(lst))

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)         # [4, 6, 8, 12]

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)         # [2, 10, 8, 12, 16, 22, 6, 24]

import sys
    ....
    sys.exit("no es un numero")

import random
options = ["roca", "papel", "tijera"]
p1 = random.choice(options)         # elige un elemento de la lista
ran = random.randint(1, 9)          # elige un solo numero entre 1 y 8 inclusive
t = random.sample(range(1,30), 12)              #sin repeticiones
w = [random.randint(1,30) for x in range(12)]   #con repe
# h = sorted([random.randint(1,30) for x in range(12)])   #con repe y ordenada
s = "abcdefghijklmnopqrstuvwxyz"
p =  "".join(random.sample(s,5 ))   # genera un codigo de 5 caracteres

alt+39 '
alt+60 <
alt+62 >
alt+92 \ 
#sublime shortcuts
crtl+click me pernite hacer varios cursores
alt+F3 me deja elegir todas las palabras iguales a las del cursor
ctrl+D me permitre ir agregando palabras iguales de a una

manejar ventanas en Sublime
alt+shift+2 abre una ventana para ver 2 archivos en paralelo
alt+shift+1 vuelve a un solo archivo abierto

me paro en el ranglon a mover y con 
crtl+shif+flechas de direccion arriba abajo, lo muevo

crtl+(K luego B) cierro y abro el sidebar

# crear modulos(galerias) para importar y utilizar
# creamos un archivo con las funciones del modulo y lo guardamos
def sumar(a, b):
	print("la suma es " + str(a+b))

#en el mismo directorio creo otro archivo que lo importa
import modulo
modulo.sumar(3, 3)

# o mejor aun
from modulo import sumar
sumar(3,7)