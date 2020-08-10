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
	git log --oneline --all --graph --decorate

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

	git remote -v 		(me muestra los remotos que tengo asociados con el repo)
	git remote show origin	(ademas muestra las ramas asociadas a cada rama remota)
	git remote add pablo <url>		(le asigno a mi remoto un nombre, luego puedo hacer git pull pablo master)
	gir remote rm <url>				(borro una direccion de remoto asociada)

============================  BRANCHES  =================================================================================

	git branch rama_nueva 			(creo una rama paralela a master)
	git checkout rama_nueva 		(cambio a rama_nueva, cambio mi working directory a la rama_nueva)

	git checkout -b rama_nueva 		(idem reemplaza los 2 comandos anteriores)

	git branch 						(me muestra todas las branch existentes en el repositorio local)
	git branch -a 					(me lista todas las branch tanto locales, como las ocultas para las remotas)

	git branch -d rama2 			(borro la rama2)

si quiero ver las diferencias entre rama_nueva y master
	git diff rama_nueva 		tengo que estar parado en rama master

ahora le voy a agregar la branch nueva a mi repositorio remoto
	git remote			me fijo el nombre asignado al repo remoto
	git push <origin> <rama_nueva>		puede ocurrir un error, tal vez alguien ya hizo cambios en la rama remota, pro
										lo que no tienes actualizada la ultima version de la rama. Tienes que hacerle un
										fetch, evaluar, hacer un merge, y luego subirla

si ahora quiero unir mi rama_nueva a mi master, y luego subirla al remoto:
la rama_nueva ya esta commiteada y lista para el merge.	
	git checkout master 		vuelvo a posicionarme en el master
	git pull origin master 		para descargar la ultima version del master
	git merge rama_nueva 		unimos la rama_nueva a la master, resolviendo conflictos
	git push origin	master		para subir el merge al remoto

queremos copiar un commit de la master para ponerlo en la branch ramma_nueva:
	git checkout rama_nueva 				nos pasamos a la rama que no tenia el commit, al que lo queremos poner
	git cherry-pick <hash_del_commit> 		copiamos el commit de master a rama_nueva
	
por error hice un commit a la rama principal y tenia que empezar a trabajar en mi rama_pruebas:
	git reset --hard HEAD~1 							elimino commit, actualizo stagin y working
	git checkout rama_pruebas							paso a la rama_pruebas
	git commit -m "ahora estoy en la rama_pruebas"		creo el commit

cambiar el nombre del branch creado anteriormente
	git branch -m rama_pruebas rama_otro_nombre

borrar el nombre de una rama que se esta enviando al remoto
	git push origin --delete rama_pruebas

hago el merge, pero hay conflictos, tengo que establecer la union de forma manual, en el editor de texto.
borro los comentarios y luego elijo que codigo es el que queda. luego cuando ya tengo resuelto el codigo, 
hago un add y un commit dell merge. Lo resolvi de forma manual.

	git push origin delete rama_nueva 		borro la branch en el repo remoto

si en el remoto tenia ramas que se fueron borrando, en el local, sigo viendo esas ramas remotas borradas, solucion:
	git remote update origin
	git branch -a				muestra todas las branch, hasta las ocultas para fetch

quiero traer una rama_1 dell remoto y ponerla en una rama_prueba en mi local:
	git checkout -b rama_prueba origin/rama_1

PULL vs FETCH :
	git fetch origin			esto me trae solo los cambios de remoto, pero no los aplica a mi working tree
								en el mensaje de fetch, te dice las ramas "ocultas" en donde guarda lo que trajo.
										master -> origin/master
										rama_1 -> origin/rama_1
								luego puedes ir a la rama que quieras y hacer una   git diff origin/master 
								y puedes hacer merge por rama o no. Decido que hacer con la info del remoto
								Fetch me trae los cambios de las ramas del remoto tambien.

	git pull origin				me trae lo del remoto, y me actualiza mi woring tree, borra todo lo que tenia
								Pull me trae solo la rama en la que estoy parado, no se nada de las demas ramas.

============================ MODIFICAR y BORRAR ARCHIVOS =================================================================

volvemos el archivo a como estaba en el commit especificado:
	git checkout <file> 			sino especifico commit, me manda el ultimo commit
	git checkout . 					idem para todos los archivos, en el ultimo commit.
	git checkout 55df4c2 <file>		me muestra el archivo en determinado commit
	git checkout 55df4c2			idem para todos los archivos, en dereminado commit

queremos sacar algo que tenemos en el stagin
	git reset <file> 		me lo saca del stagin y me lo deja en rojo
	git reset .				me saca todo lo del stagin

