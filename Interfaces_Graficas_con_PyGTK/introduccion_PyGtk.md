##Introdución
PyGTK es un conjunto de implementaciones de las librerías de la interfaz de usuario de GTK+ para el lenguaje de programación Python.

Python es un lenguaje de programación interpretado, ampliable y orientado a objetos que se distribuye con un amplio conjunto de módulos que permiten el acceso a un gran número de servicios del sistema operativo, servicios de internet (como HTML, XML, FTP, etc.), gráficos (incluidos OpenGL, TK, etc.), funciones de manejo de cadenas, servicios de correo (IMAP, SMTP, POP3, etc.), multimedia (audio, JPEG) y servicios de criptografía. Existen además multitud de módulos proporcionados por terceros que añaden otros servicios.

GTK (GIMP Toolkit) es una librería que permite crear interfaces gráficas de usuario. Se distribuye bajo la licencia LGPL, por lo que posibilita el desarrollo de software abierto, software libre, e incluso software comercial no libre que use GTK sin necesidad de pagar licencias o derechos.

Se le conoce como el toolkit de GIMP porque originalmente se escribió para desarrollar el Programa de Manipulación de Imágenes de GNU GIMP, pero GTK se usa ya en numerosos proyectos de software, incluído el proyecto de escritorio GNOME (Entorno de Modelo de Objetos orientados a Red). GTK+ está diseñada sobre GDK (Kit de Dibujo de GIMP) que, básicamente, es una abstracción de las funciones de bajo nivel que acceden al sistema de ventanas (Xlib en el caso del sistema de ventanas X).


GTK es fundamentalmente un interfaz orientada a objetos para programadores de aplicaciones (API). Aunque está escrita completamente en C, está implementada usando la idea de clases y funciones de retrollamada (punteros a función).

En el repositorio alojado en [Github](http://github.com/oslugr/curso-python-avanzado/tree/master/Interfaces_Graficas_con_PyGTK) tenéis los códigos de ejemplo de este módulo del curso.

##Instalación

###Requisitos
Para la creación de un entorno de desarrollo decente en GNOME es necesario trabajar sobre una máquina con una distribución reciente. De esta manera evitaremos luchar con viejos problemas y dependencias. Para las siguientes instrucciones, se supone que se ha instalado Ubuntu 11.10 (o superior) en el equipo. Es muy aconsejable disponer de la versión 3.2 de GNOME, de esta manera también evitaremos problemas con dependencias.

###Herramientas de desarrollo
Mediante la línea de órdenes (o el Centro de Software de Ubuntu) instalaremos los paquetes necesarios para crear nuestras aplicaciones. Básicamente necesitaremos 3 herramientas:

1. Tu IDE preferido o un simple editor de texto nos será mas que suficiente. Como buenos editores puedes usar:
    1. [Geany](www.geany.org/)
    2. [Atom](https://atom.io/)
2. [Glade](http://glade.gnome.org/), necesario para hacer el diseño de la interfaz. Versión recomendada 3.10
3. [DevHelp](http://live.gnome.org/devhelp), documentación.

###Paquetes necesarios para Python
Python utiliza [GobjectIntrospection](http://live.gnome.org/GObjectIntrospection), por lo tanto simplemente tenemos de asegurarnos de tener un buen entorno de desarrollo para Python. Imprescindibles los paquetes python y python-object. Desde el intérprete de órdenes se instalarán fácilmente con apt-get (desde Ubuntu y derivados o con órdenes como yum, pacman etc si usamos otra distribución).

Para curarnos en salud y evitar errores por dependencias, instalaremos también el paquete gobject-introspection.

En definitiva:
```
sudo apt-get install python-gobject gobject-introspection
```

La instalación de librerías y paquetes has configurar nuestro entorno de desarrollo sea lo menos divertido en cuanto a la creación de aplicaciones con PyGTK. Una vez creado nuestro ¡Hola mundo! con PyGTK, el resto será coser y cantar.
