##Introducción Mínima a SQL

Los programas (y las personas) que trabajan con bases de datos lo hacen habitualmente a través de un lenguaje estandar llamado SQL. Una sentencia SQL se le transmite al motor de bases de datos y este ejecuta la acción que se le haya ordenado y retorna una estructura de datos en función de ello.

SQL (Structured Query Language - Lenguaje de Consulta Estructurado) es un lenguaje complejo y potente que permite el completo control de bases de datos.

Está implementado en la mayoría de motores de bases de datos y se puede usar, por medio de las librerías o APIs correspondientes, desde la mayoría de lenguajes de programación.

Naturalmente, la enseñanza de SQL es algo que escapa completamente de las pretensiones de este curso, de modo que aquí se mostrarán sólo unas pocas instrucciones muy rudimentarias que permitan a aquellos que no conozcan este leguaje comprender y practicar los ejemplos y ejercicios de este curso.

En realidad, ya hemos tenido un primer contacto con este leguaje al instalar MySQL. Cuando, usando el modo interactivo de MySQL, creamos una base de datos, una tabla y un usuario; lo hicimos usando sentencias MySQL.

De hecho, podríamos haberlos creado desde un programa en python y, si no lo hicimos así fue por no introducir todos los conceptos a la vez y por explicar paso a paso y más claramente cada concepto.

Veamos ahora unas instrucciones básicas de SQL. Naturalmente, todas ellas se podrán aplicar a nuestras propias bases de datos con sólo modificar los nombres de las tablas, campos, etc.

Nota que todas las instrucciones terminan en punto y coma ";".

Para obtener el valor de una serie de campos se usa la sentencia SELECT del siguiente modo:

```
SELECT Campo1, Campo2 FROM Tabla WHERE Campo1="Hola"; 
```

Esto nos devuelve todos los valores de Campo1 y Campo2 de los registros de Tabla para los cuales Campo1 valga "Hola"

Si queremos que nos devuelva todos los campos de cada registro en lugar de pedir unos concretos, podemos usar el asterisco (*) así:

```
SELECT* FROM Tabla WHERE Campo1="Hola"; 
```

Para instertar nuevos registros tenemos la sentencia INSERT, que se usa de este modo:

```
INSERT INTO Tabla (Campo1,Campo2) VALUES ("Valor del Campo 1", "Valor del Campo 2") 
```

La estructura es simple: En cada uno de los campos indicados en el primer paréntesis (separados por comas) de la tabla Tabla se introducen los datos indicados tras VALUES

Para modificar los datos de un registro usamos la sentencia UPDATE:

```
UPDATE Tabla SET Campo1 = "Nuevo valor del Campo 1", Campo2="Nuevo valor del Campo 2" WHERE Campo2 = "Hola"; 
```

Con la que cambiaríamos los valores de Campo1 y Campo2 a los indicados, en todos los registros en los que el Campo2 valga "Hola".

Por último, para borrar registros de una tabla se usa la sentencia DELETE de este modo:

```
DELETE FROM Tabla WHERE id=1; 
```

Que borraría de la tabla Tabla todos los registros para los que el campo id valga 1.

Cuidado: No es lo mismo “...WHERE id=1; ” que “...WHERE 1; ”. La primera sentencia es cierta si el campo id contiene el valor 1, la segunda es cierta SIEMPRE.


##Para introducirse algo más en el mundo de SQL

No sólo hay muchísimas instrucciones más, sino que estas mismas que hemos visto se pueden usar de formas mucho más sofisticadas. Aquí dejamos unos enlaces con los que ahondar algo más en el conocimiento de SQL.

[Página en Wikipedia de SQL](http://es.wikipedia.org/wiki/SQL)

[Tutorial de JJ Merelo sobre SQL](http://geneura.ugr.es/~jmerelo/tutoriales/bd-sql/)
