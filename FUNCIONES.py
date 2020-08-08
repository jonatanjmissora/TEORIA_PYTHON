"""def func(x, y=2):        # a x se lo llama parametro
    return x+y          # y es un parametro opcional, que si no lo defino cuando
                        # invoco a la funcion, toma el valor por defecto
call = func(6)      # a 6 se lo llama argumento
print(call)

# DECORATORS
# 1
def func(string):
	def wrapped(strin):
		print("Start")
		print(string+strin)
		print("End")
	return wrapped

x = func("hola")	# con esto creo el objeto que es la funcion "func()"
					# paso solo lo que me pide func que es string, 
					# no ejecuto wrapped todavia
x(" jon")			# con esto la invoco "wrapped()" y le paso otro strin
"""
#2
def func(f):
	def wrapped():
		print("Start")
		f()
		print("End")
	return wrapped

def func2():			# tiene que estar definida fuera de func()
	print("soy func2")

#x = func(func2)			# idem caso1 pero paso como argumento el nombre
#x()						# de otra funcion

func2 = func(func2)			# otra forma de escribirlo
func2()

# 3
def func(f):
	def wrapped(x):
		print("Start")
		f(x)
		print("End")
	return wrapped

@func 						# esto reemplaza al "func2 = func(func2)"
def func2(x):				# el objeto de hacer esto es: invocar a una
	print(x)				# funcion "func2", que se va a ejecutar en 
							# otra funcion maestra "func"
func2(7)

# se usan comunmente para dejar un registro de tiempo, de valores, que
# se desarrollan en func2. Es como un watch que le pongo a func2.
# en vez de print("Start") y end, le puedo decir que me imprima valores
# de voy metiendo en func2