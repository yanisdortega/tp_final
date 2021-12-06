-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.21-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Volcando estructura para tabla databasename.carrito
CREATE TABLE IF NOT EXISTS `carrito` (
  `CarritoID` int(11) NOT NULL AUTO_INCREMENT,
  `Usuarios_id` int(11) DEFAULT NULL,
  `Productos_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`CarritoID`),
  KEY `Usuarios_id` (`Usuarios_id`),
  KEY `Productos_id` (`Productos_id`),
  CONSTRAINT `carrito_ibfk_1` FOREIGN KEY (`Usuarios_id`) REFERENCES `usuarios` (`UsuariosID`),
  CONSTRAINT `carrito_ibfk_2` FOREIGN KEY (`Productos_id`) REFERENCES `productos` (`ProductosID`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla databasename.carrito: ~11 rows (aproximadamente)
/*!40000 ALTER TABLE `carrito` DISABLE KEYS */;
INSERT INTO `carrito` (`CarritoID`, `Usuarios_id`, `Productos_id`) VALUES
	(2, 5, 4),
	(3, 13, 19),
	(6, 13, 19),
	(11, 13, 19),
	(22, 5, 16),
	(24, 13, 19),
	(25, 13, 19),
	(26, 13, 19),
	(27, 13, 19),
	(28, 13, 7);
/*!40000 ALTER TABLE `carrito` ENABLE KEYS */;

-- Volcando estructura para tabla databasename.categorias
CREATE TABLE IF NOT EXISTS `categorias` (
  `CategoriasID` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` text DEFAULT NULL,
  PRIMARY KEY (`CategoriasID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla databasename.categorias: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` (`CategoriasID`, `Nombre`) VALUES
	(1, 'Insumos librería'),
	(2, 'Ropa y moda'),
	(3, 'Ropa niños'),
	(4, 'Accesorios'),
	(5, 'Electrónica'),
	(6, 'Calzados');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;

-- Volcando estructura para tabla databasename.ciudad
CREATE TABLE IF NOT EXISTS `ciudad` (
  `CiudadID` int(11) NOT NULL AUTO_INCREMENT,
  `NombreCiudad` varchar(40) DEFAULT NULL,
  `Provincia_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`CiudadID`),
  KEY `Provincia_id` (`Provincia_id`),
  CONSTRAINT `ciudad_ibfk_1` FOREIGN KEY (`Provincia_id`) REFERENCES `provincia` (`ProvinciaID`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla databasename.ciudad: ~11 rows (aproximadamente)
/*!40000 ALTER TABLE `ciudad` DISABLE KEYS */;
INSERT INTO `ciudad` (`CiudadID`, `NombreCiudad`, `Provincia_id`) VALUES
	(1, 'CABA', 1),
	(2, 'Rosario', 5),
	(3, 'Santa Rosa', 8),
	(9, 'Edimburgo', 84),
	(11, 'La Serena', 80),
	(12, 'Carmelo', 75),
	(15, 'Montevideo', 77),
	(24, 'Tupiza', 11),
	(30, 'Guayaquil', 30),
	(45, 'Ciudad del Este', 12),
	(71, 'Barcelona', 96);
/*!40000 ALTER TABLE `ciudad` ENABLE KEYS */;

-- Volcando estructura para vista databasename.comprasusuarios
-- Creando tabla temporal para superar errores de dependencia de VIEW
CREATE TABLE `comprasusuarios` 
) ENGINE=MyISAM;

-- Volcando estructura para tabla databasename.factura
CREATE TABLE IF NOT EXISTS `factura` (
  `FacturaID` int(11) NOT NULL AUTO_INCREMENT,
  `FechaEmision` datetime DEFAULT NULL,
  `Carrito_id` int(11) DEFAULT NULL,
  `Mediodepago_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`FacturaID`),
  KEY `Carrito_id` (`Carrito_id`),
  CONSTRAINT `factura_ibfk_1` FOREIGN KEY (`Carrito_id`) REFERENCES `carrito` (`CarritoID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla databasename.factura: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
INSERT INTO `factura` (`FacturaID`, `FechaEmision`, `Carrito_id`, `Mediodepago_id`) VALUES
	(4, '2021-12-06 14:22:37', 2, 2),
	(5, '2021-12-06 14:23:30', 3, 1),
	(6, '2021-12-06 14:28:53', 3, 4),
	(8, '2021-12-06 14:55:58', 3, 2),
	(9, '2021-12-06 15:00:26', 3, 1);
/*!40000 ALTER TABLE `factura` ENABLE KEYS */;

-- Volcando estructura para vista databasename.itemscarrito
-- Creando tabla temporal para superar errores de dependencia de VIEW
CREATE TABLE `itemscarrito` (
	`Productos_id` INT(11) NULL,
	`Nombre` TEXT(65535) NULL COLLATE 'latin1_swedish_ci',
	`Precio` FLOAT(12) NULL,
	`Usuarios_id` INT(11) NULL
) ENGINE=MyISAM;

-- Volcando estructura para tabla databasename.marcas
CREATE TABLE IF NOT EXISTS `marcas` (
  `MarcasID` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`MarcasID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla databasename.marcas: ~8 rows (aproximadamente)
/*!40000 ALTER TABLE `marcas` DISABLE KEYS */;
INSERT INTO `marcas` (`MarcasID`, `Nombre`) VALUES
	(1, 'TI electronics'),
	(2, 'Flor de loto'),
	(3, 'Youkai Kei'),
	(4, 'Hey!'),
	(5, 'DoomDom'),
	(6, 'Librería Perlita'),
	(7, 'Lady Stonk'),
	(8, 'Arañita');
/*!40000 ALTER TABLE `marcas` ENABLE KEYS */;

-- Volcando estructura para tabla databasename.mediopago
CREATE TABLE IF NOT EXISTS `mediopago` (
  `medioPagoID` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`medioPagoID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla databasename.mediopago: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `mediopago` DISABLE KEYS */;
INSERT INTO `mediopago` (`medioPagoID`, `Nombre`) VALUES
	(1, 'EFECTIVO'),
	(2, 'TARJETA DEBITO'),
	(3, 'TARJETA CREDITO'),
	(4, 'DEPOSITO BANCARIO'),
	(5, 'PAGO ELECTRONICO');
/*!40000 ALTER TABLE `mediopago` ENABLE KEYS */;

-- Volcando estructura para vista databasename.mostrarciudad
-- Creando tabla temporal para superar errores de dependencia de VIEW
CREATE TABLE `mostrarciudad` (
	`nombrePais` VARCHAR(40) NULL COLLATE 'latin1_swedish_ci',
	`nombreProvincia` VARCHAR(40) NULL COLLATE 'latin1_swedish_ci',
	`nombreCiudad` VARCHAR(40) NULL COLLATE 'latin1_swedish_ci',
	`CiudadID` INT(11) NOT NULL
) ENGINE=MyISAM;

-- Volcando estructura para tabla databasename.pais
CREATE TABLE IF NOT EXISTS `pais` (
  `PaisID` int(11) NOT NULL AUTO_INCREMENT,
  `NombrePais` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`PaisID`)
) ENGINE=InnoDB AUTO_INCREMENT=599 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla databasename.pais: ~9 rows (aproximadamente)
/*!40000 ALTER TABLE `pais` DISABLE KEYS */;
INSERT INTO `pais` (`PaisID`, `NombrePais`) VALUES
	(33, 'Paraguay'),
	(34, 'España'),
	(49, 'Alemania'),
	(50, 'Chile'),
	(54, 'Argentina'),
	(62, 'Bolivia'),
	(100, 'Ecuador'),
	(352, 'Reino Unido'),
	(598, 'Uruguay');
/*!40000 ALTER TABLE `pais` ENABLE KEYS */;

-- Volcando estructura para tabla databasename.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `ProductosID` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` text DEFAULT NULL,
  `Modelo` text DEFAULT NULL,
  `Precio` float DEFAULT NULL,
  `Puntuacion` float DEFAULT NULL,
  `Marcas_id` int(11) DEFAULT NULL,
  `Categorias_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`ProductosID`),
  KEY `Marcas_id` (`Marcas_id`),
  KEY `Categorias_id` (`Categorias_id`),
  CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`Marcas_id`) REFERENCES `marcas` (`MarcasID`) ON DELETE SET NULL ON UPDATE SET NULL,
  CONSTRAINT `productos_ibfk_2` FOREIGN KEY (`Categorias_id`) REFERENCES `categorias` (`CategoriasID`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla databasename.productos: ~19 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` (`ProductosID`, `Nombre`, `Modelo`, `Precio`, `Puntuacion`, `Marcas_id`, `Categorias_id`) VALUES
	(1, 'Remera estampada', 'remes', 1500, 7, 5, 2),
	(2, 'Riñonera', 'R400', 2400, 9.9, 4, 4),
	(3, 'Zapatos bebe', 'albe', 800, 9.8, 2, 3),
	(4, 'Cartera', 'cartera ecocuero', 7500, 10, 4, 4),
	(5, 'Musculosa top', 'espalda descubierta', 952, 6, 5, 2),
	(6, 'Bralette', 'br7', 1350, 9.6, 4, 2),
	(7, 'Parche', 'gogo', 150, 9, 4, 4),
	(8, 'Libreta agenda', 'musical', 890, 8, 6, 1),
	(9, 'Campera bell', 'gigante', 7890, 9, 7, 2),
	(10, 'Zapatos con taco', 'LS 1', 9999, 8.3, 7, 6),
	(11, 'Tableta digitalizadora', 'gen 760', 12899, 10, 1, 5),
	(12, 'Balanza alimentos', '10 kg', 1950, 7.89, 1, 5),
	(13, 'Notebook A4', 'sublimado', 310, 7, 1, 1),
	(14, 'Pijama onesie', 'Kigurumi', 5200, 10, 3, 2),
	(15, 'Conjunto pijama', 'set 8', 2300, 10, 7, 2),
	(16, 'Medias', 'z333', 400, 8, 8, 2),
	(17, 'Pantufla bebe', 'Panpolar', 750, 10, 2, 3),
	(18, 'Mochila con compartimiento', 'Black001', 11099, 9.9, 4, 4),
	(19, NULL, NULL, NULL, NULL, NULL, NULL);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

-- Volcando estructura para tabla databasename.provincia
CREATE TABLE IF NOT EXISTS `provincia` (
  `ProvinciaID` int(11) NOT NULL AUTO_INCREMENT,
  `NombreProvincia` varchar(40) DEFAULT NULL,
  `Pais_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`ProvinciaID`),
  KEY `Pais_id` (`Pais_id`),
  CONSTRAINT `provincia_ibfk_1` FOREIGN KEY (`Pais_id`) REFERENCES `pais` (`PaisID`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla databasename.provincia: ~14 rows (aproximadamente)
/*!40000 ALTER TABLE `provincia` DISABLE KEYS */;
INSERT INTO `provincia` (`ProvinciaID`, `NombreProvincia`, `Pais_id`) VALUES
	(1, 'CABA', 54),
	(5, 'Santa Fé', 54),
	(8, 'La Pampa', 54),
	(9, 'Lothian', 352),
	(11, 'Elqui', 50),
	(12, 'Alto Paraná', 33),
	(24, 'Sud Chichas', 62),
	(30, 'Guayas', 100),
	(45, 'Alto Paraná', 33),
	(75, 'Colonia', 598),
	(77, 'Montevideo', 598),
	(80, 'Coquimbo', 50),
	(84, 'Escocia', 352),
	(96, 'Cataluña', 34);
/*!40000 ALTER TABLE `provincia` ENABLE KEYS */;

-- Volcando estructura para tabla databasename.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `UsuariosID` int(11) NOT NULL AUTO_INCREMENT,
  `Nombres` varchar(40) DEFAULT NULL,
  `Apellidos` varchar(40) DEFAULT NULL,
  `Fecha_de_nacimiento` date DEFAULT NULL,
  `Mail` varchar(40) DEFAULT NULL,
  `Contrasena` varchar(40) DEFAULT NULL,
  `Telefono` int(11) DEFAULT NULL,
  `Ciudad_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`UsuariosID`),
  KEY `Ciudad_id` (`Ciudad_id`),
  CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`Ciudad_id`) REFERENCES `ciudad` (`CiudadID`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla databasename.usuarios: ~23 rows (aproximadamente)
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`UsuariosID`, `Nombres`, `Apellidos`, `Fecha_de_nacimiento`, `Mail`, `Contrasena`, `Telefono`, `Ciudad_id`) VALUES
	(1, 'Aída', 'Oriana', '1998-03-20', 'aidisaidis@mail.com', 'MS1Db3Ju', 1177584415, 1),
	(2, 'Salomón', 'Cuo', '1991-05-05', 'salomoncuo@mail.com', 'NzEqRmVlZw==', 1111154871, 11),
	(3, 'Estefanía', 'Quinteros', '1983-02-14', 'este@mail.com', 'RmVybmFucG8/NTM=', 1526996333, 71),
	(4, 'María', 'Solano', '1974-08-20', 'mariasola@mail.com', 'MTgyQjchZQ==', 1199588466, 30),
	(5, 'Leandro', 'Ortega', '1959-09-05', 'ortegal@mail.com', 'T3JvNzAk', 1154568655, 45),
	(6, 'Nicolás', 'Conde', '2002-10-09', 'niconico@mail.com', 'QXYmJlNhdHVybmkzMA==', 1124594888, 9),
	(7, 'Marcos', 'Sola', '1963-01-01', 'marcolsa@mail.com', 'JSVDRW5HaTMyNA==', 1164545635, 3),
	(8, 'Giuliano', 'Rosas', '1996-12-25', 'giuri@mail.com', 'LVJzZDE1My0=', 1112468762, 24),
	(9, 'Camilo', 'Sesto', '1946-09-16', 'camsesto@mail.com', 'JiYxQ2FtU2VzdG8=', 1166588897, 71),
	(12, 'Lady', 'Gaga', '1982-01-01', 'ladygaga@mail.com', 'LTFMYWR5JiY=', 1152055655, 71),
	(13, 'Yanina', 'Ortega', '1996-08-16', 'al.degaan@mail.com', 'LVlhbmluYXMxNjA4', 1128678233, 1),
	(14, 'Magdalena Maria', 'Vasvaldo', '1963-08-08', 'vavaldo3015@mail.com', 'I01hcm80Njc5', 1163081089, 1),
	(15, 'Fernando Maximo', 'Rodriguez', '1996-09-09', 'dferrero@mail.com', 'LU5vdG1lJiY5OQ==', 1154255888, 2),
	(16, 'Ana María', 'Casanova', '1946-08-16', 'moriacasan@mail.com', 'JCRMYU9uZTE=', 1176058499, 1),
	(18, 'Esperanza', 'Sosa', '1990-11-27', 'espe@mail.com', 'QEVzcGUxMjM=', 1149587433, 30),
	(19, 'Elizabeth', 'Woolridge Grant', '1985-06-21', 'lanadelrey@mail.com', 'JUxhbmExMjM=', 1145628499, 9),
	(20, 'Jeffrey Preston', 'Bezos', '1964-01-12', 'amazon@mail.com', 'JCRBbWF6b242NjY=', 1159896455, 9),
	(21, 'Steven Vincent', 'Buscemi', '1957-12-13', 'stevebuscemi@mail.com', 'wr9TdGV2ZTE3NT8=', 1175131219, 15),
	(22, 'Brandon', 'Sanderson', '1975-12-19', 'bransanderson@mail.com', 'MTkqKlNhbmRlcnNvbg==', 1132006197, 9),
	(24, 'Juan', 'Paredes', '1992-08-30', 'juanparedes@mail.com', 'LUp1YW5jaG9zMTIl', 1123458903, 2),
	(25, 'Christina Maria', 'Aguilera', '1980-12-18', 'aguilera@mail.com', 'JCQxTWlsbGlvbmRvbGxhcg==', 1157983289, 9),
	(26, 'Gwen Renée', 'Stefani', '1969-10-03', 'gwen@mail.com', 'KipnV2VuMzQ=', 1168594856, 71),
	(27, 'Pepe', 'Picas', '1978-05-14', 'pepepicas@mail.com', 'IyNQZXBlOTk=', 1159485623, 45);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;


-- Volcando estructura para vista databasename.itemscarrito
-- Eliminando tabla temporal y crear estructura final de VIEW
DROP TABLE IF EXISTS `itemscarrito`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `itemscarrito` AS SELECT carrito.Productos_id, productos.Nombre, productos.Precio, carrito.Usuarios_id
FROM  carrito, productos
WHERE productos.ProductosID=carrito.Productos_id ;

-- Volcando estructura para vista databasename.mostrarciudad
-- Eliminando tabla temporal y crear estructura final de VIEW
DROP TABLE IF EXISTS `mostrarciudad`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `mostrarciudad` AS SELECT nombrePais, nombreProvincia, nombreCiudad, ciudad.CiudadID
FROM pais, provincia, ciudad
WHERE pais.PaisID=provincia.Pais_id
AND provincia.ProvinciaID=ciudad.Provincia_id ;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
