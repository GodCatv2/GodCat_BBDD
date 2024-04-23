-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 18-04-2024 a las 07:54:50
-- Versión del servidor: 8.0.36-0ubuntu0.22.04.1
-- Versión de PHP: 8.1.2-1ubuntu2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `godcat2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `info_json`
--

CREATE TABLE `info_json` (
  `id` int NOT NULL,
  `nombre_host` varchar(255) DEFAULT NULL,
  `direccion_ipv4` varchar(15) DEFAULT NULL,
  `mascara_subred` varchar(15) DEFAULT NULL,
  `direccion_ip_publica` varchar(15) DEFAULT NULL,
  `direccion_mac` varchar(17) DEFAULT NULL,
  `dns` varchar(255) DEFAULT NULL,
  `sistema_operativo` varchar(255) DEFAULT NULL,
  `version_sistema` varchar(255) DEFAULT NULL,
  `pais` varchar(50) DEFAULT NULL,
  `region` varchar(50) DEFAULT NULL,
  `ciudad` varchar(50) DEFAULT NULL,
  `zip` varchar(10) DEFAULT NULL,
  `isp` varchar(255) DEFAULT NULL,
  `timezone` varchar(50) DEFAULT NULL,
  `usuario` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `info_json`
--

INSERT INTO `info_json` (`id`, `nombre_host`, `direccion_ipv4`, `mascara_subred`, `direccion_ip_publica`, `direccion_mac`, `dns`, `sistema_operativo`, `version_sistema`, `pais`, `region`, `ciudad`, `zip`, `isp`, `timezone`, `usuario`) VALUES
(1, 'PC18479', '100.77.20.56', '255.0.0.0', '84.76.250.178', '90:8d:6e:62:63:e2', '100.77.20.56, 192.168.56.1', 'Windows, 10.0.19045, Windows-10-10.0.19045-SP0, [\'64bit\', \'WindowsPE\']', NULL, 'ES', 'Madrid', 'Madrid', '28004', 'AS12479 Orange Espagne SA', 'Europe/Madrid', 'Alumno'),
(2, 'PC18475', '100.77.20.31', '255.0.0.0', '84.76.250.178', '90:8d:6e:62:63:57', '100.77.20.31, 192.168.56.1, 192.168.5.1', 'Windows, 10.0.19045, Windows-10-10.0.19045-SP0, [\'64bit\', \'WindowsPE\']', NULL, 'ES', 'Madrid', 'Madrid', '28004', 'AS12479 Orange Espagne SA', 'Europe/Madrid', 'Alumno');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `info_json`
--
ALTER TABLE `info_json`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `info_json`
--
ALTER TABLE `info_json`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
