# MercadoPago
  
Modulo para trabajar con MercadoPago  

*Read this in other languages: [English](Manual_MercadoPago.md), [Español](Manual_MercadoPago.es.md).*
  
![banner](imgs/Banner_MercadoPago.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Acceso
  
Ingrese el token de acceso
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Token de Acceso|Token de acceso de MercadoPago|token|

### Buscar pagos
  
Obtenga los identificadores de todos los pagos
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de referencia externa|ID de referencia externa del pago|id|
|Criterios|Criterios de búsqueda|criterio|
|Ordenar|Ordenar por|sort|
|Variable|Variable donde se guardarán los resultados|resultado|

### Obtener Pago
  
Obtiene detalles del pago desde un id obtenido en el comando buscar pagos
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de pago|ID del pago a buscar|id|
|Variable|Variable donde se almacenará el resultado|result|
