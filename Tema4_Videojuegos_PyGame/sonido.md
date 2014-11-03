##Sonidos

Pygame dispone del módulo `pygame.mixer` para manipular sonidos.

Para nuestro ejemplo vamos a usar como "efecto especial" el siguiente archivo de audio:

[ouch.wav](../img/ouch.wav)

Creado por [Under7dude](http://www.freesound.org/people/Under7dude/) y de dominio público.

Y para la "música de ambiente" este otro:

[guitarra.wav](../img/guitarra.wav)

Creado por [eltenjohn](http://www.freesound.org/people/eltenjohn/) y también en el dominio público.

Vamos a cargar ambos sonidos con la función `pygame.mixer.Sound()`, a la que se le pasa un archivo de sonido (en formato *.wav o *.ogg) y retorna un objeto `Sound`, que usaremos para reproducirlo etc.

Para reproducirlos, usaremos el método `play()` de la clase Sound. a este método se le pasa como parámetro el número de veces que quieras que se repita el sonido **además de la primera**. Si le pasas un 0 se reproducirá una sola vez, si le pasas un 3, el sonido se reproducirá cuatro veces en total.

Si le pasamos un cero como parámetro, el loop de sonido se reproducirá indefinidamente.

Podemos controlar el volumen de cada sonido con el método `set_volume`, que admite un valor entre 0.0 y 1.0 (aunque es mucho más recomendable tener los archivos de sonido preparados al volumen que nos interesa que ajustar unos respecto a otros durante la ejecución del programa)

Veamoslo con este ejemplo, en el que, además de reproducir un *sample* en loop como música de fondo, aplicaremos un efecto de sonido al hacer clic con el ratón:

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

import sys

from pygame.locals import *

def main():

    pygame.init()

    Reloj= pygame.time.Clock()

    Ventana = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Monigotillo animado")

    Fondo = pygame.image.load("fondo.jpg")

    Imagen = pygame.image.load("monigotillo.png")
    transparente = Imagen.get_at((0, 0))
    Imagen.set_colorkey(transparente)

    # Ruidito es un objeto Sound creado a partir del archivo *.wav
    Ruidito = pygame.mixer.Sound("ouch.wav")

    # Musica es otro objeto Sound creado a partir del archivo *.wav
    Musica = pygame.mixer.Sound("guitarra.wav")

    coordenadas_monigotillo= (300, 200)

    MiMonigotillo = Monigotillo(coordenadas_monigotillo, Imagen)

    # Bajamos el volumen de la música (sí, se puede hacer antes o durante la reproducción)
    Musica.set_volume(0.5)

    # Reproducimos nuestro sample de música en un bucle infinito (-1)
    Musica.play(-1)

    while True:

        MiMonigotillo.update(coordenadas_monigotillo)

        Ventana.blit(Fondo, (0, 0))
        Ventana.blit(MiMonigotillo.image, MiMonigotillo.rect)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    sys.exit()

            # Si el evento es una pulsación de ratón...
            elif evento.type == MOUSEBUTTONDOWN:

                # ...actualizamos las coordenadas de monigotillo con las del puntero...
                coordenadas_monigotillo = pygame.mouse.get_pos()

                # ...y reproducimos el sonido.
                Ruidito.play(0)
        Reloj.tick(30)


class Monigotillo(pygame.sprite.Sprite):

    def __init__(self, coordenadas, imagen):
        pygame.sprite.Sprite.__init__(self)

        self.ImgCompleta = imagen
        a=0
        self.arrayAnim=[]
        while a < 6:
            self.arrayAnim.append(self.ImgCompleta.subsurface((a*32,100,32,64)))
            a= a + 1
        self.anim= 0

        self.actualizado = pygame.time.get_ticks()
        self.image = self.arrayAnim[self.anim]
        self.rect = self.image.get_rect()
        self.rect.center = coordenadas


    def update(self, nuevas_coordenadas):
        self.rect.center = nuevas_coordenadas
        if self.actualizado + 100 < pygame.time.get_ticks():
            self.anim= self.anim + 1
            if self.anim > 5:
                self.anim= 0
            self.image = self.arrayAnim[self.anim]
            self.actualizado= pygame.time.get_ticks()


main()

```

> Naturalmente, tienes más herramientas para manipular sonodos en [la libería mixer de Pygame](http://www.pygame.org/docs/ref/mixer.html) 
