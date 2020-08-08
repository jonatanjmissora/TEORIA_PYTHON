for x in range(1, 11):
     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print("primer renglon \nsegundo renglon")
print("esto va to", end = "")
print("do seguido")

print("\nEnter number as a list\n")
lista1=[int(i) for i in input().split()]

cid, prov, cp="Bahia", "BsAs", "8000"
print("Ciudad: %s \nProvincia: %s \tCP: %s" % (cid, prov, cp))			# old
print("Ciudad: {} \nProvincia: {} \tCP: {}".format(cid, prov, cp))		# new

# https://pyformat.info/		formato de print, ejemplos