##Conectando a MySQLlib

Para empezar, como con cualquier otro módulo, hay que importarlo:

```
import MySQLdb 
```

Lo siguiente es establecer una conexión

```
Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan') 
```

Dado que una base de datos puede ser servida desde un ordenador remoto a través de una red, la opción "host" nos da la oportunidad de indicar aquí la dirección de esa máquina. Normalmente (y este va a ser nuestro caso), se conectará con un servidor de bases de datos ubicada en el mismo ordenador, lo que indicamos con "localhost".

En "user" indicamos, obviamente, el nombre de usuario con el que conectaremos a la base de datos (y cuyos permisos serán los que tenga nuestra conexión) y, en "passwd" indicamos la contraseña de este usuario. Por último, dado que un servidor de bases de datos puede servir varias de ellas, tenemos que indicar el nombre de la base a la que conectamos, lo que hacemos en "db".

La función "connect" nos devuelve un objeto "Connection" que recogeremos en la variable "Conexion" para poder referenciarla luego.

Algunas configuraciones de bases de datos, principalmente para optimizar recursos, usan lo que se llama "transacciones" (particularmente, las bases de datos del tipo InnoDB permiten transacciones, mientras que las MyISAM no).

Esto significa, de modo muy resumido y a los efectos de lo que nos interesa ahora, que pueden ir acumulando las órdenes que se les dan y ejecutarlas de una sola vez como un paquete. Lo bueno es que se pueden hacer cosas como cancelar peticiones o grupos de ellas en función de otras entradas posteriores y otras cosas parecidas. Y lo malo de esto es que puede darse el caso de que creamos haber insertado datos y estos no estén aún allí. Afortunadamente, tenemos una orden para obligar a la base de datos a ejecutar las órdenes que le hemos mandado.

Se trata del método commit de la clase Connection que, si la base de datos admite transacciones, hace ese envío de los datos, de este modo:

```
Conexion.commit() 
```

En caso de que la base de datos no admita transacciones (con lo que las órdenes se ejecutan sobre la marcha), este método no hace nada, lo cual hace que podamos usarlo "preventivamente" aún sin saber qué tipo de base de datos estamos usando, y si usa transacciones. 
