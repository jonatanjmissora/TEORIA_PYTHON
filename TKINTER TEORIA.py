#============================================================================
#               CLASES VENTANA
#============================================================================
from tkinter import *

class Ventana():
    def __init__(self, win, x, y, ancho, alto, titulo):
        self.win=win
        self.win.geometry(str(ancho)+ "x" + str(alto) + "+" + str(x) + "+" + str(y))
        self.win.title(str(titulo))

        self.label1 = Label(win, text="Escriba algo:").place(x=5, y=0)
        self.entry1 = Entry(win).place(x=5, y=25, width=185)
        self.boton1 = Button(win, text="Miau", command=self.func1)
        self.boton1.place(x=5, y=50, width=185)

    def func1(self):
        print("Hello word")

root=Tk()
v1 = Ventana(root, 450, 300, 200, 90, "Buenos días")
root.mainloop()

#otra forma de crear clase
from tkinter import *
class Application(Frame):
    def __init__(self, window):
        super().__init__(win)
        window.title("Panel de widgets")
        window.geometry("300x300+100+100")
        self.lab= Label(self, text="Etiqueta")
        self.lab.pack()
        self.but= Button(self, text="Boton")
        self.but.pack()
        self.pack()
win = Tk()
app = Application(win)
app.mainloop()

#otra definiendo los widgets en la clase ventana
from tkinter import *

class Win:
    def __init__(self, win):
        self.win = win
        self.button1 = Button(win, text = 'Close', command = self.close)
        self.button1.pack()
    def close(self):
        self.win.quit()

def main(): 
    root = Tk()
    app = Win(root)
    root.mainloop()

if __name__ == '__main__':
    main()

#otra si defino los widgets afuera de windows
from tkinter import *

class Buttons:
    def __init__(self, win):
        self.win = win
        self.button1 = Button(win, text = 'Close', command = self.close)
        self.button1.pack()
    def close(self):
        self.win.quit()

class Win:
    def __init__(self, win):
        self.win=win
        self.button1 = Buttons(win)

def main(): 
    root = Tk()
    app = Win(root)
    root.mainloop()

if __name__ == '__main__':
    main()

#============================================================================
#               PARAMETROS A VENTANA
#============================================================================
.title("Ventana 1")
.config(bg="red", ...)
.geometry("300x400+110+100")
.resizable(True, False)
command=win.quit    # asiciado a cualquier boton o func de widget, cierra la ventana

#============================================================================
#               PARAMETROS de widget: 
#============================================================================
(text="Hola \n a todos", activebackground="yellow", activeforeground="red",
 width=20, height=10, anchor="nw", bg="#38EB5C", bitmap="question",
 bd=15(borde), command=..., cursor="hand1", compound="left"(lugar del icono),
 state="disable", disabledforeground="", font=("Helvetica",15), fg="red", 
 justify="right", relief="flat", overrelief="raised", 
 relief="raised", borderwidth=5, state="normal", fill=x)

#============================================================================
#               PACK
#============================================================================
parametros: fill=(X,Y,BOTH) llena el espacio en el frame
            side=(LEFT, RIGHT, TOP, BOTTOM) posicion dentro del frame
            padx pady separacion con el parent
            ipadx, ipady relleno para que se vea dentro del frame
            expand=(0,1) si el parent tiene espacio, el =1 permite expandirse
            anchor=(N, W, E, S, CENTER) posicion dentro del frame
cuando haces .pack() debes tener en cuenta que muchos metodos, no toman efecto
sino se hace .pack() en otro renglon.
metodos:    .pack_configure()

#============================================================================
#               GRID
#============================================================================
parametros: row, column, padx, ipad, 
            columnspan, rowspan para ocupar mas de una fila o columna
            sticky=(N, W, S, E, etc) a que bordes se pega el widget
metodos:    .grid_configure()   grid_info()     grid_size()

#============================================================================
#               PLACE
#============================================================================
parametros: anchor=NW(donde se posiciona), height, width, relx(offset x e y, en el rango de
            0.0 a 1.0 en relacion a la ventana que lo contiene), x, y, relheight, relwidth)
metodo:     .place_info()  .place_configure()

#dividir en 2 frames segun variable split
from tkinter import *

