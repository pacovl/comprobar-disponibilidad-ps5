# comprobar-disponibilidad-ps5
Código python que usa webscraping para notificarte por email cuando una página tenga disponible la ps5. En realidad serviría para cualquier tipo de producto online.
Los pasos a seguir son muy sencillos para que cualquiera pueda usarlo incluso sin saber programación:

1. Tener Python instalado (Si no tienes ni idea puedes empezar aquí https://docs.anaconda.com/anaconda/install/windows/)
2. Instalar la librería selenium. Para ello, en la terminal de python introducir el siguiente comando:
```
pip install selenium
```
3. Crear una cuenta de gmail para usarla como dirección origen de los avisos de disponibilidad. Debes activar la opción de seguridad 'Acesso de aplicaciones poco seguras' para que python pueda enviar correos desde esa cuenta (https://myaccount.google.com/lesssecureapps). La dirección de correo de destino puede ser cualquiera.
4. Descargar mi código y sustituir los datos para el correo electrónico en estas tres líneas:
```
  me = '<correo_origen>'     ### <-------------------------------------- Sustituir
  you = '<correo_destino>'   ### <-------------------------------------- Sustituir
  gmail.login(me,'<contraseña_correo_origen>')   ### <------------------ Sustituir
```
5. En el directorio donde tengas el código tienes que incluir un ejecutable de chrome que lo puedes descargar comprimido aquí: http://chromedriver.storage.googleapis.com/index.html?path=2.15/
6. Con esto ya estaría listo y puedes ejecutar el código para comprobar que todo funciona.

Hecho todo esto explico a grandes rasgos como funciona el código. En primer lugar hay que facilitarle un enlace del producto cuya disponibilidad queramos comprobar y dentro de esa página debemos fijarnos en algún elemento que nos indique que el producto se encuentra agotado por ejemplo un mensaje de 'producto no disponible'. Una vez lo localizemos debemos hacer click derecho y seleccionar la opción 'Inspeccionar'.
![image](https://user-images.githubusercontent.com/17747757/115062952-39410e00-9eeb-11eb-87df-d137a8214818.png)

Al inpeccionar ese elemento se nos resaltará una parte del código de la página (flecha roja) y debemos hacer click en los tres puntos que he rodeado en color verde en la siguiente imágen. Saldrán varias opciones y tenemos que seleccionar 'Copy' > 'Copy XPath'. Esto nos proporciona un identificador que usaremos en el código python. Por último también debes fijarte en el texto que hay dentro del elemento, que en este caso he subrayado en azul.
![image](https://user-images.githubusercontent.com/17747757/115063711-34c92500-9eec-11eb-9e21-c3caaa067c6a.png)

Si observas la última parte del código verás estas líneas, que son las más importantes y las únicas que debes entender para poner incluir más enlaces en los que buscar el producto.
```
  # EJEMPLO =================================================================================
  print('vvvvvvvvvv EJEMPLO vvvvvvvvvv')
  link_ejemplo = 'https://www.mediamarkt.es/es/product/_consola-sony-ps5-825-gb-4k-hdr-blanco-1487016.html'
  xpath_ejemplo = '//*[@id="root"]/div[2]/div[3]/div[1]/div/div[4]/div/div/div[3]/div/span'

  if ( S.texto_xpath(link_ejemplo, xpath_ejemplo) != 'Este artículo no está disponible actualmente.' ):
      mandar_correo('Disponible en: ' + link_ejemplo)
  # FIN EJEMPLO =================================================================================
```
Para añadir otra página para comprobar la disponibilidad tendrías que ir sustituyendo el enlace, el xpath y el texto del elemento. Para comprobar enlaces adicionales simplemente copia este bloque de código a continuación, respentando la misma tabulación. Al ejecutar el programa, cada cierto tiempo se abrirá chrome e irá abriendo los enlaces introducidos para comprobar si en el elemento indicado sigue teniendo el mismo mensaje de 'producto agotado' o el que sea. En caso de que no coincida te mandará un correo electrónico con el enlace en cuestión. Puedes ajustar el tiempo que pasa entre cada comprobación modificando el siguiente número, que por defecto está a una hora:
```
# Tiempo de refresco, en segundos
refresh_time = 3600
```
Puede haber avisos falsos en los que la página te bloquee porque haya detectado que haces demasiadas peticiones, se caiga la web u otras razones.
