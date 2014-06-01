## Instalando MySQL

Lo primero que necesitamos para trabajar con bases de datos es, evidentemente, una base de datos con la que trabajar.

Existen multitud de bases de datos, pero todas se usan en Python de modo similar, con lo que sólo usaremos una de ellas en este curso.

MySQL es un motor de bases de datos robusto, eficiente y libre que es tremendamente popular y puede encontrarse en cualquier plataforma, por lo que es de los más utilizados hoy en día.

###Windows

En Windows el modo más simple de instalar MySQL es ir a su página oficial y descargar el instalador automático [http://dev.mysql.com/downloads/installer/](http://dev.mysql.com/downloads/installer/).

Una vez descargado se ha de ejecutar y este irá dirigiendo los pasos del usuario. La instalación no plantea más dificultad que recordar la clave que se use como root (ver más abajo) pero, si hubiese algún problema, hay una extensa página de ayuda en la instalacion [http://dev.mysql.com/doc/refman/5.0/es/windows-installation.html] en la página oficial de MySQL

###Linux

Desde Linux es muy fácil instalar MySQL usando un gestor de paquetes.

Por ejemplo, en Debian, Ubuntu y derivadas se puede instalar por medio del paquete deb mysql-server:

```
aptitude install mysql-server 
```

(necesitas permisos de root para ello)

Durante la instalación se mostrará una pantalla para introducir la clave del usuario root similar a esta:

![Solicitando la clave de root](../img/Bases_de_Datos_con_MySQLdb1.png)

En ella debemos introducir una contraseña para el usuario root de la base de datos (que no tiene por qué coincidir con el usuario root de tu sistema, si lo tienes). Este usuario puede hacer y deshacer todo en todas tus bases de datos, de modo que úsalo con cuidado (luego, para trabajar, crearemos otro usuario menos peligroso).

una vez finalizada la instalación, el servidor se iniciará como demonio en tu sistema y todo está listo para empezar. 
