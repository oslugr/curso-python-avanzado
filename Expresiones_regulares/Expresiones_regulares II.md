##Funciones

En el anterior tema hemos visto un montón de teoría sobre expresiones regulares y un pequeño ejemplo del módulo re por medio de search. Ahora vamos a ver algunas funciones que nos puedan servir para encontrar utilidad a lo aprendido:

Empecemos con search, que para algo ya la hemos usado:

re.search(Patrón, Cadena, [flags]) 

search busca en Cadena el Patrón que le indiquemos y, como comentamos entonces, retorna un objeto MatchObject [http://docs.python.org/library/re.html#re.MatchObject] que es el que contiene los datos de nuestra búsqueda y el que realmente usaremos.

Si no encuentra ninguna coincidencia, search retorna un valor booleano "falso".

Otra función muy similar a search es match:

re.match(Patrón, Cadena, [flags]) 


match se comporta igual que search, buscando el Patrón en la Cadena, pero sólo si coincide desde el inicio de Cadena. Más o menos, es un equivalente a hacer un search, pero iniciando el patrón con el carácter "^".

Una herramienta mucho más interesante es split:

re.split(Patrón, Cadena, [max], [flags]) 


split divide Cadena usando Patrón como referencia y retorna un array conteniendo las cadenas resultantes. Con el parámetro opcional max se le indica el número máximo de "trozos" que queremos obtener.

Veamoslo con este ejemplo que divide la cadena que se le proporciona en varias subcadenas numéricas usando cono separadores los caracteres no numéricos:


```
#!/usr/bin/python

# -*- coding: utf-8 -*-

import re

Resultados= re.split("\D", "123a45x6-78.90")

print Resultados

```

Naturalmente, lo complejo del patrón sólo está limitado por tu imaginación y necesidades.

Otra herramienta muy útil es findall:

re.findall(Patrón, Cadena, [max], [flags]) 

Se comporta igual que find pero, en lugar de detenerse en la primera coincidencia, retorna un array que, por ejemplo, permite usar la salida de esta función en un bucle para explorar todas las coincidencias.

Las coincidencias se retornan en el orden en el que aparecen, y no se superponen (Es decir, que los caracteres que pertenezcan a una coincidencia no pueden pertenecer a otra).

Veamos un ejemplo simple:


```
#!/usr/bin/python

# -*- coding: utf-8 -*-

import re

Coincidencias= re.findall(".n", "En un lugar de la Mancha")

print Coincidencias

```

Hasta ahora sólo hemos usado las regexps para encontrar coincidencias, pero otra potente utilidad es la de reemplazar cadenas o partes de estas. Una utilidad para ello es sub:

re.sub(Patrón, Reemplazar, Cadena, [contador], [flags]) 

Esto es algo más complicado, pero fácil de entender. Usamos Patrón para buscar en Cadena y, las coincidencias que encontremos, las reemplazamos por Reemplazar. Si se usa un número en el argumento opcional "contador", sólo se reemplazará ese número de apariciones como máximo, aunque hubiera más coincidencias.

Por ejemplo:


```
#!/usr/bin/python

# -*- coding: utf-8 -*-

import re

Cadena= "En un lugar de la Mancha fea y negra de los piratas"

Resultados= re.sub("a |a$", "as ", Cadena)

print Cadena

print Resultados

```

Igual que antes, las posibilidades de complejidad y sofisticación son ilimitadas

Un detalle interesante de sub es que Reemplazar puede ser una función, en lugar de una cadena. En este caso, la función será llamada a cada coincidencia, se le pasará la cadena encontrada como parámetro y su resultado será lo que se use como cadena para reemplazar.

En los ejemplos anteriores, cada vez que se usa un Patrón, Python tiene que compilar y preparar ese patrón antes de poder usarlo (Esto no es del todo cierto, porque python usa una caché para ello).

En realidad, esto no ocupa demasiados recursos pero, si se va a hacer un uso más o menos intensivo, es mejor compilar la expresión una sola vez y usar el objeto compilado como patrón. Para ello está compile:

re.compile(Patrón, [flags]) 

El resultado de esta función puede usarse como patrón en todas las expresiones que hemos visto antes, en lugar de usar una cadena de texto o una variable conteniéndola. 


##Flags

Ya hemos visto un par de flags que nos servía para cambiar el comportamiento por defecto de las funciones y los métodos del módulo “re”, pero hay algunos más que también resultan muy útiles. Se muestran tanto en la forma larga (y más comprensible) de una palabra y la forma breve, de una letra. Ambas formas de escribirlas tienen exactamente el mismo comportamiento, aunque se recomienda la forma larga, en beneficio de la claridad:


re.UNICODE

re.U

Necesaria para usar caracteres UNICODE (lo que no significa que no vayas a tener problemas con Unicode)


re.MULTILINE

re.M

Hace que "^" y "$" no se aplique sólo al principio y al fin de la cadena respectivamente, sino que se aplique a cada (salto de) línea dentro de ella.


re.IGNORECASE

re.I

Hace que los patrones no distingan mayúsculas de minúsculas


re.DOTALL

re.D

Hace que el comodín "." identifique TAMBIEN al carácter "\n"

Todos ellos tiene una versión larga y descriptiva y otra versión más corta y de significado ligeramente más hermético. En general, es recomendable la primera de ellas, por razones de claridad y legibilidad.


##Clases

El módulo re provee de un par de clases, con sus métodos y atributos correspondientes, para tratar con expresiones regulares en POO. En realidad, su uso y propiedades son prácticamente iguales al visto en el caso de las funciones, pero se enlazan aquí sus descripciones a modo de referencia.

RegexObject

La clase RegexObject es el objeto de uso de las expresiones regulares, y admite métodos equivalentes a las funciones vistas anteriormente (find, match, split, sub)

MatchObject

La clase MatchObject, de la que ya hemos hablado anteriormente, es la que contiene el resultado de operaciones como search o match, y siempre tiene un valor booleano de true.



