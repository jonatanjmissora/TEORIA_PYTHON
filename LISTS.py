# generar listas comprimidas
digits = list(range(10))          # digits = [0,1...,8,9]
x = list(range(2, 11, 2))           # x = [2, 4, 6, 8, 10]
strs = [str(d) for d in digits]     # strs = ["0",...,"9"]

lista = [1, 2, 3, 4, 5]
lista2 = [5, 10, 15]
lista3 = []
for x in lista:             # es lo mismo que escribir
    lista3.append(x)        # lista3 = [x for x in lista]

multilista = [[1, 2, 3], [4, 5], [6]]
completa = []
for sub in multilista:
    for x in sub:               # es lo mismo que escribir
        completa.append(x)      # completa = [x for sub in multilista for x in sub]

for n in lista:
    if n < num:                 # es lo mismo que escribir
        lista3.append(n)        # [n for n in lista if n<num]

customlist = [a*b for a in lista for b in lista2 if a*b%2 != 0]
print(customlist)                       # [5, 15, 15, 45, 25, 75]

# lista de numeros primos hasta el 49
no_primos = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primos = [x for x in range(2, 50) if x not in no_primos]
print(primos)

a = [2, 3, 4, 5, 6, 7]       # lista nueva, con [x,y] donde y in b es el multiplo
b = [12, 14, 10]             # de x in a
c = [[x, y] for x in a for y in b if y % x == 0]
for i in c:
    print(i)

c = [i for i in set(a) if i in b]       # interseccion de 2 listas
d = list(set(i for i in a if i in b))   # idem
n = int(math.sqrt(num))
a = [x for x in range(2, n + 1) if num % x == 0]    # divisores de num
z = [x for x in a[0::len(a)-1]]                     # lista con primer y ultimo elemento

# metodos de la lista
rand = [6, 22, 7, 1, 16]
rand.sort()
print(rand)                         #   [1, 6, 7, 16, 22]
c = sorted(a)                       # c = [1, 6, 7, 16, 22]
a = list(range(10))                 # a = [0, 1..., 8, 9]
ind = a.index(4,2,7)                # busca la posicion de "4"  dentro de a[2:7]
a.insert(3, 11)                     # inserta 11 en la posicion 3, desplaza la lista
for i in range(2, 5):               # remueve los obj desde el 2do hasta el 4to
    a.remove(i)
for i in a:                         # ejemplo cuando i=0    0 , 0
    print(a.index(i), ",", i)                      # i=1    1 , 1

a = [1, 1, 2, 3, 3, 4, 5, 5]
b = []
[b.append(i) for i in a if i not in b]
print(b)                # b = [1, 2, 3, 4, 5]
c = []
c.extend(i for i in a if i not in c)
print(c)                # c = [1, 2, 3, 4, 5]
a.pop(4)                # regresa el objeto de la posicion 4


S = "telefono"
Sinv = S[::-1]
print(Sinv)                         #   onofelet

#invertir el orden de las palabras de una frase
string = "el mundo esta al reves"
new = string.split()        # ['el', 'mundo', 'esta', 'al', 'reves']
new = new[::-1]             # ['reves', 'al', 'esta', 'mundo', 'el']
new = " ".join(new)         # new = "reves al esta mundo el"

# COUNT
string = "HELLO"
print(string.count("L"))    # 2, de dice la cantidad del argumento en una lista
                            # da 0 sino se encuentra en la lista
# FIND
print(string.find("E"))     # da la posicion de la primera aparicion del argumento
                            # da -1 si no esta el argumento

# MAP
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def func(x):
    return x+3
newlist = []
for i in lista:                 # idem a poner newlist = list(map(func, lista))
    newlist.apped(func(i))      # o tambien    newlist = [func(x) for x in list]

# FILTER

def add7(x):                # filter, filtra una lista segun una funcion que tire
    return x+7              # true o false. Si es true, lo agrega a la lista, sino lo saltea

def isOdd(x)
    return x%2 != 0         # con map, podemos hacer una funcion, con un filtrado de una lista

a = [1, 2, ...10]
b = list(filter(isOdd, a))              # b = [1, 3, 5, 7, 9]
c = list(map(add7, filter(isOdd, a)))   # c = [8, 10, 12, 14, 16]

# LAMBDA
func = lambda x: x+3            # es escribir una funcion pero no hace falta invocarla con
print(func(2))                  # def func(x):      da como salida un solo dato, no una lista
func2 = lambda x, y=2: x+y      # se pueden pasar varios parametros, hasta opcionales

a = [1, 2, ..10]
func = list(map(lambda x:x*2, a))
print(func)                             # func = [2, 4, 6,..20]
func2 = list(filter(lambda x: x%2 == 0, a))
print(func2)                            # func2 = [2, 4, 6..10]

# se puede poner una funcion dentro de otra
def func(x):
    func2 = lambda x: x*2
    return func2(x) + 23

