GIT = SISTEMA DE CONTROL DE VERSIONES (VCS) VERSION CONTROL SYSTEM
===================================================================


========================= CONCEPTOS =================================================================
rama local = master o head (es la que esta en la computadora principal o servidor principal)

working directory = repo local en la compu
rama remota = origin (es la que se pone en la nube, o GitHub)

rama stagin = Index (zona de espera)

========================== COMANDOS ==================================================================

	git version 	(si te da la version, significa que esta instalado)

	git help			(listado de comandos)
	git help commits 	(listado de atributos de un comando)

configuro mis datos:
	git config --global user.name "Jonatan Missora"
	git config --global user.mail "jonatanjmissora@gmail.com"

	git config --list  		(veo todo lo que tengo configurado, para corroborar datos)

tenemos nuestro codigo e inicimos su seguimiento en la carpeta del proyecto. Creamos el repositorio
	git init 	(crea un archivo oculto .git donde guarda el historial de cambios. si queremos dejar
				de registrar cambios, borramos ese archivo y listo)

.gitignore  (si queremos dejar de seguir ciertos archivos o subcarpetas, creamos un archivo en el mismo directorio,
  			con el nombre .gitignore y adentro ponemos en cada renglon, el nombre dell archivo o carpeta a ignorar)

	git status (me da una lista de los archivos o carpetas, que han sido modificados, con respecto al repositorio.
				rojo: estan en en working directory y no estan en el stagin area. No estam traqueados
				verde: estan en el stagin area no en el repo, estan traqueados, listos para commitear, 
				nada: significa que todo lo que esta en el directorio esta igual que el repositorio, no tienen modificacion
	git status -s 		solo muestra los archivos modificados
	?? 				sin traquear porque son nuevos, son rojos
 	 M readme.txt 	M estan modificados y sin traquear, son rojos
	A index.htm 	A estan traqueados, son verdes
	M  opcion.ccs 	readme y opcion tienen la M a la derech (esta en el working) y a la izq (esta en el stagin)	

	git status -v       que muestra?? probar


	git log 				(veo todos los commits que tiene el proyecto)
	git log --oneline		(los veo en una sola linea)
	git log --follow <file> (log solo de ese archivo)
	git log -p -2			(-p muestra las diff, y el -2 muestra silo los 2 ultimos commits)
	git log --stat 			(muestra total de lineas eliminadas y agregadas)
	git log --graph			(muestra dibujo de ramas y merges)
	

	git show <commit> (mustra datos dell commit) 

	git diff <file>			(compara el working directory con el index)
	git diff HEAD <file>	(compara el working directory con el repositorio)
	git diff --cached <file>( o git diff --staged	compara el index con el repositorio)
	
	git diff --staged 		(idem pero dell que ya esta en el stagin)
	(las lineas en rojo, son renglones borrados, las lineas en verde, son las creadas o modificadas)
	git diff nueva_rama			(se pueden comparar rama con master)

	git add <file>  	(agrega el archivo al stagin area)
	git add . 			(agrega todos los archivos)
	git add -A 			(agrega todos los archivos)

	git rm --cached <file>  (saco el archivo dell stagin area)
	git restore <file>	    (vuelvo lo que modifique para atras, al original dell repositorio)

	git commit "Primer commit" 	(graba los cambios al historial dell repositorio, y les da un hash unico a cada commit
								(en vim, insertamos con i. Primer renglon va el commit, luego ESC :wq y salimos con ZZ :q!)
	git commit -m "Primer commit"	(no paso por vim)
	git commit -a -m "Primer commit"	(evita hacer el add de los archivos, lo hace con -a)								

	git log (para ver el listado de commits)

============================  BRANCHES  =================================================================================

	git branch rama_nueva 			(creo una rama paralela a master)
	git checkout rama_nueva 		(cambio a rama_nueva, cambio mi working directory a la rama_nueva)

	git checkout -b rama_nueva 		(idem reemplaza las 2 lineas anteriores)

	git branch 						(me muestra todas las branch existentes en el repositorio)
	git branch -a 					(me lista todas las branch tanto locales, como remotas)

	git branch -d rama2 			(borro la rama2)

si quiero ver las diferencias entre rama_nueva y master
	git diff rama_nueva 		creo que tengo que pasarme a la rama master ??

ahora le voy a agregar la branch nueva a mi repositorio remoto
	git push origin rama_nueva

si ahora quiero unir mi rama_nueva a mi master:
	git checkout master 		vuelvo a posicionarme en el master
	git pull origin master 		para descargar la ultima version del master
	git merge rama_nueva 		unimos la rama_nueva a la master
	git push origin master		para subir el merge al remoto

por error hice un commit a la rama principal
	git branch rama_pruebas							(creo una nueva branch)
	git reset HEAD~ --hard 							(elimino commit, actualizo stagin y working)
	git checkout rama_pruebas						(cambio a la branch nueva)
	git commit -m "ahora estoy en la rama_pruebas"	

cambiar el nombre del branch creado anteriormente
	git branch -m rama_pruebas rama_otro_nombre

borrar el nombre de una rama que ya se envio al remoto
	git push origin --delete rama_pruebas

si hay conflicto, tengo que establecer la union de forma manual, en el editor de texto.
borro los comentarios y luego elijo que codigo es el que queda. luego cuando ya tengo resuelto el codigo, 
hago un add y un commit, y ya resolvi el merge en forma manual, puedo hacer merge, pero me va a decir que no es 
necesario porque ya grabe los cambios manualmente, asi que puedo borrar la rama

	git push origin delete rama_nueva 		borro la branch en el repo remoto

	git branch -d rama_nueva 				si quiero borrarlo de mi repositorio local

============================ MODIFICAR y BORRAR ARCHIVOS =================================================================

modificamos codigo, esta en el woking directory pero queremos volver a la version del repositorio nuevamente
	git checkout <file> 		el git status me lo mostraba en rojo y luego del checkout desaparece
	git checkout . 				para todos los archivos.

queremos sacar algo que tenemos en el stagin
	git reset <file> 		me lo saca del stagin y me lo deja en rojo
	git reset 				me saca todo lo del stagin?

modificando archivos que ya estaba en un commit
primero modificamos y mandamos el archivo al stagin,
	git add <file> 			agregamos al stagin area
	git commit --amend 		abre Vim, y ahi podemos modificar el texto de commit, y va a commitear lo que esta en el stagin
							se sobre-escribe el commit y se cambia el hash
	git log --stat 			muestra los archivos que fueron modificados en cada commit

git mv <file> <file_renamed> (cuando quiero cambiar el nombre de un archivo ya en el repositorio y quiero
							  dejar en el commit que cambio el nombre. y luego hacer un git commit)

git rm <file> 			(borra el archivo dell repositorio, y lo manda al stagin)
git rm --cached <file> 	(borra el archivo de control de versiones, pero lo conserva en el local)

sacar un archivo luego de que hice el commit
	git reset --soft HEAD~1
	git reset <file>
	rm <file>
	git commit -m "ya saque el archivo"

volver un archivo al working, de un commit anterior
	git checkout HEAD <file>  
	git checkout -- <file>
luego agregar con add y hacer un commit para que se guarden los cambios

	git rm texto.txt 	eliminas el archivo del proximo commit, cuando hagas el nuevo commit, 
						desaparecera de tu working
	git rm --cached texto.txt 	te lo deja en el working pero no lo rastrea mas. 
								Es como incluirlo en el .gitignore
	git mv texto.txt te.txt 	renombrar archivo								

============================ MOVERSE ENTRE COMMITS o BORRAR ================================================================

https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado							

modificamos solo el texto dell commit:
	git commit --amend -m "Texto modificado"

deshace todos los cambios despues dell commit especificado
	git reset <hash_commit>

	git reset HEAD~1 					me borra solo el ultimo commit, y vuelve al ante-ultimo
	git reset HEAD@{dfa27a2} 			me lleva hasta el commit del hash

	git reset --soft a458de44765ef 		borra el commit, actualiza head, no actualiza stagin, no actualiza working
	git reset a458de44765ef   			borra el commit, actualiza head, si actualiza stagin, no actualiza working
	git reset --hard a458de44765ef 		borra el commit, actualiza head, si actualiza stagin, si actualiza working

	git reflog 			un log mas completo, muestra los amend, reset, etc						nos muestra los commits, los amend, y los movimientos entre ramas

volver el archivo a cualquier commit especifico
	git log --oneline				listamos los commits para ver su hash
	git checkout 55df4c2 <file>		movemos al working como estaba ese archivo en ese commit

si queremos llevar a todos los archivos al working, como estaban en un determinado commit:
	git checkout 55df4c2

hicimos un commit en la master, pero queriamos hacerlo en la branch ramma_nueva. Asi lo pasamos:
	git checkout rama_nueva 				nos pasamos a la rama que no tenia el commit, al que lo queremos poner
	git cherry-pick <hash_del_commit> 		copiamos el commit de master a rama_nueva
	git checkout master 					nos pasamos a la master

============================ TAGs ======================================================================================

	git tag version 1.0			creo una etiqueta
	git tag						muestro el nombre de la etiqueta actual
	git tag -d version 1.0		borro etiqueta

	git tag -a v1.0 -m "version mejorada"		me da mas opcion para escribir detalles

si quiero poner una etiqueta a un commit anterior, hago un log, copio el hash
	git tag -a v0.1 <hash_commit> -m "version inicia" 

============================= GITHUB ======================================================================================
CREACION y SUBIDA:

Si tengo un repositorio en mi compu y lo quiero subir. En GitHub creamos el repositorio. 
Tienen que haber un commit antes de poder subirlos a la web. Copiamos la url
En mi compu, en la carpeta donde esta el .git, abro consola y ejecutamos:
	git remote add origin url 			esto crea el link entre mi compu y GitHub
	git push origin master 				subimos el repositorio a GitHub, me va a pedir claves de GitHub
	git push -u origin master 			otra forma pero con -u hacemos que luego solo tengamos que escribir "git push" solamente

si queremos subir una branch nueva, tenemos que:
	git push origin nueva_rama 			puedo verificar en GitHub que ya tengo las 2 ramas subida, con sus respectivos commits

verificar si tambien tengo que subir manualmente los tags con:
	git push --tags

DESCARGA o ACTUALIZACION:

si quiero bajar un repositorio en otra compu, o bajarlo a mi compu porque lo borre, abro consola donde quiero volcar el repo.
en GitHub vamos a < > Code, boton verde Code, en el repo que queremos clonar, y copiamos en el portapapeles el url:
	git clone url

si ya lo teniamos en el working directory (.git) pero fue modificado en el remoto, traemos solo las modificaciones con 
respecto al repositorio que tenemos en nuestra compu con:
	git pull url
	git pull origin master
	git fetch url 				es como un pull, pero con este comando luego hay que hacer un merge a master

una vez tengamos todos los cambios que necesitabamos, lo subimos al remoto con el comando:
	git push origin master

EN LA WEB:
aca GitHubb me da la opcion de hacer un pull request, si trabajo con mas gente, o un merge ahi mismo en la web.
me da la opcion de mergear la rama con el master, y guardar los cambios. Asi la proxima vez que baje la master, ya
estaran mergeados los cambios y commits, de la rama_nueva

dentro de GitHub, podemos ver los commits:
 <> 		ver como estaba el reposiorio en ese momento
 <hash> 	ver los cambios en cada archivo, los muestra en paralelo

el FORK es para copiar un repositorio de otra persona a mis proyectos, lo puedo corregir, o hasta generar un pull request
para el autor. Es para tener una copia y poder modificarla a nuestro gusto

============================== FLUJO DE TRABAJO ============================================================================

trabajamos en un poyecto en una empresa, y tenemos nuetro codigo en casa, para continuar trabajando con el grupo:

	git checkout master 					me paro en la master dell proyecto
	git pull origin master 					bajo la ultima version dell repositorio
	git branch mi_rama_de_trabajo 			creo mi branch de trabajo para trabajar el codigo y no tocar la master
	git add -A 								una vez que modifique mi codigo, agrego al stagin area
	git commit -m "Agregue mi codigo" 		lo grabo en mi repositorio
	git push origin mi_rama_de_trabajo 		subo mi rama modificada a la web, para que alguien la apruebe y la mergee

===============================	CONSOLA ===================================================================================

ls = lista directorio actual
ls -alh = lista directorio actual, hasta los ocultos

pwd = ver en que directorio estamos parados

clear = limpia la pantalla

cat > texto.txt crea el archivo y lo edito, con CTR+D salgo del archivo. Sobreescribe si ya existe

cat texto.txt lee el archivo, no edita

vim text.txt edita texto. i insert texto  ESC :wq (graba y exit) :q! o ZZ (exit sin guardar) 
nano text.txt

rm text.txt 	borra el archivo