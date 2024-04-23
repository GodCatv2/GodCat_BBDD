<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Información de Hosts</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0; /* Añadido margen superior e inferior */
            border: 2px solid #ccc; /* Añadido borde */
        }
        th, td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
            border-right: 1px solid #ddd; /* Añadido borde derecho */
        }
        th {
            background-color: #4ad626; /* Cambiado a verde */
            color: white; /* Cambiado el color del texto a blanco */
        }

        h2 {
            text-align: center;
            margin-bottom: 20px;
        }

        td:nth-child(odd) {
            background-color: transparent; /* Quitado el color de fondo de las columnas */
        }

        .hidden {
            display: none;
        }

        /* Estilo específico para la segunda tabla */
        #detailedTable th {
            background-color: #30f530; /* Cambiado a un tono de verde más claro */
        }

        /* Efecto de difuminado al pasar el cursor sobre una fila */
        .hostRow:hover {
            opacity: 0.3; /* Opacidad reducida */
        }
    </style>
</head>
<body>

<h2>Viewer godcat2 Grid</h2>

<table id="hostTable">
    <tr>
        <th>Nombre del Host</th>
        <th>Direccion IPv4</th>
        <th>Direccion IP Publica</th>
        <th>Direccion MAC</th>
        <th>Pais</th>
        <th>Region</th>
        <th>Ciudad</th>
    </tr>

    <?php
    // Conexión a la base de datos
    $servername = "localhost"; // Cambia esto si tu servidor MySQL no está en localhost
    $username = "godcat2";
    $password = "Godcat_123";
    $dbname = "godcat2";

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Conexión fallida: " . $conn->connect_error);
    }

    // Consulta SQL para seleccionar solo los campos necesarios
    $sql = "SELECT * FROM info_json";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Mostrar los datos de cada fila
        while($row = $result->fetch_assoc()) {
            echo "<tr class='hostRow'>";
            echo "<td>" . $row["nombre_host"] . "</td>";
            echo "<td>" . $row["direccion_ipv4"] . "</td>";
            echo "<td>" . $row["direccion_ip_publica"] . "</td>";
            echo "<td>" . $row["direccion_mac"] . "</td>";
            echo "<td>" . $row["pais"] . "</td>";
            echo "<td>" . $row["region"] . "</td>";
            echo "<td>" . $row["ciudad"] . "</td>";
            echo "<td class='hiddenData' style='display: none;'>" . htmlspecialchars(json_encode($row)) . "</td>"; // Datos ocultos
            echo "</tr>";
        }
    } else {
        echo "0 resultados";
    }
    $conn->close();
    ?>
</table>

<div id="detailedInfo" class="hidden">
    <h3>Información detallada</h3>
    <table id="detailedTable">
        <tr id="columnNames">
            <th>Nombre del Host</th>
            <th>Direccion IPv4</th>
            <th>Mascara de Subred</th>
            <th>Direccion IP Publica</th>
            <th>Direccion MAC</th>
            <th>DNS</th>
            <th>Sistema Operativo</th>
            <th>Pais</th>
            <th>Region</th>
            <th>Ciudad</th>
            <th>Codigo Postal</th>
            <th>ISP</th>
            <th>Zona Horaria</th>
            <th>Usuario</th>
        </tr>
    </table>
</div>

<script>
    const hostRows = document.querySelectorAll('.hostRow');
    const detailedInfo = document.getElementById('detailedInfo');
    const detailedTable = document.getElementById('detailedTable');

    hostRows.forEach(row => {
        row.addEventListener('click', () => {
            const hiddenData = row.querySelector('.hiddenData').textContent;
            const rowData = JSON.parse(hiddenData);

            detailedTable.innerHTML = ''; // Limpiar la tabla detallada

            // Agregar fila para los nombres de las columnas
            const columnNamesRow = document.createElement('tr');
            Object.keys(rowData).forEach(key => {
                const columnNameCell = document.createElement('th');
                columnNameCell.textContent = key;
                columnNamesRow.appendChild(columnNameCell);
            });
            detailedTable.appendChild(columnNamesRow);

            // Agregar fila con los datos de la fila seleccionada
            const newRow = document.createElement('tr');
            Object.values(rowData).forEach(value => {
                const cell = document.createElement('td');
                cell.textContent = value;
                newRow.appendChild(cell);
            });
            detailedTable.appendChild(newRow);

            detailedInfo.classList.remove('hidden');
        });
    });
</script>

</body>
</html>
