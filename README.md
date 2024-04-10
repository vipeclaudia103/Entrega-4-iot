# Entrega-4-iot
Repositorio para la entrega de la cuarta práctica en la asignatura de Desarrollo de aplicaciones IOT

Miembros del equipo: Claudia Viñals

# Explicación de los pasos seguidos

## Instalar InfluxDB 2
Instalar InfluxDB 2.0 como servicio:

```bash
# Ubuntu/Debian AMD64
curl -O https://dl.influxdata.com/influxdb/releases/influxdb2_2.7.5-1_amd64.deb
sudo dpkg -i influxdb2_2.7.5-1_amd64.deb

```

Iniciar el serrvicio

```bash
sudo service influxdb start
```

token de influx:
```
SXzum1org1t_mYU5dxdPB7o9sQHLqtv3govXNySAFcmWNuQhwT4_PaooIeKmX2g3F0bHdzApWNenWx6sG9tErA==
```
Para guardar la varariable den token en el entorno ejecutar:
```bash
export INFLUXDB_TOKEN=hiwt2t-GCL8w6qS9HZFZ6oDfwqYUdRscZ3uX8urlPb_CBvW298IEE19zaeJU4JEEmc4LBWTuT2aR_bcAiA9p0g==
```

## Instalar libreria de InfluxDB client
Para enviar los datos a InfluxDB es necesario instalar la libreria de python correspondiente.

```bash
pip3 install influxdb-client
```

# Instrucciones de uso
# Posibles vías de mejora
# Problemas / Retos encontrados
# Alternativas posibles