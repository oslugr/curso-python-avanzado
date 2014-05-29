##Introducción
En este módulo vamos a ver qué trata esta técnica de programación, a la que se le puede sacar mucho partido y puede dar mucho juego para hacer aplicaciones.
Acabando el módulo con un ejercicio simple de hacer, así que empecemos.


###¿Qué es el scraping?
Os preguntaréis ¿qué es eso del scraping? Pues el scraping (traduciendo del inglés sería como “raspar algo”) en general es una técnica para obtener información de diferentes medios, lo que podemos denominar como Data scraping.

Pues bien hay varios términos que podemos diferenciar en el mundo del scraping como son:
-Screen scraping.
Es la técnica con la que podemos obtener la información de un dispositivo gráfico, como ejemplo hipotético pongámonos en aquellos años de 1950 donde se usaban pantallas informativas, unos simples terminales que mostraban información. Pues para recabar esos datos tendríamos que diseñar un sistema el cual podríamos conectar mediante algún protocolo y emular las pulsaciones para movernos por el texto mostrado obteniendo lo que nos interese y enviando esta información a un sistema moderno para procesarla.

-Web scraping.
Es una técnica muy común (de hecho es sobre la que nos vamos a centrar en este módulo de scraping) ya que de lo que trata es obtener la información de un recurso como por ejemplo de una página web en HTML y procesar esa información.

-Report mining.
Al igual que el web scraping y el screen scraping es otra técnica que también pretende obtener información pero en este caso a partir de un archivo (HTML, RDF, CSV, etc). Así con esta aproximación de definición podemos crear un mecanismo simple y rápido sin necesidad de escribir una API y como característica principal podemos indicar que el sistema no necesita de una conexión ya que al trabajar a partir de un fichero es posible extraer la información de forma offline y sin necesidad de utilizar ninguna API. Con esta técnica se consigue facilitar el análisis evitando el uso excesivo del equipo y tiempo de computación e incrementar la eficiencia y la rapidez para un prototipado y desarrollo de reportes personalizados (por ejemplo en una empresa, que estos reportes se realicen fuera del horario comercial).

-Spider.
Los spiders (podríamos traducirlo por los rastreadores aunque su significado literal sea arañas) son scripts o programas que siguen unas reglas para moverse por el sitio web y recabar la información imitando la interacción que realizaría un usuario con el sitio web.

###¿Para qué me sirve?
Supongamos el ejemplo que has visto una página web que te gusta mucho y quieres obtener cierta información de la misma, por ejemplo has entrado en ```JuanitoInformática``` y quieres obtener de forma periódica los precios de las tarjetas gráficas de nVidia, pues con el scraping puedes conseguirlo, te cueste más o menos y tardes más tiempo o menos se puede recabar esa información tan interesante y preciada para ti para que puedas utilizarla según lo que necesites de forma independiente a la web original.

### Entonces creo que puedo empezar
Llegados a este punto del módulo podemos decir que el scraping es una técnica muy potente si sabes como utilizarla y si aún no estás convencido continúa con el módulo y verás que no es complicada la técnica una vez empiezas.

###¿Qué necesito saber?
Pues aparte de lo descrito antes, para que tengas unas nociones básicas de este tema es necesario que sepas algo básico de páginas web y poquito más.

###Herramientas de refuerzo y útiles
-Firefox como navegador
Para la realización del curso es recomendable usar Firefox por varios motivos, entre ellos, que es un navegador perteneciente a la comunidad de software libre, cumple los estándares web y tiene una gran funcionalidad.
-Firebug.
Depuración y obtención de XPath expresions. Firefox dispone de un add-on (un complemento) llamado Firebug. Con este complemento nos podemos ayudar para el desarrollo de proyectos de distintas índoles, entre ellas para hacer scraping ya que podemos obtener la expresión XPath de los enlaces o metadatos que queremos obtener.
![XPath Expressions](../img/Scraping_XPathExpression.png)

