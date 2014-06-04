##Movimiento

Dado lo que hemos visto en el tema anterior, mover una imagen no es nada complicado: Sólo hay que cambiar sus coordenadas y redibujarla.

Un detalle importante es que no estamos moviendo nada, simplemente estamos volviendo a dibujar el objeto en otra posición ¡Pero no desaparece del lugar donde estaba dibujado antes!

Esto quiere decir que, a cada cilco de nuestro bucle, debemos redibujar el fondo y todos y cada uno de los objetos.

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos la libería
import pygame

import sys

# Importamos constantes locales de pygame
from pygame.locals import *

#Inciamos pygame
pygame.init()

# Creamos un objeto screen (la ventana de juego), asginándole un alto y un ancho
Ventana = pygame.display.set_mode((600, 400))

# Le ponemos untítulo a la ventana
pygame.display.set_caption("Moviendo Imágenes")

# Cargamos las imágenes
Fondo = pygame.image.load("fondo.jpg")
Imagen = pygame.image.load("imagen.png")

coordX = 300
coordY = 200
Coordenadas = (coordX, coordY)

# Bucle infinito para mantener el programa en ejecución
while True:

    Ventana.blit(Fondo, (0, 0))
    Ventana.blit(Imagen, Coordenadas)    
    pygame.display.flip()

    # Manejador de eventos
    for evento in pygame.event.get():
        # Pulsación de la tecla escape
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                sys.exit()

            elif evento.key == pygame.K_RIGHT:
                coordX = coordX + 5
            elif evento.key == pygame.K_DOWN:
                coordY = coordY + 5
            elif evento.key == pygame.K_LEFT:
                coordX = coordX - 5
            elif evento.key == pygame.K_UP:
                coordY = coordY - 5
    Coordenadas = (coordX, coordY)
```

Vale. Nuestro código (que es casi el mismo del tema anterior)está creciendo y empieza a ser lo suficientemente complejo para ir necesitando que estructuremos el código, con sus funciones y sus clases, pero para estos ejemplos nos hace el apaño.

Las únicas diferencias sobre los ejemplos del tema anterior son:

* Hemos definido las coordenadas de Imagen en un par de variables (coordX y coordY), para poder modificarlas cómodamente al recibir la pulsación de la tecla correspondiente
* Hemos añadido el control para las interrupciones de teclado de las teclas de flecha
* Ahora rdibujamos Fondo e Imagen en cada ciclo de nuestro bucle (prueba a sacar ese " Ventana.blit(Fondo, (0, 0))" y ponerlo *antes* de iniciar el bucle)

Un detalle importante es que, como el evento KEYDOWN ocurre al *pulsar* una tecla, Imagen se mueve dando un "paso" cada vez que se pulsa. Si queremos que el movimiento sea contínuo, se puede hacer con un sistema de flags parecido al siguiente:

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos la libería
import pygame

import sys

# Importamos constantes locales de pygame
from pygame.locals import *

#Inciamos pygame
pygame.init()

# Creamos un objeto screen (la ventana de juego), asginándole un alto y un ancho
Ventana = pygame.display.set_mode((600, 400))

# Le ponemos untítulo a la ventana
pygame.display.set_caption("Moviendo Imágenes")

# Cargamos las imágenes
Fondo = pygame.image.load("fondo.jpg")
Imagen = pygame.image.load("imagen.png")

coordX = 300
coordY = 200
Coordenadas = (coordX, coordY)

incrementoX = 0
incrementoY = 0

# Bucle infinito para mantener el programa en ejecución
while True:

    Ventana.blit(Fondo, (0, 0))
    Ventana.blit(Imagen, Coordenadas)    
    pygame.display.flip()

   # Manejador de eventos
    for evento in pygame.event.get():
        # Pulsación de la tecla escape
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                sys.exit()
            elif evento.key == pygame.K_RIGHT:
                incrementoX = 5
            elif evento.key == pygame.K_DOWN:
                incrementoY = 5
            elif evento.key == pygame.K_LEFT:
                incrementoX = -5
            elif evento.key == pygame.K_UP:
                incrementoY = -5
        if evento.type == pygame.KEYUP:
            incrementoX = 0
            incrementoY = 0

    coordX = coordX + incrementoX
    coordY = coordY + incrementoY

    Coordenadas = (coordX, coordY)
```
Bueno, quizás no es mu elegante, pero es sencillo y deberías pararte un momento y verlo detenidamente para asegurarte de que lo entiendes.

Aunque posiblemente aún no nos hayamos dado cuenta, tenemos otro problema.

Dado que incrementamos las coordenadas en una cantidad fija a cada ciclo del bucle, la velocidad resultante depende de la velocidad a la que se complete el ciclo, y esta puede variar dependiendo del procesador, la carg del sistema, lo que esté haciendo nuetro programa en cada ciclo, etc.

¿Hay una forma de asegurarnos que la velocidad es constante indpendientemente de las circunstancias?

Bueno, si el procesador donde se ejecuta es muy lento o la máquia está muy sobrecargada va a ser dificil hacer que vaya más rápido, pero sí podemos limitar la velocidad para que no exceda de cierto nivel.

Para esto (y para más cosas) tenemos la clase de pygame "Clock", que se llama del siguiente modo:

```
Reloj= pygame.time.Clock() 
```

y nos retorna un reloj que podemos usar para muchas cosas, entre las que está establecer un "tic", un tiempo en milisegundos que limita la velocidad a la que se procesa nuestro bucle principal. Por ejemplo:

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos la libería
import pygame

import sys

# Creamos un reloj
Reloj= pygame.time.Clock()


# Importamos constantes locales de pygame
from pygame.locals import *

#Inciamos pygame
pygame.init()

# Creamos un objeto screen (la ventana de juego), asginándole un alto y un ancho
Ventana = pygame.display.set_mode((600, 400))

# Le ponemos untítulo a la ventana
pygame.display.set_caption("Moviendo Imágenes")

# Cargamos las imágenes
Fondo = pygame.image.load("fondo.jpg")
Imagen = pygame.image.load("imagen.png")

coordX = 300
coordY = 200
Coordenadas = (coordX, coordY)

incrementoX = 0
incrementoY = 0

# Bucle infinito para mantener el programa en ejecución
while True:

    Ventana.blit(Fondo, (0, 0))
    Ventana.blit(Imagen, Coordenadas)    
    pygame.display.flip()

   # Manejador de eventos
    for evento in pygame.event.get():
        # Pulsación de la tecla escape
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                sys.exit()
            elif evento.key == pygame.K_RIGHT:
                incrementoX = 5
            elif evento.key == pygame.K_DOWN:
                incrementoY = 5
            elif evento.key == pygame.K_LEFT:
                incrementoX = -5
            elif evento.key == pygame.K_UP:
                incrementoY = -5
        if evento.type == pygame.KEYUP:
            incrementoX = 0
            incrementoY = 0

    coordX = coordX + incrementoX
    coordY = coordY + incrementoY

    Coordenadas = (coordX, coordY)

    # Asignamos un "tic" de 30 milisegundos
    Reloj.tick(30)
```

Fíjate que, en este ejemplo, creamos un reloj al principo del programa y le ponemos el tic de 30 milisegundos dentro del bucle (al final)

> Puedes cambiar el tiempo del tic y experimentar con los resultados.

Podemos usar este reloj para muchas otras cosas, como contar el tiempo (lógicamente) sincronizar eventos, hacer animaciones...

> Puedes ver más detalles en la [documentación oficial del módulo "time" de pygame](http://www.pygame.org/docs/ref/time.html)

