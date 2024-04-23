<?php
// Recibir los datos POST en formato JSON
$datos_json = file_get_contents("php://input");

// Decodificar los datos JSON a un array asociativo
$datos = json_decode($datos_json, true);

// Guardar los datos en un archivo JSON
$archivo = '/var/www/server_lamp/datos_recibidos.json';
file_put_contents($archivo, $datos_json);

// Imprimir respuesta para verificar que se han guardado los datos
echo "Datos recibidos y guardados en el archivo '$archivo'.";
?>
