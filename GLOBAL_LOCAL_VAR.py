class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

p1 = Person("Tim")
print(p1.number_of_people)  # 1
print(Person.number_of_people)  # 1
p2 = Person("Bob")
print(p2.number_of_people)  # 2
print(Person.number_of_people)  # 2

class Person2:
    number_of_people2 = 0

    def __init__(self, name):
        self.name = name
        Person2.add_person()

    @classmethod
    def number_of_pp(cls):
        return cls.number_of_people2

    @classmethod
    def add_person(cls):
        cls.number_of_people2 += 1

p1 = Person2("Tim")
p2 = Person2("Bob")
print(Person2.number_of_pp())  # 2

=======================================================================================
res=0
op=""

def show(n):
    global op
    print("n:",n)
    op=""

def suma(n):
    global res, op
    op="s"
    res+=n
    print("+:",res)

def resta(n):
    global res, op
    op="r"
    res=-res+n
    print("-:", res)


def igual(n):
    global res
    res+=n
    print("=:", res)

show(2)
suma(2)
show(3)
suma(3)
show(2)
igual(2)
print("----------------------")
res=0
show(2)
resta(2)
show(3)
resta(3)
show(2)
igual(2)