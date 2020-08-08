class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.is_active = False

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def num_of_students(self):
        return len(self.students)

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)
course = Course("Science", 4)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(s3.name, s2.name, s1.name)            #   Jill Bill Tim
print(course.name)                          #   Science
print(Student.get_grade(s1))                #   95
print(Course.num_of_students(course))       #   3
print(course.students[1].name)              #   Bill
print(course.num_of_students())             #   3
print(course.get_average_grade())           #   78.333
for x in course.students:
    print(x.name)                           # Tim /n  Bill  /n  Jill
for x in range(0, len(course.students)):
    print(course.students[x].name)          # Tim /n  Bill  /n  Jill


============================================================================================
p = Pet(Tim, 3)    p es una instancia de la clase Pet
                name y age son atributos de la clase Pet
                las funciones definidas dentro de la clase
                se llaman metodos

class Dog:
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dog(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        for i in range(n):
            print("Bark")

pucho = Dog("Pucho")
print(Dog.dogs)     #puedo invocar una variable definida en la clase
print(pucho.dogs)   #se puede hacer con el objeto pucho, pero Dog es mas general a la clase

print(Dog.num_dog())    # idem con los metodos
print(pucho.num_dog())  # pero dog es mas general a toda la clase

Dog.bark(3)     #creamos una funcion general de la clase, no tenemos que crear ningun objeto
                #para usarla. No puede usar las variables de la clase, como "dogs"
class Math:
    @staticmethod
    def add(x, x2):
        return x + x2

math.add(2, 4)  #para esto es un metodo estatico

# tengo 2 archivos, uno en donde defino la clase y los metodos que usa una clase
# y el otro donde importo los metodos de esa clase

# archivo llamado "metodos.py"
# contiene lo siguiente
#class UnaClase:
#   def __init__(self, name):
#       self.name = name

#   def print(self):
#       print(self.name)

# y en el otro archivo puedo poner
#import metodos
#from metodos import print      #si esto no lo pongo, tengo que invocar con tim=metodos.UnaClase("Tim")

#tim = UnaClase("Tim")
#tim.print()
=============================================================================================================
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

    def speak(self):
        print("Soy un Pet")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Soy " + self.name + " y tengo " + str(self.age) + " y soy " + self.color)

class Dog(Pet):
    def speak(self):
        print("Soy un Dog")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.show()                        #   Tim 19
c = Cat("Bill", 34, "marron")
d = Dog("Boby", 15)
f = Fish("Bubble", 5)
p.speak()                       #   Soy un pet
c.speak()                       #   Soy Bill y tengo 34 y soy marron
d.speak()                       #   Soy un Dog
f.speak()                       #   Soy un Pet

==============================================================================================================


"""
#================== __NAME__==__MAIN__ ====================

primer_archivo.py                   !   segundo_archivo.py
                                    !   
print("esto se ejecuta siempre")    !   import primer_archivo
print( "sea importado o no")        !   
                                    !   print("estoy en el segundo_archivo")        
def main():                         !   
    print("esto se ejecuta si")     !
    print("se ejecuta este archivo")! 
                                    !
if __name__ == "__main__":          !
    main()                          !


cuando ejecutamos un archivo en python, automaticamente asigna
__name__ == __main__.
cuando el archivo es importado, ejecutado desde otro archivo, 
ya el __name__ asignado sera el nombre del archivo, es decir
__name__ == primer_archivo
 y no ejecutaria el modulo "def main():", si es importado. 

si ejecuto el primer_archivo.py la salida sera:
--> "esto se ejecuta siempre sea importado o no"
--> "esto se ejecuta si se ejecuta este archivo"

si ejecuto el segundo_archivo.py la salida sera:
--> "esto se ejecuta siempre sea importado o no" 
--> "estoy en el segundo archivo"


#============== CLASES ========================
#instancia = objeto de clase
#variables de instancia = atributos y son unicos a cada instancia (.nombre, .apellido, .paga)

class Empleado():
    
    aumento = 1.04
    num_empleados = 0
    def __init__(self, nombre, apellido, paga):
        self.nombre = nombre
        self.apellido = apellido
        self.paga = paga
        self.mail = nombre + apellido + "@gmail.com"
        Empleado.num_empleados +=1

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

    def aumentar_paga(self):
        self.paga = self.paga * self.aumento

    @classmethod                # son metodos que modifican a la clase o sus variables
    def aplicar_aumento(cls, aum):
        cls.aumento = aum

    @staticmethod               # son metodos que no dependen de la clase ni las instancias
    def hay_que_compar(stock):
        if stock < 10:
            return True
        else:
            return False

    def __repr__(self):         # forma de representar la instancia como creacion de ella "print(emp1)" --> Empleado("gus", "ote", 45)
        return "Empleado('{}', '{}', {})".format(self.nombre, self.apellido, self.paga)     #si esta el metodo __str__, entonces __repr__ no se ejecuta

    def __str__(self):          # forma de representar la instancia para que sea legible "print(emp1)"  --> gus ote
        return "{} {}".format(self.nombre, self.apellido)

class Programador(Empleado):    
    aumento = 1.2
    def __init__(self, nombre, apellido, paga, programa):
        super().__init__(nombre, apellido, paga)        # = Empleado.__ini__(self, nombre, apellido, paga) pero no se usa
        self.programa = programa

class Gerente(Empleado):
    aumento = 1.5
    def __init__(self, nombre, apellido, paga, empleados_a_cargo=None):
        super().__init__(nombre, apellido, paga)
        if empleados_a_cargo is None:
            self.empleados_a_cargo = []
        else:
            self.empleados_a_cargo = empleados_a_cargo

    def add_empleado(self, emp):
        if emp not in self.empleados_a_cargo:
            self.empleados_a_cargo.append(emp)

    def remove_empleado(self, emp):
        if emp in self.empleados_a_cargo:
            self.empleados_a_cargo.remove(emp)

    def mostrar_emp(self):
        for emp in self.empleados_a_cargo:
            print("-->", emp.nombre_completo())



# creo instancias (objetos) de la clase
emp1 = Empleado("gus", "ote", 45)
emp2 = Empleado("ro", "mose", 39)

# invoco un metodo de la clase
#print(emp1.nombre_completo())  # idem Empleado.nombre_completo(emp1)

# conocer los metodos y atributos de una clase
#print(Empleado.__dict__) #me lista todos los metodos y variables de clase
#print(emp1.__dict__)   # me lista todos los atributos de instancia

# invoco un metodo para modificar un atributo de la instancia
#emp1.aumentar_paga()
#print(emp1.aumento) # = emp2.aumento = Empleado.aumento  muestra 

# esto crea un atributo nuevo solo para emp1, pero no modifica nada del resto de la clase
#emp1.aumento = 1.05 # esto crea un atributo nuevo de emp1, pero no modifica la variable de clase
#print(emp1.aumento, emp2.aumento)  #1.05  1.04

# esto si modifica una variable "aumento" que es de la clase, y sirve para todas las instancias
#Empleado.aumento = 1.10     #con esto modifico la variable de clase y sirve para todas las intancias
#print(emp1.aumento)  # 1.10 
#print(Empleado.num_empleados) # = emp1.num_empleados

# @classmethod
#Empleado.aplicar_aumento(1.15)  # = Empleado.aumento = 1.15 
                                # hago un metodo para cambiar una variable de clase

#@staticmethod
#Empleado.hay_que_compar(7)     # invoco una funcion que la inclui en la clase, 
                                # pero no depende de ella ni de las instancias
# lases heredadas
#print(prg1.nombre_completo())  # heredan todos los metodos y variables de clase
#print(prg1.aumento)

# info de quien heredo
#print(help(Programador))     # puedo ver de quien hereda, tambien metodos y variables heredadas

# creo especificaciones de la subclase, como una rectificacion de aumento
#print(prg1.aumento)        # sin modificaciones en la clase principal
#print(prg1.programa)

gr1 = Gerente("arr", "miss", 150, [emp1])
#gr1.add_empleado(emp2)
#gr1.mostrar_emp()
#gr1.remove_empleado(emp1)
#gr1.mostrar_emp()

#print(isinstance(gr1, Empleado)) # es True, tambien de Gerente, es Falso de Programador
#print(issubclass(Gerente, Empleado)) # es True, y (Gerente, Programador) es False

#para ver que hace __repr__
#print(gr1)     # = print(gr1.__repr__())   --> Empleado("arr", "miss", 150)

# para ver que hace __str__
#print(gr1)     # = print(gr1.__str__())    --> arr miss


#=========================================================================
# property decorators
class Empleado():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = nombre + "." + apellido + "@gmail.com"
        
emp1 = Empleado("gus", "ote")
# si hacemos 
print(emp1.mail)    # --> gusote@gmail.com
emp1.nombre = "pepe"    # cambio solo el atributo .nombre
print(emp1.mail)    # --> sigue siendo gusote@.. porque el mail se creo cuando se creo la instancia.
                    # para solucionar eso, se puede hacer un metodo que sea def mail(self):
                    # pero el problema es que debemos reemplazar en todo el program cuando quiero acceder al mail
                    # emp1.mail    por   emp1.mail()
# para evitar modificar lo, tenemos el metodo @property  

class Empleado():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    @property                   # hace que el metodo se invoque como emp1.mail y no como emp1.mail()
    def mail(self):             # transforma un metodo en un atributo casi
        return "{}.{}@gmail.com".format(self.nombre, self.apellido)

emp1 = Empleado("gus", "ote")

print(emp1.mail)    # --> gus.ote@gmail.com
emp1.nombre = "pepe"    # cambio solo el atributo .nombre
print(emp1.mail)    # --> pepe.ote@gmail.com    ya que ahora uso el metodo @property y lo invoco como un atributo 
"""
# @setter @getter
class Empleado():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @property
    def fullname(self):
        return "{} {}".format(self.nombre, self.apellido)
    
    @fullname.setter                        # esto me permite cambiar en codigo, los atributos de emp1, por unos nuevos
    def fullname(self, name):               # con el formato de fullname
        nom, apell = name.split(" ")
        self.nombre = nom
        self.apellido = apell

emp1 = Empleado("gus", "ote")
emp1.fullname = "rod mose"          # esto hace que vaya a .setter y asigne nuevos valores a .nombre y .apellido
print(emp1.fullname)