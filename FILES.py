"""# escribir un archivo
open_file = open('test.txt', 'w')
open_file.write('testprimer renglon\n')
open_file.write('segundo renglon\n')
open_file.write('tercer renglon\n')
open_file.close()

#otra forma de escribir, mejor syntaxis
with open('names.txt', 'w') as open_file:
    open_file.write('cuarto renglon\n')

# leer y escribir archivos
with open('names.txt', 'w') as open_file:
    open_file.write('primer renglon\nsegundo renglon')

with open('names.txt', 'r') as open_file:
    all_text = open_file.read()
    all_text = all_text.split("\n")

with open('names.txt', 'r') as open_file:
    line = open_file.readline()
    while line:

# separa la lista por renglones
all_text = all_text.split("\n")

# convierte cada renglon "line" en una lista "char" de caracteres
#chars = list(line) imprime ["D","a","r","t","h","\n"]

counter_dict = {}
    ....
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print("directorio: ", counter_dict) #{"Luke":15, "Darth":31, "Lea":54}
print(counter_dict["Lea"])      #54 ,valor de Lea

for i in counter_dict.items(): #("Luke",15)   ("Darth", 31)   ("Lea", 54)
    print(i)                #  se pueden operar pero como pares juntos

for i in counter_dict:      # luke    Darth   Lea  "no se pueden operar"
    print(i)
#pero si puedo usar sus nombre para operar sus valores
total = 0
for i in counter_dict:
    total += counter_dict[i]
print(total)

total = 0
for x, y in counter_dict.items(): # se pueden operar por separado
    print(x, y)
    if x == "Lea":
        print("esta Lea!!")
    total += int(y)
print(total)

print("solo keys:", counter_dict.keys(), "no se puede acceder")
print("solo values:", counter_dict.values(), "tampoco")
print("los pares:", counter_dict.items(), "sirve para iterar")

# interseccion de numeros de 2 archivos

def arch_list_int(filename):
    with open(filename) as f:
        f = list(map(x, f.read().split()))
    return f

primes = arch_a_ints('num1.txt')
happies = arch_a_ints('num2.txt')
overlap = [x for x in primes if x in happies]
print(overlap)