modificando archivos que ya estaba en un commit. Primero modificamos y mandamos el archivo al stagin,
	git add <file> 								agregamos al stagin area
	git commit --amend -m "Texto modificado"	modificamos solo el texto dell commit, y agrega archivos dell stagin

	git log --stat 			muestra los archivos que fueron modificados en cada commit

quiero cambiar el nombre de un archivo dell repo, dejando asentado el cambio con un commit
	git mv <file> <file_renamed> 	
	git commit -m "Cambie el nombre del archivo"

sacar un archivo dell repo, hacido 1 commits:
	git rm <file> 				borra el archivo por completo, manda al stagin el mensaje de borrado, para luego commitear
	git rm --cached <file> 		saca el archivo dell repo, pero lo conserva en la carpeta local, como .gitignore

sacar un archivo luego del ultimo commit
	git reset --soft HEAD~1					vuelvo al anteultimo commit 
	git rm -f <file>						fuerzo el borrado de <file>
	git commit -m "ya saque el archivo"		

============================ MOVERSE ENTRE COMMITS o BORRAR ================================================================

https://git-scm.com/book/es/v2/Herramientas-de-Git-Reiniciar-Desmitificado							

deshace todos los cambios despues dell commit especificado

	git reset HEAD~1 					me borra solo el ultimo commit, y vuelve al ante-ultimo
	git reset HEAD@{dfa27a2} 			??

										working		stagin		
	git reset --soft a458de44765ef 		    X		  X	            
	git reset a458de44765ef   				X		  SI
	git reset --hard a458de44765ef 		    SI        SI

	git reflog 			un log mas completo, muestra los amend, movimiento en ramas, etc	

============================ TAGs ======================================================================================

	git tag version 1.0			creo una etiqueta simple
	git tag -a v1.0 -m "version mejorada"		son etiquetas anotadas, me da opcion de ver un texto asociado
	
	git tag						muestro el nombre de las etiquetas dell proyecto
	git show <tag>				muestra el commit asociado a la etiqueta si es una simple
								muestra commit y descripcion de la etiqueta si es una de tipo anotadas

	git tag -d version 1.0		borro etiqueta, creo que la mueve a otra rama, no se

las etiquetas no se suben al remoto, salvo que lo hagas de forma manual:
	git push origin <tag>		si es una etiqueta especifica
	git push origin --tags 		si son todas las etiquetas dell proyecto

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
	git pull url			un pull modifica tanto el repositorio como el working. Si estabas modificando codigo ya creado,
	git pull origin master		es sobreescrito por lo que viene del pull.
	git fetch origin 		es como un pull, pero coloca los archivos en una rama oculta llamada origin/master
							por lo que luego hay que hacer un merge con master. Sirve si quiero tener mi repositorio
							actualizado del remoto, pero no quiero tocar mi working o mi rama master

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

============================== VS CODE - GIT - GITHUB ==================================================================

subir codigo a github:
1_ tener el codigo en el working, ya con un commit
2_ crear el repositorio en github y copiar la url
3_ en VS en ... poner push, y me pide la url dell repo en github y un nombre(no se para que)
4_ en VS click en la nube con flechita (abajo izq), o en los ... poner push otra vez.
5_ ya esta subido a github

actualizar codigo de master a remoto:
1_ hacemos el commit
2_ abajo a la izq ponemos la flecha hacia arriba o en ... pull y listo

actualizar codigo de remoto a master:
1_ en los ... hacemos un pull

clonar un remoto:
1_ abrir una carpeta nueva, un proyecto nuevo. En la parte Source control (git), elegir clonar repositorio
2_ o en Command Pallete, ponemos clone, ponemos url y elegimos carpeta para guardar el repo local

extension Git Lens:
en el codigo, me permite ver en cada linea, si esta en stage, el commit asociado, el autor, fecha, etc 
en el sidebar, me muestra, los cambios de la linea, los commits asociados al archivo, puedo
ver como estaba el archivo en cada commit, traerlo al area de trabajo, copiar el hash, ver los tags, ver los 
remotos asociados, autores, ramas, push, pulls, etc

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

touch <file_name>		crea un archivo vacio

pwd = ver en que directorio estamos parados

clear = limpia la pantalla

cat > texto.txt crea el archivo y lo edito, con CTR+D salgo del archivo. Sobreescribe si ya existe

cat texto.txt lee el archivo, no edita

vim text.txt edita texto. i insert texto  ESC :wq (graba y exit) :q! o ZZ (exit sin guardar) 
nano text.txt

rm text.txt 	borra el archivo