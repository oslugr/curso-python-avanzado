##DictCursor

Las tres formas de acceder a los datos que hemos visto nos retornan los propios datos, pero no nos dan información de a qué campo se corresponde cada uno de ellos. En principio esto no es necesario porque, después de todo, se los estamos pidiendo nosotros en el SELECT. Pero sí que habrá muchas circunstancias en las que nos interese conservar esa información de a qué campo se corresponde cada uno de los datos recibidos.

Afortunadamente tenemos DictCursor, una herramienta que nos permitirá precisamente eso:

```
micursor = Conexion.cursor(MySQLdb.cursors.DictCursor) 
```

DictCursor es, en realidad, una subclase de cursor y, por tanto, se usa y se comporta como vimos que hacía Cursor, con la diferencia de que, en lugar de retornar una tupla de datos retorna un diccionario.

Lo veremos más claro con un ejemplo:

```
#!/usr/python

# -*- coding: utf-8 -*-

import MySQLdb

# Establecemos la conexión

Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan')

# Creamos el cursor, pero especificando que sea de la subclase DictCursor

micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)

# Insertamos un par de registros

query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (1, \"Ejercito de Zombies\",\"Muertos Vivientes\",\"Desmembramiento a espada\");"

micursor.execute(query)

query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (2, \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");"

micursor.execute(query)

# Ahora vamos a hacer un SELECT

query= "SELECT * FROM Victimas WHERE 1;"

micursor.execute(query)

# Obtenemos el resultado con fetchall

registros= micursor.fetchall()

for registro in registros:

# ... imprimimos el registro...

print registro["Nombre"] + " es del tipo " + registro["Profesion"]

# Esto que sigue es para borrar el contenido de la base de datos,
# y que no se nos acumule al ir haciendo pruebas

query= "DELETE FROM Victimas WHERE 1;"

micursor.execute(query)
```


##Cerrar cursores

Cuando se ha acabado de trabajar con un cursor, este se debería cerrar con la orden close, de este modo.

```
micursor.close () 
```

La conexión también se cierra a acabar con ella:

```
Conexion.close () 
```

Si estamos trabajando con bases de datos transaccionales, es importante asegurarse de haber hecho el commit antes de cerrar la conexión. 
