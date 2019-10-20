# SQL Manager 2005 Lite for MySQL 3.7.0.1
# ---------------------------------------
# Host     : localhost
# Port     : 3306
# Database : afatse


SET FOREIGN_KEY_CHECKS=0;

DROP DATABASE IF EXISTS `BDFerreteria`;

CREATE DATABASE `BDFerreteria`
    CHARACTER SET 'utf8'
    COLLATE 'utf8_general_ci';

USE `BDFerreteria`;

#
# Structure for the `alumnos` table :
#

DROP TABLE IF EXISTS `cliente`;

CREATE TABLE `cliente` (
  `dni` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `apellido` varchar(20) NOT NULL,
  `tel` varchar(20) default NULL,
  `email` varchar(50) default NULL,
  `direccion` varchar(50) default NULL,
  PRIMARY KEY  (`dni`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Structure for the `plan_capacitacion` table :
#

DROP TABLE IF EXISTS `proveedor`;

CREATE TABLE `proveedor` (
  `cuit` char(20) NOT NULL ,
  `nombre` varchar(20) NOT NULL,
  `apellido` varchar(20) NOT NULL,
  `tel` varchar(20) default NULL,
  `email` varchar(50) default NULL,
  `direccion` varchar(50) default NULL,
  PRIMARY KEY  (`cuit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Structure for the `personas` table : 
#

DROP TABLE IF EXISTS `producto`;

CREATE TABLE `producto` (
  `id_prod` int(11) NOT NULL,
  `descripcion` varchar(20) NOT NULL,
  `precio_uni` float NOT NULL,
  `cant_stock` int(11) default NULL,
  `cant_min` int(11) default NULL,
  `cuit` char(20) NOT NULL ,
  PRIMARY KEY  (`id_prod`),
  KEY `cuit` (`cuit`),
  CONSTRAINT `producto_fk` FOREIGN KEY (`cuit`) REFERENCES `proveedor` (`cuit`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Structure for the `cuotas` table :
#

DROP TABLE IF EXISTS `remito`;

CREATE TABLE `remito` (
	`nro_remito` int(11) NOT NULL AUTO_INCREMENT,
	`nombre` varchar(50) NOT NULL,
	`apellido` varchar(50) NOT NULL,
	`telefono` varchar(20) default NULL,
	`direccion` varchar(50) default NULL,
    `id_prod` int(11) NOT NULL,
  PRIMARY KEY  (`nro_remito`),
  KEY `id_prod` (`id_prod`),
  CONSTRAINT `remito_fk` FOREIGN KEY (`id_prod`) REFERENCES `producto` (`id_prod`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Structure for the `inscripciones` table :
#

DROP TABLE IF EXISTS `factura`;

CREATE TABLE `factura` (
  `id_factura` int(11) NOT NULL AUTO_INCREMENT,
  `total` float NOT NULL,
  `tipo` varchar(10) NOT NULL,
  `nom_tarjeta` varchar(50) NOT NULL,
  `cuenta` varchar(50) NOT NULL,
  `num_tarjeta` varchar(50) NOT NULL,
  `cant_cuotas` int(11) NOT NULL,
  `id_prod` int(11) NOT NULL,
  KEY `id_prod` (`id_prod`),
  PRIMARY KEY  (`id_factura`),  
  CONSTRAINT `factura_prod_fk` FOREIGN KEY (`id_prod`) REFERENCES `Producto` (`id_prod`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Structure for the `cursos_horarios` table :
#

DROP TABLE IF EXISTS `solicitud`;

CREATE TABLE `solicitud` (
	`nro_solicitud` int(11) NOT NULL AUTO_INCREMENT,
  `id_prod` int(11) NOT NULL,
  `cant_pedida` varchar(50) default NULL,
  `nro_remito` int(11) NOT NULL,
  PRIMARY KEY  (`nro_solicitud`),
  KEY `id_prod` (`id_prod`),
  KEY `nro_remito` (`nro_remito`),
  CONSTRAINT `solicitud_prod_fk` FOREIGN KEY (`id_prod`) REFERENCES `Producto` (`id_prod`) ON UPDATE CASCADE,
  CONSTRAINT `solicitud_rem_fk` FOREIGN KEY (`nro_remito`) REFERENCES `Remito` (`nro_remito`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `bdferreteria`.`proveedor`
(`cuit`,
`nombre`,
`apellido`,
`tel`,
`email`,
`direccion`)
VALUES
('11123654783',
'pepito',
'gonzales',
'112233',
'pgonzales@gmail.com',
'mariquita sanchez 61');


INSERT INTO `bdferreteria`.`producto`
(`id_prod`,
`descripcion`,
`precio_uni`,
`cant_stock`,
`cant_min`,
`cuit`)
VALUES
(
1,
'tornillos 15mm',
1.5,
500000,
5000,
'11123654783');