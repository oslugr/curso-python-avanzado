##Instalar MySQLlib

MySQLlib es una librería que gestiona el acceso a MySQL desde Python. Es la que se ocupa de que Python y MySQL “se entiendan”, y debe estar instalada para poder usar MySQL.

###Método básico (Linux y Windows)

El procedimiento para instalar es el mismo que para cualquier otro módulo:

Primero, debes ir a la página del proyecto y descargarlo:

[http://sourceforge.net/projects/mysql-python/](http://sourceforge.net/projects/mysql-python/)

El archivo que se obtiene en su página de sourceforge es un archivo comprimido (con extensión *.tar.gz). Se debe descomprimir en cualquier directorio (es sólo temporal, luego se podrá borrar) y después, en ese mismo directorio, ejecutar la siguiente orden:

```
python setup.py install 
```

necesitarás permisos de superusuario, de modo que, dependiendo de la distribución de linux que uses deberás usar sudo, su, o cambiar de usuario.

Por ejemplo, en Ubutu se haría así:

```
sudo python setup.py install 
```

###Gestor de paquetes (Linux)

Casi todas las distribuciones tienen un paquete para instalar este módulo.

En el caso de sistemas Debian, Ubuntu y similares, puedes usar tu gestor de paquetes favorito para evitare tener que descargar nada e instalar el paquete deb desde el repositorio de tu distribución. Por ejemplo, con apt-get:

```
apt-get install python-mysqldb 
```

(también necesitarás permisos de root)

###Binarios precompilados (Windows)

Algunas versiones de Windows dan errores durante la instalación, a causa de un problema en el registro. Para ellas existen una serie de binarios precompilados (con extensión *.exe) que sólo hay que descargar y ejecutar para que se instalen.

Se pueden descargar de la siguiente dirección:

[http://www.codegood.com/](http://www.codegood.com/)

Como segunda opción, también puede ser interesante conocer un repositorio no oficial de librerías de Python para Windows:

[http://www.lfd.uci.edu/~gohlke/pythonlibs/](http://www.lfd.uci.edu/~gohlke/pythonlibs/)

En esta página sólo tienes que buscar el módulo que te interesa, descargar la versión adecuada para tu arquitectura, y ejecutar el instalador. 
