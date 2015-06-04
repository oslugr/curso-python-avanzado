##Ejecutar sentencias SQL

Como hemos visto al hablar de SQL, una sentencia puede retornar un montón de campos de muchos registros. Para poder manipular estos, usamos una estructura intermedia llamada "Cursor". El cursor recoge los datos devueltos por la base de datos y los almacena de modo que puedan ser recogidos por nuestro programa.

Para ello, usamos el método "cursor" del objeto "Connection" de este modo:

<script src="https://gist.github.com/psicobyte/a07651c4fc13cb868dc1.js"></script>

Con esto creamos un objeto Cursor que, esta vez sí, ya podemos usar para enviar órdenes a la base de datos y recoger sus resultados.

Por ejemplo, es hora de introducir algún dato, usando el método execute:

<script src="https://gist.github.com/psicobyte/2267bf0635515143a9c5.js"></script>

Con esto, introducimos en la tabla "Victimas" un nuevo registro con los valores indicados.

Nota que hemos escapado las comillas interiores con "\". Otra opción es alternar el uso de comillas dobles y simples.

En realidad, es mucho más práctico guardar la sentencia SQL en una variable y usarla luego en el cursor, de un modo similar a este:

<script src="https://gist.github.com/psicobyte/58c469d8ea91014a62ff.js"></script>

Del mismo modo, podemos usarlo para leer registros. Por ejemplo:

<script src="https://gist.github.com/psicobyte/b703f1b60cd3a3177f02.js"></script>

Esto recogerá el campo Nombre de los registros que coincidan con la clausula WHERE (en nuestro caso, uno solo). Pero ¿Cómo accedemos a ellos?

Para ello tenemos fetchone, que sitúa un puntero en la lista de registros y nos retorna el primero de ellos, pasando dicho puntero al siguiente, y así sucesivamente mientras queden registros.

<script src="https://gist.github.com/psicobyte/7f207a9190c7272cf042.js"></script>

De este modo, cada vez que llamemos a fetchone nos retormara un registro de la tabla. En caso de que no queden registros, fetchone retorna un valor falso, con lo que es trivial usarlo dentro de una estructura while o similar para ir tomando registros mientras existan.

En caso de que sea necesario, el número de registros obtenidos (o insertados, si se trataba de un INSERT, o borrados, si era un DELETE...) puede obtenerse con la propiedad rowcount de la clase cursor, de este modo:

<script src="https://gist.github.com/psicobyte/276952096026f6a1acd0.js"></script>

Vamos a practicar todo esto en un solo script:

<script src="https://gist.github.com/psicobyte/de5d0fa0c91f2ca6d8a0.js"></script>

Puedes (y deberías) editar el código y hacer distintas pruebas para ver por ti mismo su funcionamiento. Como ves, el resultado de nuestro select (que es lo que imprime el programa) es una tupla que puede ser almacenada como convenga o ser recorrida por un bucle para ir recogiendo los datos y usarlos para lo que sea. 
