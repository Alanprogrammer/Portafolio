-- phpMyAdmin SQL Dump
-- version 4.5.2
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 12-03-2016 a las 23:09:15
-- Versión del servidor: 10.1.10-MariaDB
-- Versión de PHP: 5.6.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `keylogger_Web`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_recibido`
--

CREATE TABLE `datos_recibido` (
  `id` int(11) NOT NULL,
  `ip` text NOT NULL,
  `fecha` text NOT NULL,
  `nombre_equipo` text NOT NULL,
  `data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `datos_recibido`
--

INSERT INTO `datos_recibido` (`id`, `ip`, `fecha`, `nombre_equipo`, `data`) VALUES
(1, '192.168.1.72', '2016/03/12|01:58:52', 'Alanprogrammer', '1921adminadminpepe clavo un clavo en la puta de un clavito pequeño okno eres un puto crack de mierda '),
(2, '192.168.1.72', '2016/03/12|02:00:03', 'Alanprogrammer', 'gg\r\r\r<h1\0>hola<\0/h1< [BACK SPACE] \0> <h1\0>hoa<\0/hola\0>\r<h1\0>hola<\0/h1\0> dddddddddddddddddddddddddddddd'),
(3, '192.168.1.72', '2016/03/12|02:01:18', 'Alanprogrammer', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
(4, '192.168.1.72', '2016/03/12|02:01:21', 'Alanprogrammer', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
(5, '192.168.1.72', '2016/03/12|02:01:24', 'Alanprogrammer', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
(6, '192.168.1.72', '2016/03/12|02:01:28', 'Alanprogrammer', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
(7, '192.168.1.72', '2016/03/12|02:01:31', 'Alanprogrammer', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
(8, '192.168.1.72', '2016/03/12|02:02:09', 'Alanprogrammer', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `datos_recibido`
--
ALTER TABLE `datos_recibido`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `datos_recibido`
--
ALTER TABLE `datos_recibido`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