win=Tk()
f1 = Frame(win, bd=10, relief=SUNKEN)
f2 = Frame(win, bd=10, relief=SUNKEN)
split = 0.5
f1.place(rely=0, relheight=split, relwidth=1)
f2.place(rely=split, relheight=1.0-split, relwidth=1)
mainloop()

#============================================================================
#               BUTTON
#============================================================================
class boton:
    def __init__(self, ventana, text, row, col):
        Button(ventana, ...).grid(...)
...    
boton1=boton(root, "uno", 0, 0)

parametros: bg, bd, command, fg, font, width, height, image, justify, padx, relief,
            state, anchor, compound, cursor, takefocus, text, textvariable, underline 
metrodos:   .destroy()  .cget() .configure() .flash()
            .invoke()  #invoco, por codigo, la accion que tiene asociada el boton

# Cambiar Parametros por funcion
# debo hacer .pack() aparte, y ahi puedo hacer: button.["text"]="DOS"

from tkinter import *
root = Tk()
def prueba():
     button["text"]="DOS"
button = Button(root, text="UNO", command=prueba) #puedo pasar lambda tambien
button.pack()
button["text"]="TRES"
root.mainloop()

from tkinter import *
class botones:
    def __init__(self, win, txt):
        self.b=Button(win, text=txt, command=self.click)
        self.b.pack(side="left")
    def invokes(self):
        self.b.invoke()
    def click(self):
        self.b.config(bg="yellow")
    def cambiar(self, txt2, color):
        self.b["text"]=txt2
        self.b["bg"]=color  # idem self.b.config(bg="red")
    def cambiar2(self, side):
        self.b.pack(side=side)  #modifico pack, place o grid
root=Tk()
b1=botones(root, "Uno")
b2=botones(root, "Dos")
#b1.cambiar("TRES", "red")      #modifico los parametros del boton
b2.cambiar2("right")
#b1.invokes()       #por codigo le hago ejecutar la funcion asociada al boton
root.mainloop()

from tkinter import *
class botones:
    def __init__(self, win, txt):
        self.b=Button(win, text=txt)
        self.b.grid(row=0, column=0)
    def cambiar(self, r, c):
        self.b.grid(row=r, column=c)    #modifico pack, place o grid
root=Tk()
b1=botones(root, "Uno")
b2=botones(root, "Dos")
b3=botones(root, "Tre")
b4=botones(root, "Cua")
list_botones=[b1, b2, b3, b4]
i=0
for x in range(2):
    for y in range(2):
        list_botones[i].cambiar(x, y)
        i+=1
root.mainloop()

#============================================================================
#               CANVAS
#   frame para dibujar y pegar widgets
#============================================================================
usado para poner graficos ademas de los demas widgets
parametros: bd, bg, closeenough, confine, cursor, height, relief, scrollregion, 
            takefocus, width, xscrollcommand
metodos:    itemconfigure, delete, find_all, find_enclosed, find_closest, move, 
            scale, coords

#ejemplo1
from tkinter import *
root = Tk() 
C = Canvas(root, bg ="yellow", height = 250, width = 300) 
line = C.create_line(108, 120, 320, 40, fill ="green") 
arc = C.create_arc(180, 150, 80, 210, start = 0, extent = 220, fill ="red") 
oval = C.create_oval(80, 30, 140, 150, fill ="blue") 
C.pack() 
mainloop() 

#ejemplo2
i = w.create_line(xy, fill="red")
w.coords(i, new_xy) # change coordinates
w.itemconfig(i, fill="blue") # change color
w.delete(i) # remove
w.delete(ALL) # remove all items

#ejemplo3 agrupando por tags, son como colecciones
from tkinter import *
master = Tk()
w = Canvas(master, width=200, height=100)
w.pack()
u=w.create_line(0, 0, 200, 100, tags="linea", fill="blue")
d=w.create_line(0, 100, 200, 0, tags="linea", fill="red")
t=w.create_line(0, 50, 200, 50, tags="linea", fill="red")

