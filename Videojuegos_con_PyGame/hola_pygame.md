##¡Hola pyGame!

Vamos a dar nuestros primeros pasos en la programación de videojuegos con pygame usando un clásico "Hola Mundo".

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos la libería
import pygame

#Inciamos pygame
pygame.init()

# Creamos una surface (la ventana de juego), asginándole un alto y un ancho
Ventana = pygame.display.set_mode((600, 400))

# Le ponemos untítulo a la ventana
pygame.display.set_caption("Hola Mundo")
```

Como se puede leer en los comentarios (y cómo deberías comprobar ejecutándolo), este código crea una ventana de 600X400 pixels y le asigna un título.

> El módulo `pygame.display` es el encargado de crear y controlar la ventana y la pantalla de juego que contiene (que, a efectos prácticos, es un objeto `surface` (una imagen), como veremos más adelante.
> Nosotros hemos creado una ventana muy simple, pero puedes ver más posibilidades en la [documentación del módulo `pygame.display`](http://www.pygame.org/docs/ref/display.html)

Al ejecutar este ejemplo comprobarás que, inmediatamente, la ejecución del programa finaliza y esta ventana se cierra.

Para poder manejar nuestro programa, necesitaremos un bucle de eventos. Un bucle de eventos es un bucle infinito donde, a cada ciclo, comprobamos si ocurre algún envento y actuamos en consecuencia. El programa permanecerá en ejecución mientras permanezca en el bucle.

Veamoslo con un ejemplo algo más complejo:

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

# Creamos una surface (la ventana de juego), asginándole un alto y un ancho
Ventana = pygame.display.set_mode((600, 400))

# Le ponemos untítulo a la ventana
pygame.display.set_caption("Hola. Pulsa Escape para salir")

# Bucle infinito para mantener el programa en ejecución
while True:
    # Manejador de eventos
    for evento in pygame.event.get():
        # Pulsación de la tecla escape
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                sys.exit()
```

Para empezar, debes notar que estamos importando "pygame.locals" justo después de importar a la libería pygame (Bueno, también hemos importado "sys", pero esa librería no debería necesitar explicación).

Se trata de una serie de constantes que contienen los códigos para poder acceder a las teclas, eventos de ratón, etc. En nuestro ejemplo usaremos la tecla Escape.

En este ejemplo usamos un bucle infinito que mantiene el programa en ejecución, por lo que nuetra ventana no se cierra.

En cada ciclo del bucle infinito estamos usando pygame.event.get(), que nos retorna los eventos de pygame que estén ocurriendo.

Si el tipo de evento es una pulsación de tecla (al que accedemos con la constante de pygame "KEYDOWN") y esa tecla es Escape (K_ESCAPE), salimos del programa.

Por otro lado notarás que, si tratas de cerrarla pulsando el botón de cerrar de la propia ventana, esto no funciona.

Como prácitca, puedes intentar hacer que funcione teniendo en cuenta que la constante de pygame correspondiente a pulsar ese boton es "QUIT".

Como ya te estarás imaginado, prácticamente toda la interacción que hagamos con uestro juego en pygame se hará por medio de eventos.

Puedes verlos todos en esta [lista completa de eventos de pygame](http://www.pygame.org/docs/ref/event.html)
