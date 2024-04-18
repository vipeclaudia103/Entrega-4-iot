# Entrega-4-iot
**_Claudia Viñals Perlado_**

Repositorio para la entrega de la cuarta práctica en la asignatura de Desarrollo de aplicaciones IoT.



# Explicación de los pasos seguidos
## Leer archivo CSV línea a línea
Desarrollar un archivo de Python que lee el CSV de los datos línea a línea.
## Configurar entorno

### Instalar y Configurar InfluxDB 2.0 como servicio
La base de datos elegida para el proyecto es de series temporales ya que se adapta mejor para la casuística. Para instalar InfluxDB 2.0 como servicio:

```bash
# Ubuntu/Debian AMD64
curl -O https://dl.influxdata.com/influxdb/releases/influxdb2_2.7.5-1_amd64.deb
sudo dpkg -i influxdb2_2.7.5-1_amd64.deb
```

Iniciar el servicio
```bash
sudo service influxdb start
```
### Instalar y configurar Node-Red
Instalar Node-Red con Docker mediante el comando:
```bash
docker run -it -p 1880:1880 -v node_red_data:/data --name mynodered nodered/node-red
```


## Instalar librería de InfluxDB client
Para enviar los datos a InfluxDB es necesario instalar la librería de Python correspondiente.

```bash
pip3 install influxdb-client
```
## Crear token para el envío
Para poder acceder con todos los permisos para introducir datos, se necesita crear un token. Desde Influx en el apartado de tokens.
## Envío del archivo línea a línea a InfluxDB 2.0 por Python
### Completar las configuraciones de InfluxDB 2.0
Una vez instalado todo el entorno, se agrega la funcionalidad del envío de datos a InfluxDB. Para ello se completan las configuraciones de conexión que son las siguientes:
 - Organización: CVP
 - Bucket: Molinos
 - URL: http://172.28.141.208:8086/ (La IP del WSL donde está ejecutándose el InfluxDB)
 - Token 

### Enviar campos de la línea e introducir hora actual
Se utiliza el objeto Point y se rellenan los campos para el envío de los parámetros. Además, para poder identificar la turbina, se usa un tag "turbine_id" que indica si es la T1 o la T2.

## Configurar envío de datos por Node-Red
Para enviar datos continuamente sobre otra turbina, se realizan los siguientes pasos:
- Crear los datos de la turbina T2 con un archivo en JavaScript.
- Configurar JSON para el envío de datos.
- Configurar nodo de InfluxDB 2.0: Se completan los mismos campos que en el archivo de Python en las páginas.

## Crear dashboard para visualizar datos en InfluxDB.
Para visualizar la inserción correcta de los valores y hacer cálculos con ellos, se ha diseñado un dashboard:
- Se utilizan las variables de la tag "turbine_id" para ver las turbinas por separado.
- Se realizan sumas y derivadas de los datos.

# Instrucciones de uso
1. Instalar el entorno.
2. Crear un bucket en InfluxDB llamado “Molinos”.
3. Ejecutar el archivo “envio_T1.py”.
4. Encender el contenedor de Node-Red e importar el archivo “envio_T2.json”.
    a. Cambiar los datos necesarios para enviar a su InfluxDB deseado.
    b. Hacer un deploy.
5. Importar el dashboard con el archivo “lecturas_de_molinos.json”.

# Posibles vías de mejora
- Incluir encriptación de los datos de envío con TLS a InfluxDB.


# Problemas / Retos encontrados
- Creación de tokens funcionales.
- Dirección URL a InfluxDB de WSL. 

# Alternativas posibles

Utilizando Grafana y Prometheus conjuntamente porque pueden captar datos desde diferentes herramientas, dando mucha flexibilidad.

# Bibliografía
1. https://nodered.org/docs/getting-started/docker
2. https://www.timescale.com/learn/5-influxdb-alternatives-for-your-time-series-data
3. https://docs.influxdata.com/influxdb/cloud/visualize-data/variables/create-variable/