-Firefinder.
Testing de XPath expresions. Es otro complemento de Firefox con el que podemos probar expresiones XPath sobre la página web y así, después, traerlas a un proyecto y usarlas.
![Firefinder](../img/Scraping_Firefinder.png)

###¿Dónde y cómo conseguir la información?
Para hacer scraping la información la podemos obtener de cualquier página web, y para conseguirla tenemos dos medios:
-De forma automatizada por el sitio. Es decir, que el website provee una API (Aplication Programing Interface) para interactuar con el sitio.
-Manualmente. No disponemos de la API comentada y tenemos que diseñar nosotros los mecanismos para el acceso a ella.


##Un ejemplo sencillo y básico
Pues aquí os dejamos un ejemplo sencillo y básico para hacer scraping, como se dice, de andar por casa.
Se trata de un módulo (lo podemos importar en la shell de python incluso) llamado pyGIFW (pyGetImagesFromWebsites) el cual se puede usar para descargar las imágenes de una página web indicada o de varias. Os lo podéis descargar aquí o clonar el repositorio con GIT.

Implementa una serie de funciones junto con una pequeña interfaz para usarlas.

Veamos parte del código:
```python
def getImgFromUrl(urlSource, extension):
	"""
		name: getImgFromUrl
		brief: Get images from a url template.
		param urlSource: Url from where get the links of the images.
		param extension: Extension to add the regular expression.
		return: All the links that match with the regular expresion.
	"""
	# GET HTML
	url = urllib.urlopen(urlSource)
	html = url.read()

	# REGULAR EXPRESION COMPILATION
	expresion = r'<img src="([^"]+).' + extension + '"'
	regexp = re.compile(expresion, re.I | re.MULTILINE | re.DOTALL

	# FIND ALL CASES OF THE REG. EXPR.
	links = regexp.findall(html)

	# CREATING A LIST WITH ALL THE LINKS THAT MATCH WITH THE REG. EXPR.
	i=0
	while i<len(links):
		links[i]=links[i]+'.'+extension
		print links[i], "\n"
		i += 1

	return links
```

Como podéis ver es un ejemplo sencillo y fácil de entender aunque expliquemoslo un poco. El módulo puede recibir varios argumentos. Veamos el caso más sencillo, que es escribir en la consola:
```bash
python pyGIFW 0 URL
```

Con esto lo que estamos haciendo es indicarle al módulo que con la opción 0 le vamos a pasar a continuación una URL, que es de la que queremos descargar las imágenes. En sí no se descargan directamente si no que, para la URL dada, hace un scraping muy simple tomando todos los enlaces a imágenes de una extensión determinada (también podemos indicar qué tipo de extensión queremos descargar) y creando un script para su posterior descarga. El script lo ejecutaríamos como:
```bash
sh img_extension.sh
```
Donde 'extension' es el nombre de la extensión de la imagen.


##Frameworks y librerías para scraping
En los siguientes apartados trataremos distintos frameworks y librerías que se usan en Python para scraping.

###¿Qué es un framework? Objetivos
Un framework si lo traducimos literslamente es un "Marco de trabajo". Aunque más bien deberíamos definirlo como el entorno o capa de abstración que existe entre el código puro y duro con respecto a lo que el usuario ve. La interacción es algo como:
CODE <-|Interactua con|-> FRAMEWORK <-|Interactua con|-> USER

¿Qué obtenemos con esto? Básicamente lo que conseguimos con un framework es tener un nivel más alto de abstracción para realizar nuestro trabajo. No evita el tener que realizar el código a mano, pero sí nos quita bastante trabajo. Así que ¿cuáles son los objetivos de un frawework? Son los siguientes:
-Simplificar el trabajo, ganando eficiencia.
-Extensibilidad de sí mismo.
-Proveer una unión de herramientas como son el editor de código, compilador, librerías y APIs entre otras.