w.itemconfig(u, tags="azul")            #cambio el tag de "u"
w.addtag_withtag("roja", "linea")       #le agrego un nuevo tag a la coleccion "linea"
print(w.gettags(3))                     #verifico que tags tiene el elemento id=3
print(w.find_withtag("linea"))          #obtengo los elementos de tag "linea"
w.delete("azul")                        #borro todos los elementos con tag "azul"
w.itemconfig("roja", fill="green")      #cambia el color de los tag "roja"
mainloop()

#============================================================================
#               CHECKBUTTON
#   opcion para tildar o destildar. 2 estados
#============================================================================
parametros: anchor, bg, bd, bitmap, command, compound, cursor, font, fg, 
            height, image, justify, padx, relief, state, takefocus, text, 
            textvariable, variable, width, onvalue, offvalue
metodos:    .deselect() .toggle()   .invoke()   .select()

from tkinter import *
root = Tk()
var = IntVar()
def show():
     print(var.get())
checkbutton = Checkbutton(root, text="Probando", variable=var, command=show,
                onvalue=3, offvalue=0).pack()
root.mainloop()

#============================================================================
#               COMBOBOX
#   menu desplegable pero con opcion de escribir sin desplegar menu
#============================================================================
parametros: cursor, height, width, justify, takefocus, textvariable, validate, validatecommand,
            values, postcomand, state="readonly"
metodos:    .current()  .set()  .get()

from tkinter import *
from tkinter.ttk import Combobox
def seleccion(evento):
    print(combo.get())
win=Tk()
lista=[1, 4, 8]
combo=Combobox(win, values=lista, width=5)   # idem combo["values"]=(1, 2, 3)
combo.pack()                             
combo.current(0)                
combo.bind("<<ComboboxSelected>>", seleccion)
combo.bind("<Return>", seleccion)       #puedo ingresar valor y luego "ENTER"
win.mainloop()

#============================================================================
#               ENTRY
#   entrada de texto de una linea
#============================================================================
parametros: bg, bd, cursor, fg, font, justify, relief, show, state, takefocus, 
            textvariable, width, validate, validatecommand, readonly
metodos:    .insert(0, "te decia")    #donde 0 es el indice a insertar
            .delete(0, END)         #desde donde a hasta donde borramos
            .focus_set()            #pone el cursor para escribir
            .index(index) 
             text_var=StrinvVar()   text_var.get()     text_var.set()

var=StringVar() # es la variable de entrada salida de datos
                #declararla como global si va a una funcion
E=Entry(win, textvariable=var,...)
var.get()   # lo invocamos con .get()
var.set()

# codigo para verificar que la entrada, a medida que se tipea, sean solo digitos
from tkinter import *
def check_input(e):
    return e.isdigit()
win=Tk()
entry1=Entry(win)
entry1.pack()
c = win.register(check_input)
entry1.configure(validate="key",validatecommand=(c,'%P'))
mainloop()

#============================================================================
#               FRAME
#   sirve para agrupar widgets en espacios rectangulares
#============================================================================
parametros: bg, bd, width, height, cursor, relief, padx, pady, fill 
            takefocus(cambiamos frame con Tab), colormap="new"
metodos: f.cget("bg")     f["bg"]="red" # si el .pack() esta separado

f = Frame(win, width=100, height=100, bg="grey", bd=5, relief=SUNKEN)
f.pack(fill=X, padx=5, pady=5)
usar para separar widgets
separator = Frame(win, height=2, bd=1, bg="grey", relief=SUNKEN)

#============================================================================
#               LABEL
#   para mostrar texto (1 sola linea) o imagenes
#============================================================================
parametros: anchor, bg, bitmap, bd, compound(mezcla texto e imagen),
            cursor, font=("Helvetica", 16), fg, height, image, justify, padx, 
            relief, state, takefocus, text, textvariable, underline, width) 
metodos: lab.cget("text")   lab["text"]="hola"  var.get() var.set("HI")
var=StringVar()
img = PhotoImage(file='myimage.gif')
lab = Label(win, textvariable=var, image=img, compound="center", bg="grey")
lab.cget("text")

#============================================================================
#               LISTBOX
#   lista de a renglones, donde cada renglon es elemento de la lista
#============================================================================
paramteros: activestyle, bg, bd, cursor, font, fg, height, width, relief,
            selectmode, state, takefocus, listvariable, justify
            selectforeground, selectbackground, selectborderwidth
