##Introducción

 Las "expresiones regulares", también conocidas por la contracción "regexps" (del inglés "regular expresions") son un sofisticado método de descripción (y de búsqueda y manipulación) de cadenas de texto. Son un estándar POSIX (aunque hay ciertas variaciones) que existe en cualquier lenguaje de programación decente y son una de las herramientas mas poderosas para manejar cadenas.

Pueden parecer un tanto áridas y extrañas al principio, pero seguramente acabarán haciéndose imprescindibles para tí. 

##El módulo re

Naturalmente, Python también tiene su propia aproximación a las expresiones regulares, y esta es por medio del módulo re (del inglés "Regular Expresions", también).

"re" es un módulo que provee a Python de una serie de funciones, clases y métodos para manejar cadenas por medio de expresiones regulares. Viene incluído por defecto en cualquier instalación de Python, por lo que no requiere de ninguna clase de preparativo especial antes de poder ser usado.

Antes de empezar a hablar de ello, veamos un pequeño ejemplo que nos servirá para, cambiando sus datos, ir probando los ejemplos que veamos a lo largo de este tema:


```
#!/usr/bin/python

# -*-coding: utf-8 -*-

import re

patron= "mancha"

cadena="En un lugar de la mancha de cuyo nombre no quiero acordarme"

if re.search(patron, cadena):

print "Lo encontré, que cosas"

else:

print "No aparece"

```

En este simple ejemplo estamos usando el método search para buscar un patrón (mancha) en una cadena (En un lugar de la mancha de cuyo nombre no quiero acordarme). No es muy sofisticado, y simplemente nos dice si aparece o no, pero nos servirá para ir empezando. Puedes (y deberías) probar a cambiar el patrón y/o la cadena para ver qué resultado te da.

En realidad, como veremos más adelante, el método search retorna un objeto MatchObject, que permite, entre otras cosas, ver cuántas apariciones de qué cadenas se han encontrado en qué posiciones, etc. Afortunadamente, el valor booleano de de este objeto es "true", con lo que también se puede usar en instrucciones más simples como la de arriba, que por ahora nos vale.

Para entender realmente los ejemplos que vamos a ir viendo deberías comprobarlos con este simple código, e incluso sería buena idea introducir tus propias variaciones. 


##Comodines


Los "comodines" son caracteres o grupos de estos que tienen una interpretación especial que sustituye a otros caracteres. Del mismo modo que un comodín de la baraja puede reemplazar a un As de corazones o un siete de picas, estos comodines se pueden interpretar como otros caracteres o grupos de estos.

Veamoslo con el más básico de los comodines:

**Punto "."**

El punto (.) reemplaza a un carácter cualquiera. De este modo, una búsqueda de la cadena "Pe.a", coincidirá con "Peta", "Pela" "Pesa", "PeÑa", "Pe-a", "Pe.a"...

La expresión que usamos para reemplazar o buscar cadenas se suele llamar el "patrón", y así lo haremos en adelante. De este modo, en el ejemplo anterior, "Pe.a" es el patrón que hemos usado para que coincida con todas esas cadenas.

Fíjate que no es necesario que sean caracteres alfanuméricos (admite también signos de puntuación y, en general, cualquier carácter) y que, evidentemente, también coincide con el propio signo ".". El único carácter con el que no coincide con "." (e incluso esto puede configurarse de otro modo con el uso del flag re.DOTALL) es con el "retorno de carro" o "nueva línea" (el clásico "\n").

Para poder poner en tu expresión regular un punto y que signifique sólo un punto y no otra cosa, hay que "escapar" el carácter anteponiéndole la barra "\". De este modo, la expresión "Pe\.a" sólo coincidiría con "Pe.a".


```
#!/usr/bin/python

# -*- coding: utf-8 -*-

import re

patron = "r.ar.e\."

cadena= "En un lugar de la mancha de cuyo nombre no quiero acordarme."

if re.search(patron, cadena):

print "Lo encontré, que cosas"

else:

print "No aparece"

```


