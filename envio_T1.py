from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
import csv
import time


# Configuración de conexión a InfluxDB
token = "iH8lRT8epPlzBWGya3EkKwOCKEa2fSj9SAtTGY_ytNHwrye73hvakM98MDoe7He9sAYTO34jRzJgb8_QsvSVCg=="
org = "CVP"
bucket = "Molinos"
url = "http://localhost:8086"


client = InfluxDBClient(url=url, token=token,  org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Función para leer el archivo CSV y cargar los datos en InfluxDB
def load_csv_to_influxdb(csv_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Saltar la fila de encabezado
        for row in csv_reader:
            # Obtener el timestamp actual en formato UNIX en milisegundos
            timestamp = int(datetime.now().timestamp() * 1000)
            lv_active_power = float(row[1])  # Potencia activa LV (kW)
            wind_speed = float(row[2])  # Velocidad del viento (m/s)
            theoretical_power_curve = float(row[3])  # Curva de potencia teórica (KWh)
            wind_direction = float(row[4])  # Dirección del viento (°)
            
            # Crear un punto de datos
            point = Point("turbina") \
                    .time(timestamp, 'ms') \
                    .field("lv_active_power", lv_active_power) \
                    .field("wind_speed", wind_speed) \
                    .field("theoretical_power_curve", theoretical_power_curve) \
                    .field("wind_direction", wind_direction) \
                    .tag("Turbina", "T1")
                
            time.sleep(1)
            # Escribir el punto de datos en InfluxDB
            write_api.write(bucket=bucket, org=org, record=point)

# Ruta al archivo CSV
csv_file_path = "Entrega-4-iot/T1.csv"

# Cargar datos desde el archivo CSV a InfluxDB cada 10 minutos
while True:
    load_csv_to_influxdb(csv_file_path)
    print("Datos cargados en InfluxDB")
      # Esperar 10 minutos antes de cargar los datos nuevamente
