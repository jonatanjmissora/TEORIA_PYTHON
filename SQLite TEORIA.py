#CREAR TABLA y ARCHIVO
#SQLite base de datos
#=======================================================================
import sqlite3
conn = sqlite3.connect("Base.db")
c = conn.cursor()

########## esto es lo que se cambia segun lo que quiera hacer con la Tabla
c.execute("""CREATE TABLE clientes (
			nombre text,
			apellido text,
			edad int)
			""")
##########

conn.commit()
conn.close()

#INSERT RECORDS
#cambiamos solo lo que esta entre ####
#=======================================================================
c.execute("INSERT INTO clientes VALUES ('Jonatan','Missora','41')")
conn.commit()
# si quiero insertar varios, creo una lista
varios_clientes = [('Albana','Garcia','35'),
				   ('Gianluca','Missora','6'),
				   ('Leon','Buccella','6')]
c.executemany("INSERT INTO clientes VALUES (?,?,?)", varios_clientes)

#READ RECORDS
#=======================================================================
c.execute("SELECT * FROM clientes")
#c.execute("SELECT rowid, * FROM clientes")		#si quiero poner los indices internos
#c.execute("SELECT * FROM clientes WHERE nombre='Jonatan'")	#si quiero buscar
#c.execute("SELECT * FROM clientes WHERE nombre LIKE 'Jo%'") #% significa "lo que siga"
#c.execute("SELECT rowid, * FROM clientes WHERE apellido='Missora' AND edad < 10")
[print(row) for row in c.fetchall()]

#UPDATE RECORDS
#=======================================================================
c.execute("UPDATE clientes SET nombre='Bianca' WHERE apellido='Missora'")
# cambia TODOS los nombres por Bianca en los apellidos Missora
# sino uso el rowid
c.execute("UPDATE clientes SET nombre='Bianca' WHERE rowid=1")

#DELETE RECORDS
#=======================================================================
c.execute("DELETE FROM clientes WHERE rowid=1")	#solo el 1er record
c.execute("DELETE FROM clientes WHERE apellido='Missora'")	#todos los missora

#SORT RECORDS
#=======================================================================
c.execute("SELECT rowid, * FROM clientes ORDER BY rowid DESC")	#default pero descendente
c.execute("SELECT rowid, * FROM clientes ORDER BY apellido") #orden alfabetico de apellidos

#BORRAR TABLA
#=======================================================================
c.execute("DROP TABLE clientes")