metodos:    .insert()   .delete()   .get()  .set()  .bind()  .curselection()
            .itemconfigure(3, bg="red") puedo darle estilos distintos a los items

from tkinter import *
win=Tk()
lis=StringVar()
def mostrar():
    for item in lista.curselection():
        print(lista.get(item))
lista=Listbox(win, listvariable=lis, selectmode=EXTENDED)   
lista.pack()                             
lis.set("matematica geografia lengua ingles historia")  #
print("Toda la lista es:", lis.get())       #
lista.bind("<Return>", lambda event: mostrar())
win.mainloop()
#sino usamos un listvariable se hace:
#lista.insert(0, "matematica")
#lista.insert(END, "mate", "fisica", "Gym")
#li=("mate", "fisica", "Gym")
#lista.insert(0, *li)
#lista.get(2)   # obtengo el item de la posicion 2
#lista.delete(2)
#lista.get(0, END)  # retorna una tupla con todos los elementos
#lista.delete(0, END)
#str = lis.get()    # nos retorna una cadena de caracteres, no es tupla
                    # porque lis es un StringVar()
# t = eval(lis.get())    #con esto convierto StringVar en una tupla
#print(t[0])    
#lista = Listbox(win, selectmode=EXTENDED) #para seleccionar mas de un item
#lista.curselection()   #retorna una tupla con los indices de los elementos seleccionados
#lista.curselection_set(2)  #selecciono el 3er elemento, tb se puede (0, END)
#lista.selection_clear()    #des-selecciona
#lista.selection_includes(3)    #True si el 4to elemento esta seleccionado

#============================================================================
#               MENU
#   menu clasico desplegable, con menues en cascadas
#============================================================================
menu desplegable con opciones de submenu
parametros: bg, bd, cursor, font, fg, postcomand, relief, tearoff, tearoffvariable, 
            title, image, accelerator
metodos:    add_command, add_separator, add_cascade, add_checkbutton, add_radiobutton
            delete, index, invoke, 

from tkinter import *
root = Tk()
menu = Menu(root)
file = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file)
file.add_command(label="New", command=doNew)
file.add_command(label="Open", command=donOpen)
file.add_separator()
file.add_command(label="Exit", command=root.quit)
root.bind('<Control-1>', lambda e: menu.post(e.x_root, e.y_root))
root.config(menu = menu) 
mainloop() 

# hacer un menu desplegable cuando click derecho en la ventana
from tkinter import *
root = Tk()
menu = Menu(root, tearoff=0)
menu.add_command(label="hola")
root.bind('<Control-1>', lambda e: menu.post(e.x_root, e.y_root))
root.bind('<3>', lambda e: menu.post(e.x_root, e.y_root))     #<= no se porque, pero hay
root.mainloop()                                               #que ponerlo

# menu que se actualiza cada vez que seleccionamos una opcion
from tkinter import *
root = Tk()
counter = 0
def update():
    global counter
    counter = counter + 1
    menu.entryconfig(0, label="clicks: "+str(counter))
menubar = Menu(root)
menu = Menu(menubar, tearoff=0, postcommand=update)
menu.add_command(label="clicks: "+str(counter))
menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Test", menu=menu)
root.config(menu=menubar)
root.mainloop()

#============================================================================
#               NOTEBOOK
# se pueden elegir distintas paginas segun solapas en la parte superior
#============================================================================
parametros1: height, width, padding, takefocus
parametros2: state, sticky, padding, text, image, compound, underline
metodos:    add, forget, hide, index, insert, select, tab, tabs
            parametros en add y tab (parametros2)
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
note = ttk.Notebook(win, width=400, height=400, padding=5)
note.pack()
fr1 = tk.Frame(note, bg="red")
fr2 = tk.Frame(note, bg="yellow")
lab1 = tk.Label(fr1, text="Hola").grid()
lab2 = tk.Label(fr2, text="mundo").grid()
note.add(fr1, text="Web")
note.add(fr2, text="Foro")
note.select(fr2)   

# se puede re-configurar los parametros de una pestaña con
note.tab(lab1, text="Chauu")
#puedo invocar una funcion cuando cambio de pestaña
note.bind("<<NotebookTabChanged>>", tab_changed)
tk.mainloop()

