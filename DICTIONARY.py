post = {"user_id":209, "finit":"S A E", "loc":(11.4, -5)}
post2 = dict(sur="bien", lala=2)
post2["sl"] = "A A"
post2["yoyo"] = 51
print(post)                         #   {'user_id': 209, 'finit': 'S A E', 'loc': (11.4, -5)}
print(post2)                        #   {'sur': 'bien', 'lala': 2, 'sl': 'A A', 'yoyo': 51}
print(post["finit"])                #   S A E
if "yoy" in post2:
    print(post2["yoyo"])
else:
    print("no esta en el dict")     # True
for key in post.keys():
    value = post[key]
    print(key, " = ", value)        # user_id  =  209 /n finit  =  S A E /n loc  =  (11.4, -5)
for key, value in post.items():
    print(key, " = ", value)        # user_id  =  209 /n finit  =  S A E /n loc  =  (11.4, -5)

lista = ["pera", "uva", "manzana", "uva", "pera", "uva"]
counter = {}
for i in lista:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
print(counter)          # {'pera': 2, 'uva': 3, 'manzana': 1}

#para archivos
counter_dict = {}
with open('names.txt') as f:
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