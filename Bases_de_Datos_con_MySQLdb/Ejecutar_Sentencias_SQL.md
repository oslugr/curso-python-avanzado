##Ejecutar sentencias SQL

Como hemos visto al hablar de SQL, una sentencia puede retornar un montón de campos de muchos registros. Para poder manipular estos, usamos una estructura intermedia llamada "Cursor". El cursor recoge los datos devueltos por la base de datos y los almacena de modo que puedan ser recogidos por nuestro programa.

Para ello, usamos el método "cursor" del objeto "Connection" de este modo:

```
micursor = Conexion.cursor() 
```

Con esto creamos un objeto Cursor que, esta vez sí, ya podemos usar para enviar órdenes a la base de datos y recoger sus resultados.

Por ejemplo, es hora de introducir algún dato, usando el método execute:

```
micursor.execute("INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (1, \"Ejercito de Zombies\",\"Muertos Vivientes\",\"Desmembramiento a espada\");") 
```

Con esto, introducimos en la tabla "Victimas" un nuevo registro con los valores indicados.

Nota que hemos escapado las comillas interiores con "\". Otra opción es alternar el uso de comillas dobles y simples.

En realidad, es mucho más práctico guardar la sentencia SQL en una variable y usarla luego en el cursor, de un modo similar a este:

```
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (2, \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");"  

micursor.execute(query) 
```

Del mismo modo, podemos usarlo para leer registros. Por ejemplo:

```
query= "SELECT Nombre FROM Victimas WHERE id=1;"  

micursor.execute(query) 
```

Esto recogerá el campo Nombre de los registros que coincidan con la clausula WHERE (en nuestro caso, uno solo). Pero ¿Cómo accedemos a ellos?

Para ello tenemos fetchone, que sitúa un puntero en la lista de registros y nos retorna el primero de ellos, pasando dicho puntero al siguiente, y así sucesivamente mientras queden registros.

```
registro= micursor.fetchone() 
```

De este modo, cada vez que llamemos a fetchone nos retormara un registro de la tabla. En caso de que no queden registros, fetchone retorna un valor falso, con lo que es trivial usarlo dentro de una estructura while o similar para ir tomando registros mientras existan.

En caso de que sea necesario, el número de registros obtenidos (o insertados, si se trataba de un INSERT, o borrados, si era un DELETE...) puede obtenerse con la propiedad rowcount de la clase cursor, de este modo:

```
numero_de_registros= micursor.rowcount 
```

Vamos a practicar todo esto en un solo script:

```
#!/usr/python

# -*- coding: utf-8 -*-

import MySQLdb

# Establecemos la conexión

Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan')

# Creamos el cursor

micursor = Conexion.cursor()

# Ejecutamos un insert directamente

micursor.execute("INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (1, \"Ejercito de Zombies\",\"Muertos Vivientes\",\"Desmembramiento a espada\");")

# Lo mismo, pero por medio de una variable

query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (2, \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");"

micursor.execute(query)

# Hacemos un commit, por si las moscas

Conexion.commit()

# Ahora vamos a hacer un SELECT

query= "SELECT * FROM Victimas WHERE id=1;"

micursor.execute(query)

# Obtenemos el resultado con fetchone

registro= micursor.fetchone()

# Imprimimos el registro resultante

print registro

# Esto que sigue es para borrar el contenido de la base de datos,
# y que no se nos acumule al ir haciendo pruebas

query= "DELETE FROM Victimas WHERE 1;"

micursor.execute(query)
```

Puedes (y deberías) editar el código y hacer distintas pruebas para ver por ti mismo su funcionamiento. Como ves, el resultado de nuestro select (que es lo que imprime el programa) es una tupla que puede ser almacenada como convenga o ser recorrida por un bucle para ir recogiendo los datos y usarlos para lo que sea. 