#============================================================================
#               OPTION MENU
#   menu desplegable donde se elige una opcion
#============================================================================
parametros: anchor, bg, bd, bitmap, command, cursor, font, fg, height, width, image, 
            justify, padx, relief, selectimage, state, text, textvariable, value, variable
metodos:    select()    deselect()      invoke()
from tkinter import *
win=Tk()
color=StringVar()
colores=["red", "yellow", "blue", "black", "white"]
color.set(colores[0])
def show(x):
    L["bg"]=x
    L["text"]=x
menu=OptionMenu(win, color, *colores, command=show).pack()
L=Label(win, text=colores[0])
L.pack()
win.mainloop()
#en vez de poner *colore se puede poner "red", "green", ... como parametros, en vez de la lista

#============================================================================
#               PANEDWINDOW
#============================================================================
from Tkinter import *

m1 = PanedWindow(orient="vertical", bd=10, bg="grey", showhandle=True)
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane")
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)
top = Label(m2, text="top pane")
m2.add(top)
bottom = Label(m2, text="bottom pane")
m2.add(bottom)

mainloop()

#============================================================================
#               PROGRESSBAR
#============================================================================
from tkinter import *
from tkinter import ttk
win = Tk()
var=IntVar()
def sube():
    var.set(var.get()+20)
pb=ttk.Progressbar(win, variable=var)
pb.pack()
Button(win, text="+", command=sube).pack()
mainloop()

#============================================================================
#               RADIOBUTTON
#   para elegir solo una opcion entre varias
#============================================================================
parametros: anchor, bg, bd, bitmap, command, compound, cursor, font, fg, 
            height, image, justify, padx, relief, state, takefocus, text, 
            textvariable, value, variable, width, 
            indicatoron=(0 default si quiero que este el puntito, o 1 si quiero
                que sea tipo boton)
metodos:    .deselect() .toggle()   .invoke()   .select()
from tkinter import *
root = Tk()
var = IntVar()
def prueba():
     print("Se ha elegido la opcion " + str(var.get()))
rad1 = Radiobutton(root, text="Opcion 1", variable=var, value=1, command=prueba)
rad2 = Radiobutton(root, text="Opcion 2", variable=var, value=2, command=prueba)
rad1.pack()
rad2.pack()
root.mainloop()

#============================================================================
#               SCROLLBAR
# barra de desplazamiento
#============================================================================
parametros: orient=(VERTICAL, HORIZONTAL), width
metodos:    get(), set(), config()

from tkinter import *
win = Tk()
scrollbar = Scrollbar(win, orient=VERTICAL)
listbox = Listbox(win, yscrollcommand=scrollbar.set)

for i in range(20):
    listbox.insert(END, "Elemento {}".format(i))

scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)  #con grid usamos sticky=NS
listbox.pack()
mainloop()



#============================================================================
#               SEPARATOR
#============================================================================
sep=Separator(win).pack(fill=X)
#usado mas que nada con .grid() y columnspan=5    o   sticky="ns"

#============================================================================
#               TEXT
#   multilinea de texto, con colecciones configurables
#============================================================================
puede manejar muchas lineas de texto, con distintas opciones para cada linea
paramteros: bg, bd, cursor, font, fg, height, padx, relief, spacing1, 
            state="normal/disable", takefocus, width, wrap, xscollcommand
metodos:    delete, index, get, insert, 

from tkinter import *
root = Tk() 
def take_input(): 
    print(i.get("1.0", "end")) 
def change_bg():
    i["fg"]="red"
    i["font"]=("Helvetica", 20)
i = Text(root, height = 10, width = 25, fg="green")
i.pack()
i.insert("2.0", "Enter text here") 
b1 = Button(root, text ="Show", command = take_input)
b1.pack()
b2 = Button(root, text = "Cambiar", command = change_bg)
b2.pack()
mainloop()  

# hacer el texto subrayado
L=Label(win, text="HOLA", font=("Arial", 10))
f=font.Font(L, L.cget("font"))
f.configure(underline=True)
L.configure(font=f)

#============================================================================
#               TREEVIEW
#============================================================================
