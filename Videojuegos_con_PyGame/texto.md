##Texto

Mostrar texto es muy parecido a mostar imágenes (de hecho, como veremos, mostar texto **es** mostar imágenes) si tenemos en cuenta una serie de detalles muy simples.

Antes de poder escribir nada necesitamos cargar las fuentes (tipografías) que vayamos a usar. Estas deben estar en formato *True Type* (*.ttf), y para ello se usa `Font()` del siguiente modo:

```
MiFuente = pygame.font.Font("ruta/al/archivo/de/fuente", Tamaño)
```

La "ruta/al/archivo/de/fuente" es la ubicación del archivo ttf, y "Tamaño" es la altura en pixels de los caractéres que queremos usar para nuestro texto. 

Pygame nos da la opción de usar **None** en lugar de la ruta al archivo de tipografía. En ese caso, se usará la fuente por defecto.

Una vez hecho esto, para escribir un texto debemos usar el método `render()` de la fuente que hemos cargado del sugiente modo:

```
Texto = MiFuente.render("Texto a mostrar", Antialias, Color)
```

Donde "Texto a mostrar" es eso mismo, el texto a mostrar. En Antialias indicaremos un 1 si queremos usar antialias (difuminado de bordes, [consuta aquí para más detalles](http://es.wikipedia.org/wiki/Antialiasing)) o un 0 si no queremos usarlo.

En Color indicaremos el color que vamos a usar. Hay varias formas de hacer esto (ver el [objeto color de pygame](http://www.pygame.org/docs/ref/color.html)) pero la forma más simple es indicar sus componestes RGB (Rojo, Verde, Azul) con una tupla.

Esto creará en "Texto" una imagen (objeto surface) que usaremos como cualquier otra imagen y que tendremos que ubicar haciendo blit (pues eso, como cualquier otra imagen).

Un problema de Pygame es que no nos permite renderizar textos de varias líneas (no reconoce el caracter *\\n*). Debemos cortar y situar el texto nostros mismos.

> Al proceso de convertir algún tipo de información (en este caso una cadena de texto) a una imagen se le suele llamar "renderizar" (del inglés "render").

Veamos un ejemplo en acción:

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos la librería
import pygame

import sys

# Importamos constantes locales de pygame
from pygame.locals import *

# Iniciamos Pygame
pygame.init()

# Creamos una surface (la ventana de juego), asignándole un alto y un ancho
Ventana = pygame.display.set_mode((600, 400))

# Le ponemos un título a la ventana
pygame.display.set_caption("Hola. Pulsa Escape para salir")

# Elegimos la fuente y el tamaño
Fuente= pygame.font.Font(None, 40)

# Renderizamos (convertimos a imagen) el mensaje con la fuente definida
Mensaje = Fuente.render("Esto es un texto para ver lo que sale", 0, (0,0,255))

# Bucle infinito para mantener el programa en ejecución
while True:

    Ventana.blit(Mensaje, (5, 5))
    pygame.display.flip()
    # Manejador de eventos
    for evento in pygame.event.get():
        # Pulsación de la tecla escape
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                sys.exit()
```

> Fíjate que, una vez renderizado el texto con `render`, lo que obtenemos es una surface con la que podemos hacer exactamente las mismas cosas que con cualquier otra surface. 

Además de lo que hemos visto, el [módulo `font` de pygame](www.pygame.org/docs/ref/font.html) nos aporta algunas otras herramientas para manipular fuentes.
