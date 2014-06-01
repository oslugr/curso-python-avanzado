##Más allá de fetchnote

Cuando se van a recibir unos pocos registros fetchone cumple su labor perfectamente pero, si se van a recibir muchos registros, es mejor cargar estos de una sola vez en una estructura más manejable y manipularlos por nosotros mismos.

Esto es fácil de conseguir con el método fetchall.

fetchall se comporta como el anterior, pero, en lugar de retornar una tupla conteniendo un registro, lo que retorna es un array de ellas con todos los registros retornados.

Naturalmente, esto puede ser una locura en bases de datos grandes, en las que es más que normal recibir cientos de miles de registros en una petición.

Una solución intermedia a recogerlos uno a uno (fetchone) o recogerlos todos (fetchall) es recogerlos por grupos. Para ello tenemos fetchmany.

fetchmany admite un parámetro numérico que indica cuántos registros recogerá, de este modo:

```
registros= micursor.fetchmany(10) 
```

En este ejemplo, el método retorna un array de tuplas (igual que hacía fetchall), pero con un límite máximo de 10 (que es el número que le hemos indicado). Además, al igual que vimos que hacía fetchone, mantiene un puntero interno que indica por qué registro va, de modo que, en la siguiente llamada, seguirá por el registro siguiente al último que hubiese retornado antes.

Vamos a verlo con un ejemplo un poco más práctico:

```
#!/usr/python

# -*- coding: utf-8 -*-

import MySQLdb

# Establecemos la conexión

Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan')

# Creamos el cursor

micursor = Conexion.cursor()

# Insertamos algunos registros (de forma cutre e ineficiente) para tener con qué trabajar

query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (1, \"Ejercito de Zombies\",\"Muertos Vivientes\",\"Desmembramiento a espada\");"

micursor.execute(query)

query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (2, \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");"

micursor.execute(query)

query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (3, \"Bestia del Pantano\",\"Monstruo\",\"Destripado\");"

micursor.execute(query)

query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (4, \"Serpiente\",\"Monstruo\",\"Destripado\");"

micursor.execute(query)

query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (5, \"Scerdote maligno\",\"Monstruo\",\"Desmembramiento a espada\");"

micursor.execute(query)

# Hacemos un commit, por si las moscas

Conexion.commit()

# Ahora vamos a hacer un SELECT

query= "SELECT * FROM Victimas WHERE 1;"

micursor.execute(query)

# Obtenemos el resultado con fetchmany

registros= micursor.fetchmany(2)

# para cada lista retornada (de 2 registros)

while (registros):

# recorremos la lista...

for registro in registros:

# ... mprimimos el registro...

print registro

# ...y recargamos los registros dentro del bucle, si quedan

registros= micursor.fetchmany(2)

# Esto que sigue es para borrar el contenido de la base de datos,
# y que no se nos acumule al ir haciendo pruebas

query= "DELETE FROM Victimas WHERE 1;"

micursor.execute(query)
```

Es cierto que el ejemplo de arriba no es un código precisamente muy optimizado, pero creo que sirve perfectamente para ver el funcionamiento de fetchmany y, por tanto, el de fetchone y fetchall (dado que, en realidad, estos dos son más simples). 