¿Y si lo que buscamos es la propia cadena "Pe\.a"? ¿Qué patrón debemos usar?

Para ello, de nuevo, debemos usar el carácter de escape "\", esta vez delante de la propia "\", para obtener algo así: "Pe\\\.a".

Nota que hay tres barras. La primera es para escapar la segunda, y la tercera es para escapar el punto (si sólo hubiésemos puesto dos, el punto se interpretaría como un comodín, tal como hemos visto arriba).

Sí, en ocasiones pueden acumularse montones de barras de escape.

**Nueva línea "\n".**

Cuando pulsas la tecla "Enter" o "Intro" para pasar a la línea siguiente, eso es un carácter de nueva línea. Como en casi todos los lenguajes y codificaciones, se representa mediante el código "\n".

**"^" y "$", principio y fin de línea.**

Otros dos caracteres especiales muy útiles son "^" y "$", que indican, respectivamente, el principio y el fin de una línea.

Por ejemplo, si en el código de arriba buscas el patrón "^acordarme", no aparecerá (porque encontraría la palabra "acordarme" sólo en el caso de que esté al principio de línea). Sin embargo, el patrón "acordarme$" (que busca la palabra acordarme" al final de la línea), sí dará un resultado.

En realidad, estos caracteres indican el principio o final de la variable. Para que realmente funcionen identificando todas las apariciones cuando hay varias líneas, hay que usar el flag "MULTILINE", que no es más que una constante predefinida en el módulo re, que indica qué tipo de comportamiento deben tener algunos de sus métodos.

Para hacer esto en nuestro ejemplo, cambiaríamos la llamada a search de este modo: "re.search(patron, cadena, re.MULTILINE):" (también se puede poner "re.M" en lugar de "re.MULTILINE", pero es mucho menos descriptivo).

De este modo, ya podemos hacer cosas como esta:


```
#!/usr/bin/python

# -*- coding: utf-8 -*-

import re

patron = "mancha$"

cadena= "En un lugar de la mancha\n de cuyo nombre no quiero acordarme"

if re.search(patron, cadena, re.M):

print "Lo encontre, que cosas"

else:

print "No aparece"

```


Y, ya que estamos en ello, para que los caracteres unicode no nos den problemas en caso de que los estemos usando, es necesario usar el flag re.UNICODE.

**Dígitos "\d" y "\D"**

El comodín \d sustituye a cualquier dígito, y "\D" a cualquier cosa que no lo sea (letras, espacios, puntuación...).

**Espacios "\s" y "\S"**

El comodín "\s" identifica a cualquier carácter que implique un espacio. Esto incluye al espacio propiamente dicho, al tabulador, retorno de carro... El comodín "\S" es su opuesto.

**Alfanumérico "\w" y "\W"**

"\w" identifica caracteres alfanuméricos. Estos son las letras (mayúsculas y minúsculas), los números y el guión bajo "_". "\W" identificará los caracteres no alfanuméricos.

**Corchetes “[]”**

Por si esto fuera poco, los corchetes "[]" se usan para crear listas de caracteres. Si, por ejemplo, queremos que coincidan los números pares del 2 al 8, pondremos [2468]. De este modo, "a[bc]d" coincidirá tanto con "abd" como con "acd". En los corchetes pueden definirse secuencias separando el primer y el último elementos con un guión (-), como "[0-9]" para los números o "[a-h]" para las letras de la "a" a la "h". Pueden agruparse varas secuencias, de modo que [a-zA-Z] coincidirá con una letra mayúscula o minúscula.Dentro de unos corchetes se puede usar el símbolo "^" para indicar el conjunto opuesto al descrito. Por ejemplo, [^a-z] se referirá a cualquier carácter que no sea una letra minúscula.

##Caracteres especiales

Además de los comodines que vimos en el tema anterior, hay otras herramientas que permiten modificar o afinar su utilidad, y que son las que le dan verdadera potencia.

**Más “+”**

Para empezar, el signo + detrás de un carácter hace que en el patrón coincidan ese carácter repetido una o más veces.

Por ejemplo, el patrón "jo+" encontrará las cadenas "jo", "joo", "jooo", etc. El patron "pa+c" coincidirá con "pac", "paac", "paaac"...

Del mismo modo, si queremos que el patrón coincida con cero, una o más apariciones, usaremos "*". Así, "ab*c" coincidirá con "ac", "abc", "abbc" "abbbc"...

Y, si sólo buscamos cero o una apariciones, tenemos "?". En este caso, "ab?c" coincidirá con "ac" y "abc", pero no con "abbc".

**Llaves “{}”**

Si esto no es suficiente y necesitas más precisión, seguimos teniendo opciones.

"{n}" (donde n es un número), indica que buscamos n repeticiones del carácter que le precede. De este modo, "ab{3}c" es lo mismo que "abbbc",

Para tener algo más de margen, tenemos "{m,n}", que nos indica que buscamos un mínimo de m repeticiones y un máximo de n.

**Paréntesis “()”**

Hasta ahora, hemos aplicado estos modificadores a caracteres, pero también se pueden usar con cadenas completas encerrando estas entre paréntesis "()".

Por ejemplo, el patrón "ba(na)+" encontrará "bana", "banana", "bananana"...

**Barra “|”**

Se puede usar el signo | para separar opciones, de tal modo que "digo (hola|mundo)" coincidirá tanto con la cadena "digo hola" como con "digo mundo".

Naturalmente, todo esto se puede combinar para hacer cosas más complejas e interesantes. Por ejemplo, hagamos una expresión que reconozca números de DNI:

"^\d{8}[ -]?[a-zA-Z]$"

Con lo visto hasta ahora deberías poder justificar ese patrón. Al principio es un poco complicado de leer, pero parémonos a examinarla detenidamente. El DNI consta de un número de ocho dígitos y una letra. La letra, que puede ser mayúscula o minúscula, puede seguir al número directamente o estar separada por un espacio o un guión.Con el símbolo "^" al principio indicamos que queremos que la coincidencia coincida con el principio de la cadena, y con "$" al final hacemos que también coincida con el final. De este modo, buscamos que coincida la cadena completa, no una subcadena dentro de esta.

*Algunos ejemplos más:*

Número de teléfono: Tres grupos de tres dígitos separados (o no) por guiones:

"^[0-9]{3}-?[0-9]{3}-?[0-9]{3}$"

Nota que esto es lo mismo que escribir:

"^\d{3}-?\d{3}-?\d{3}$"

Si queremos un número de móvil (que vamos a suponer -erróneamente- que son los que empiezan por 6):

"^6[0-9]{2}-?[0-9]{3}-?[0-9]{3}$"

Una primera aproximación para identificar un correo electrónico "nombre@dominio.com" sería la siguiente:

"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z0-9_\-\.]{1,3})$"

Y para identificar hora y minutos, en formato "21:34":

"^[0-2]\d:[0-6]\d$"

##Tabla de patrones.

Como referencia rápida tenemos:

[https://help.libreoffice.org/Common/List_of_Regular_Expressions/es](https://help.libreoffice.org/Common/List_of_Regular_Expressions/es)

##Instalando Regular Expressions Tester

Podemos obtener un complemento de Firefox para probar nuestras expresiones regulares:  
[![Alt text for your video](https://i1.ytimg.com/vi/R1g2SHJGUpc/2.jpg?time=1401275224819)](http://youtu.be/R1g2SHJGUpc)

http://youtu.be/R1g2SHJGUpc

Veamos un ejemplo para cambiar la etiqueta h1 por h2  
[![Alt text for your video](https://i1.ytimg.com/vi/1H123xAwCw4/2.jpg?time=1401275129775)](http://youtu.be/1H123xAwCw4)

http://youtu.be/1H123xAwCw4