### Frameworks para scraping en Python
-Mechanize
Un gran conocido entre todos los que hay, está basado básicamente en el trabajo de Andy Lester (Creador del framework original en Perl [WWW:Mechanize]), Gisle Aas, Jeremy Hylton y Johnny Lee.
-Scrapy
Es el framework que vamos a utilizar en este curso. Es un framework más joven que Mechanize pero sigue una filosofía mucho más cercana a la de Python. Características de este framework:
*Una sintaxis muy clara y estructurada.
*Gran potencial.
*Rapidez y eficiencia.
*Muy buena documentación y ejemplos.
*Puedes incrustar extensiones propias en Scrapy para aumentar su funcionalidad.
*Portable. Puede usarse tanto desde Linux como desde otros sistemas operativos.
Algo que podríamos también denotar de Scrapy es que sigue una filosofía de estructuración en el proyecto parecida a Django (esto es debido a que los desarrolladores de Scrapy han tomado ideas de Django, como dicen de forma resumida en su FAQ: “¿Scrapy ha "robado" algo de Django? - A lo que responden - Probablemente, por que ya que Django es un gran proyecto ¿para qué reinventar lo que ya existe?” Los desarrolladores de Scrapy han sabido usar la filosofía DRY(Don't Repeat Yourself).
Aún no soporta la versión 3.0 de Python así que es recomendable que tengáis instalada la versión 2.5, 2.6 o 2.7 de Python para trabajar con Scrapy.

###Librerías para scraping
-Beautiful Soup
Una librería que existe desde el año 2004 que ha ayudado a muchos desarrolladores. Características de esta librería:
	*Métodos simples con una estructura "Pythónica" para navegar, buscar y modificar el árbol de análisis.
	*Automáticamente convierte el documento de entrada a Unicode y el documento de salida a UTF-8.

-lxml
lxml es la caja de herramientas que une las librerías libxml2 para análisis de documentos XML y libxslt (basada en la anterior) es la libería que en sí misma es lenguaje XML para hacer transformaciones en documentos XML.Características de esta librería:
	*Soporte de forma estándar para XML.
	*Soporte para HTML.
	*Mantenido por expertos de XML.
	*Dispone de una API basada en "ElementTree".

-XPath Selectors
Es otra librería, que es la que usa Scrapy de forma predeterminada e integrada, con una sintaxis clara. Trabaja sobre documentos XML aunque también puede tratar documentos HTML lo que la hace muy versátil.
Características de esta librería:
	*Basada en libxml2.
	*Dispone de una API para XML y HTML.


##Scrapy
Este es el framework que vamos a utilizar, comencemos con el punto 5.4.1 y continuemos.

###Requisitos
Se recomienda lo siguiente:
-Usar una versión de Python 2.5, 2.6 o 2.7 (ya que la versión para Python 3.0 aún no está soportada).
-Twisted 8.0 (si estás en windows se recomienda instalar Zope.interface y pywin32).
-w3lib.
-lxml o libxml2 (si usas libxml2 se recomienda la versión 2.6.28).
-simplejson, si usas una versión 2.6 o superior de Python no es necesario.
-pyopenssl (para conexiones https seguras y se recomienda instalarlo).
-El intérprete de Python: IPython.
-Una conexión a internet estable para cuando lo usemos.

###Instalación de Scrapy (versión 0.14)
La instalación del framework es muy simple y la podemos hacer por dos vías:
-Descompilar el tarball de la página oficial del sitio, satisfaciendo las dependencias manualmente y una posterior compilación, esta vía es para los más atrevidos.
-O bien usando easy_install o pip también lo podemos instalar despreocupándonos de las dependencias, para ello ejecutaremos:
```bash
easy_instal install scrapy
```
o bien
```bash
pip install scrapy
```


##Estructura interna de Scrapy
![Estructura](../img/Scraping_EstructuraScrapy.png)
Como podéis apreciar en esta imagen, tenéis la funcionalidad del framework el cual consta de:
-El núcleo en sí (Scrapy Engine).
-Los rastreadores denominados como Spiders.
-Los objetos Items, Requests y Responses que vamos a usar.
-El planificador de ejecucion de los elementos (Scheduler).
-Los Item Pipeline encargados para el almacenamiento de la información.
-Y por último la interfaz de Descargas que interactúa con Internet.

### Elementos básicos
Scrapy dispone de una serie de elementos que engloba y con los que trabaja al hacer scraping, que son los siguientes puntos.

#### Items
El principal objetivo de Scrapy es extraer datos estructurados desde fuentes como típicamente son las páginas web. Provee la clase ```python Item()``` la cual es para este propósito. Simplemente son contenedores usados para almacenar los datos obtenidos. Estos contenedores están provistos de una API tipo diccionario con una sintaxis para declarar los campos disponibles.

Para crear un Item lo debemos hacer de esta forma:
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class Producto(Item):
	name = Field()
	precio = Field()
	stock = Field()
	ultimo_actualizado = Field(serializer=str)
```

Para quien haya usado Django esto le puede resultar familiar, ya que los Items se asemejan mucho a los Django Models aunque son algo más sencillos. Los Item Fields son los objetos que engloban en sí la meta información. En ellos podemos almacenar lo que necesitemos con lo que no existe ninguna lista de referencia para los datos a guardar. En sí son una abstracción de los diccionarios de Python. También se puede extender la funcionalidad de los Items, de forma que para el ejemplo expuesto antes podemos crear subclases cuya dependencia es la anterior clase. Por ejemplo podríamos hacer:
```python
class DiscountedProduct(Item):
	discount_percent = Field(serializer=str)
	discount_expiration_date = Field()
```

O incluso:
```python
class SpecificProduct(Product):
	name = Field(Product.fields[’name’], serializer=my_serializer)
```
Donde podemos ver que se puede añadir (o reemplazar) la clave de metadatos "serializer" manteniendo todos los metadatos existentes.

#### XPath Selectors
Los XPath Selectors o simplemente llamados Selectors son los elementos usados para acceder a los datos del documento.

Estos objetos se construyen en base a expresiones XPath. Existen dos tipos:
-HtmlXPathSelector: Para trabajar con documentos HTML
-XmlXPathSelector: Para trabajar con documentos XML

Ambos tipos comparten la misma API de selectores y se construyen con un objeto ```response``` como primer parámetro. Ejemplos:
```python
hxs = HtmlXPathSelector(response) # Un selector de HTML
```
```python
xxs = XmlXPathSelector(response) # Un selector de XML
```

Para ver su funcionamiento mejor vamos a verlo con un ejemplo práctico. En una consola vamos a usar la terminal integrada de Scrapy y una página alojada en los servidores de Scrapy, en la parte de documentación.

Así, en la terminal, escribimos:
```bash
scrapy shell http://doc.scrapy.org/_static/selectors-sample1.html
```

El código HTML de la página es:
```html
<html>
<head>
	<base href="http://example.com/" />
	<title>Example website</title>
</head>

<body>
	<div id="images">
		<a href="image1.html">Name: My image 1 <br /><img src="image1_thumb.jpg"/></a>
		<a href="image2.html">Name: My image 2 <br /><img src="image2_thumb.jpg"/></a>
		<a href="image3.html">Name: My image 3 <br /><img src="image3_thumb.jpg"/></a>
		<a href="image4.html">Name: My image 4 <br /><img src="image4_thumb.jpg"/></a>
		<a href="image5.html">Name: My image 5 <br /><img src="image5_thumb.jpg"/></a>
	</div>
</body>
</html>
```

Cuando ejecutemos la orden tendremos cargado en memoria algunas variables por defecto como la variable hxs. Podemos ejecutar estas órdenes:
```python
hxs.select(’//title/text()’)

[<HtmlXPathSelector (text) xpath=//title/text()>]

hxs.select(’//title/text()’).extract()

[u’Example website’]
```
La diferencia entre esta orden y la anterior es que si no ejecutamos el método extract() no accedemos al contenido y en cambio lo que obtenemos es el objeto en sí y de qué tipo es el contenido.
```python
hxs.select(’//a[contains(@href, "image")]/@href’).extract()
[u’image1.html’,
u’image2.html’,
u’image3.html’,
u’image4.html’,
u’image5.html’]

hxs.select(’//base/@href’).extract()
hxs.select(’//a[contains(@href, "image")]/img/@src’).extract()
```

Estos dos últimos los dejamos sin el resultado para que comprobéis que obtenéis al ejecutarlo. También podemos usar los selectores junto con expresiones regulares, lo cual lo hacemos mediante el método re(). Por ejemplo:
```python
hxs.select(’//a[contains(@href, "image")]/text()’).re(r’Name:\s*(.*)’)
[u’My image 1’,
u’My image 2’,
u’My image 3’,
u’My image 4’,
u’My image 5’]
```

Tenemos la posiblidad de usar los selectores con expresiones absolutas o relativas, al igual que con los directorios en un sistema de ficheros por lo que debemos de prestar atención. Por ejemplo:
```python
divs = hxs.select(’//div’) # Obtenemos todos los 'div' del documento.

for p in divs.select(’//p’): # Este uso es erróneo para obtener los <p> de cada <div>
	print p.extract()

for p in divs.select(’.//p’): # Con este modo extraemos todos los <p> de cada <div>
	print p.extract()

for p in divs.select('p'): # Análogo al trozo de código correcto.
	print p.extract()
```

#### Spiders
Los spiders son clases que definen la forma de navegar por un determinado sitio o dominio y como extraer datos de esas páginas. Es decir que con los spiders definimos de forma personalizada el comportamiento para caminar y analizar las páginas de un sitio particular.

El ciclo que sigue un spider es el siguiente:
-Primero empezamos generando la petición inicial (Requests) para navegar por la primera URL y especificamos la función de "vuelta atrás" a ser llamada con la respuesta (Response) descargada de esa petición. La primera petición a hacer es obtenida llamando al método start_request() que por defecto genera la petición para la URL especifica en las direcciones de partida "start_urls" y la función de "vuelta atrás" para las peticiones.
-En la función de "vuelta atrás" analizamos la respuesta y se puede devolver:
	*Objetos tipo Item.
	*Objetos tipo Request.
	*O una unión de ambos sobre la que se puede iterar.

-Así estas peticiones serán realizadas descargándose por Scrapy y sus respuestas manipuladas por las funciones de "vuelta atrás". En las funciones de "vuelta atrás" analizamos el contenido típicamente usando los selectores (XPath Selectors) y generamos los Items con el contenido analizado.

-Finalmente los Items devueltos por el spider se podrán pasar a algún Item Pipeline.

Generalmente se sigue este ciclo de funcionamiento por todo tipo de spider. Existen varios tipos que vienen por defecto con una acometida específica. Vamos a explicarlos y ver algún ejemplo:

-BaseSpider. Este es el tipo más básico de spider.

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
from myproject.items import MyItem

class Rastreador(BaseSpider):
	name = 'example.com'
	allowed_domains = ['example.com']
	start_urls = [
	'http://www.example.com/1.html',
	'http://www.example.com/2.html',
	'http://www.example.com/3.html',
	]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		for h3 in hxs.select('//h3').extract():
			yield MyItem(title=h3)
			for url in hxs.select('//a/@href').extract():
				yield Request(url, callback=self.parse)
```

-CrawlSpider. Es el más usado de todos los que hay. Aparte de los atributos inherentes a la clase BaseSpider, esta clase dispone de un nuevo atributo "rules" con el cual podemos indicarle al Spider el/los comportamiento/s que debe seguir (si hay 2 o más reglas que coinciden en el mismo enlace la primera es la que se sigue).
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item

class MySpider(CrawlSpider):
	name = 'example.com'
	allowed_domains = ['example.com']
	start_urls = ['http://www.example.com']
	rules = (
	# Extraer enlaces que coincidan con 'category.php' (pero que no coincidan con 'subsection.php') y seguir esos enlaces (si no indicamos callback significa que debe seguir por defecto)
	Rule(SgmlLinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),
	# Extraer los enlaces que coincidan con 'item.php' y analizarlos con el método parse_item de los spiders
	Rule(SgmlLinkExtractor(allow=('item\.php', )), callback='parse_item'),
	)

	def parse_item(self, response):
		self.log('Hola!, esta es una página tipo item! %s' % response.url)
		hxs = HtmlXPathSelector(response)
		elemento = Item()
		elemento['id'] = hxs.select('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
		elemento['name'] = hxs.select('//td[@id="item_name"]/text()').extract()
		elemento['description'] = hxs.select('//td[@id="item_description"]/text()').extract()
		return elemento
```

-XMLFeedSpider
-CSVFeedSpider
-SitemapSpider
Existen estos tres últimos también pero si estáis interesados en saber como funcionan en la documentación de Scrapy vienen bien especificados y con más ejemplos, por eso no van a ser explicados ya que no son necesarios para más adelante y una vez se dominen los Spiders anteriores estos serán más sencillos.

#### Items pipelines y formatos de exportación
Los Items Pipelines podríamos denominarlos como los cauces o tuberías de los Items. Son elementos de Scrapy a los que la información que les llega son Items que han sido previamente obtenidos y procesados por algún Spider. Son clases en sí que tienen un simple objetivo: volver a procesar el Item que les llega pudiendo rechazarlo por algunos motivos o dejar que pase por este cauce.
Usos típicos de estos cauces son:
-Limpieza de datos en HTML.
-Validación de datos scrapeados comprobando que los Items contienen ciertos campos.
-Comprobación de Items duplicados.
-Almacenamiento de los datos en una base de datos.

Estos objetos son clases de Python que deben implementar el método process_item(item, spider) y deben devolver un objeto tipo Item (o una subclase de este) o bien, si no lo devuelve, debe lanzar una excepción del tipo DropItem para indicar que ese Item no seguirá siendo procesado.

Un ejemplo de este componente es:
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem

class PrecioPipeline(object):
	impuesto = 18.0
	def process_item(self, item, spider):
		if item['precio']:
			if item['precio_sin_tasa']:
				item['precio'] = item['precio'] * self.impuesto
				return item
			else:
				raise DropItem("No tiene tasa alguna el elemento: %s" % item)
```

Un punto más a tener en cuenta. Cuando creamos un objeto de este tipo debemos introducir en el fichero settings.py del proyecto una línea como la siguiente para activar la tubería:
```python
ITEM_PIPELINES = [
'miproyecto.pipeline.nombreTuberia',
]
```
Donde 'miproyecto' es el nombre del proyecto en sí y 'nombreTuberia' es el nombre que le hemos dado a la clase que implementa la tubería de paso de información.


Y para la escritura de los items:
```python
import json

class FicheroJsonPipeline(object):
	def __init__(self):
		self.file = open('items.jl', 'wb') # Abrimos un fichero en modo de escritura

	def process_item(self, item, spider):
		linea = json.dumps(dict(item)) + '\n'
		self.file.write(linea)
		return item
```

Al final el salvar los datos obtenidos debemos hacerlo mediante lo que se llaman Feed Exports, que no es más que los formatos de serialización y los backends para guardar los datos.
Como formatos de serialización tenemos:

| Formato    	| Usa el exportador 	|  Salida en  	|
| ---------- 	| ----------  			|  ---------- 	|
| JSON 			| JsonItemExporter 		|  .json 		|
| JSON Lines 	| JsonLinesItemExporter	| .jsonlines 	|
| CSV 			| CsvItemExporter 		| .csv 			|
| XML 			| XMLItemExporter		| .xml 			|
| Pickle 		| PickleItemExporter 	| pickle 		|
| Marshal 		| MarshalItemExporter 	| marshal 		|


Cuando usamos un formato de exportación, debemos indicar en el fichero settings del proyecto mediante la variable FEED_URI dónde vamos a realizar el almacenamiento, es decir el backend que vamos a usar. Podemos elegir entre varios:
-Sistema de ficheros local.
-FTP.
-S3 (requiere que tengamos instalado ```boto```, una interfaz de Python para Amazon Web Services).
-Salida estándar por pantalla.

###Ciclo de trabajo
Veamos ahora cual es el ciclo de trabajo con Scrapy. 

####Creación de un proyecto
Bien, ya que hemos explicado los elementos más básicos y necesarios de Scrapy, ahora vamos a empezar con la creación de un proyecto. Para ello es tan sencillo como dirigirnos en una terminal a un directorio de trabajo que queramos y escribir:
```bash
scrapy startproject NombreDelProyecto
```
Esto nos creará un árbol de directorios predefinido como el siguiente por ejemplo:
```bash
ejemplo1/
├── ejemplo1
│ ├── __init__.py
│ ├── items.py # Fichero donde definir los Items del proyecto.
│ ├── pipelines.py # Fichero donde definir los Items Pipelines del proyecto.
│ ├── settings.py # Fichero de ajustes del proyecto
│ └── spiders # Directorio donde almacenar los ficheros que definen los Spiders.
│ └── __init__.py
└── scrapy.cfg # Fichero de configuración del proyecto.
```

####Definición de los Items, los Spiders y los Items Pipelines a extraer.
Como ya hemos visto antes, ya debemos saber definir los items, los spiders y los cauces de items para guardar la información o rechazarla. Ahora es el momento de definir todo lo que necesitemos al respecto.

####Ejecución del proyecto
Para poner en marcha el proyecto en el primer nivel del árbol de directorios del proyecto debemos escribir:
```bash
scrapy crawl NombreDelProyecto -o items.json -t json
```

Donde los últimos parámetros indican que los datos extraídos se almacenen en un fichero llamado 'items.json' y que use el exportador para formato JSON.

###Elementos avanzados
Scrapy dispone de muchos más elementos para características más avanzadas como son los Servicios Web que implementa por defecto, manejo de señales en el proyecto (tanto internas a Scrapy como externas definidas por el usuario), manejo también de excepciones, uso de memoria y depuración de fallos de memoria, configuración de proxys y Spiders, extractores de imágenes y enlaces.


##Recursos adicionales
Aquí tenéis un listado de recursos adicionales que os pueden ser útiles para este módulo por si queréis profundizar más en el tema:
-Librerías
	*Beautiful Soup http://pypi.python.org/pypi/beautifulsoup4/4.0.4
	*Mechanize http://pypi.python.org/pypi/mechanize/
	*lxml http://lxml.de/

-Scrapy
	*Scrapy Google Groups - https://groups.google.com/forum/?hl=es&fromgroups#%21forum/scrapy-users
	*Documentación de Scrapy - http://doc.scrapy.org/en/0.14/index.html
	*Snippets - http://snippets.scrapy.org/

-Wikipedia
	*Web scraping - http://en.wikipedia.org/wiki/Web_scraping
	*Screen scraping - http://es.wikipedia.org/wiki/Screen_scraping
	*Report mining - http://en.wikipedia.org/wiki/Report_mining

-Otros
	*Dive Into Python’s tutorial on HTML processing - http://www.diveintopython.net/html_processing/extracting_data.html
	*XPath Expressions - http://en.wikipedia.org/wiki/XPath
	*XPath Selectors - http://doc.scrapy.org/en/latest/topics/selectors.html
	*Scrapemark - http://arshaw.com/scrapemark/
