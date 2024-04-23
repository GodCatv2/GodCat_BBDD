import json
import mysql.connector

# Leer el archivo JSON
ruta_al_archivo_json = '/var/www/server_lamp/datos_recibidos.json'
with open(ruta_al_archivo_json, 'r') as archivo:
    datos_json = json.load(archivo)

# Conectar a la base de datos MySQL
conexion = mysql.connector.connect(
    host='localhost',
    user='godcat2',
    password='Godcat_123',
    database='godcat2',
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Función para convertir listas a cadenas de texto
def convertir_a_cadena(valor):
    if isinstance(valor, list):
        return ', '.join(map(str, valor))  # Concatenar elementos de la lista
    else:
        return str(valor)  # Convertir otros tipos a cadenas de texto

# Funciones para obtener los valores del JSON y convertirlos a cadenas de texto
nombre_host = convertir_a_cadena(datos_json["Nombre_del_host"])
direccion_ipv4 = convertir_a_cadena(datos_json["Direccion_ipv4"])
mascara_subred = convertir_a_cadena(datos_json["Mascara_de_subred"])
direccion_ip_publica = convertir_a_cadena(datos_json["Direccion_ip_publica"])
direccion_mac = convertir_a_cadena(datos_json["Direccion_mac"])
dns = convertir_a_cadena(datos_json["DNS"])
sistema_operativo = convertir_a_cadena(datos_json["Sistema_operativo"])
pais = convertir_a_cadena(datos_json["Pais"])
region = convertir_a_cadena(datos_json["Region"])
ciudad = convertir_a_cadena(datos_json["Ciudad"])
zip = convertir_a_cadena(datos_json["ZIP"])
isp = convertir_a_cadena(datos_json["ISP"])
timezone = convertir_a_cadena(datos_json["Timezone"])
usuario = convertir_a_cadena(datos_json["Usuario"])

# Generar el código SQL con los datos del JSON utilizando parámetros
sql_code = """INSERT INTO info_json (
    nombre_host,
    direccion_ipv4,
    mascara_subred,
    direccion_ip_publica,
    direccion_mac,
    dns,
    sistema_operativo,
    pais,
    region,
    ciudad,
    zip,
    isp,
    timezone,
    usuario
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
);"""

try:
    # Ejecutar el código SQL con parámetros
    cursor.execute(sql_code, (
        nombre_host,
        direccion_ipv4,
        mascara_subred,
        direccion_ip_publica,
        direccion_mac,
        dns,
        sistema_operativo,
        pais,
        region,
        ciudad,
        zip,
        isp,
        timezone,
        usuario
    ))
    # Hacer commit de los cambios
    conexion.commit()
    print("Datos insertados exitosamente en la base de datos.")
except Exception as e:
    # Si hay algún error, hacer rollback de los cambios
    conexion.rollback()
    print(f"Error al insertar datos: {e}")

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
