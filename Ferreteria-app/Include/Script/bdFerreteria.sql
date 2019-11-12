SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `bdferreteria` DEFAULT CHARACTER SET utf8 ;
USE `bdferreteria` ;

-- -----------------------------------------------------
-- Table `bdferreteria`.`cliente`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `bdferreteria`.`cliente` (
  `dni` INT(11) NOT NULL ,
  `nombre` VARCHAR(20) NOT NULL ,
  `apellido` VARCHAR(20) NOT NULL ,
  `tel` VARCHAR(20) NULL DEFAULT NULL ,
  `email` VARCHAR(50) NULL DEFAULT NULL ,
  `direccion` VARCHAR(50) NULL DEFAULT NULL ,
  PRIMARY KEY (`dni`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `bdferreteria`.`solicitud`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `bdferreteria`.`solicitud` (
  `nro_solicitud` INT(11) NOT NULL AUTO_INCREMENT ,
  `dni_cliente` INT(11) NOT NULL ,
  `precio_total` FLOAT NULL ,
  `fecha_solicitud` DATETIME NOT NULL ,
  PRIMARY KEY (`nro_solicitud`) ,
  INDEX `fk_solicitud_cliente1_idx` (`dni_cliente` ASC) ,
  CONSTRAINT `fk_solicitud_cliente1`
    FOREIGN KEY (`dni_cliente` )
    REFERENCES `bdferreteria`.`cliente` (`dni` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `bdferreteria`.`factura`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `bdferreteria`.`factura` (
  `id_factura` INT(11) NOT NULL AUTO_INCREMENT ,
  `total` FLOAT NOT NULL ,
  `tipo` VARCHAR(10) NOT NULL ,
  `forma_pago` VARCHAR(45) NOT NULL ,
  `nom_tarjeta` VARCHAR(50) NULL ,
  `cuenta` VARCHAR(50) NULL ,
  `num_tarjeta` VARCHAR(50) NULL ,
  `cant_cuotas` INT(11) NULL ,
  `nro_solicitud` INT(11) NULL ,
  PRIMARY KEY (`id_factura`) ,
  INDEX `fk_factura_solicitud1_idx` (`nro_solicitud` ASC) ,
  CONSTRAINT `fk_factura_solicitud1`
    FOREIGN KEY (`nro_solicitud` )
    REFERENCES `bdferreteria`.`solicitud` (`nro_solicitud` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `bdferreteria`.`proveedor`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `bdferreteria`.`proveedor` (
  `cuit` CHAR(20) NOT NULL ,
  `nombre` VARCHAR(20) NOT NULL ,
  `apellido` VARCHAR(20) NOT NULL ,
  `tel` VARCHAR(20) NULL DEFAULT NULL ,
  `email` VARCHAR(50) NULL DEFAULT NULL ,
  `direccion` VARCHAR(50) NULL DEFAULT NULL ,
  PRIMARY KEY (`cuit`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `bdferreteria`.`producto`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `bdferreteria`.`producto` (
  `id_prod` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(20) NOT NULL ,
  `precio_uni` FLOAT NOT NULL ,
  `cant_stock` INT(11) NULL DEFAULT NULL ,
  `cant_min` INT(11) NULL DEFAULT NULL ,
  `cuit` CHAR(20) NOT NULL ,
  PRIMARY KEY (`id_prod`) ,
  INDEX `cuit` (`cuit` ASC) ,
  CONSTRAINT `producto_fk`
    FOREIGN KEY (`cuit` )
    REFERENCES `bdferreteria`.`proveedor` (`cuit` )
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `bdferreteria`.`solicitud_detalle`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `bdferreteria`.`solicitud_detalle` (
  `idDetalle` INT NOT NULL AUTO_INCREMENT ,
  `nroSolicitud` INT(11) NOT NULL ,
  `cantidad` FLOAT NULL ,
  `idProd` INT(11) NOT NULL ,
  PRIMARY KEY (`idDetalle`, `nroSolicitud`) ,
  INDEX `fk_Solicitud_Detalle_solicitud1_idx` (`nroSolicitud` ASC) ,
  INDEX `fk_Solicitud_Detalle_producto1_idx` (`idProd` ASC) ,
  CONSTRAINT `fk_Solicitud_Detalle_solicitud1`
    FOREIGN KEY (`nroSolicitud` )
    REFERENCES `bdferreteria`.`solicitud` (`nro_solicitud` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Solicitud_Detalle_producto1`
    FOREIGN KEY (`idProd` )
    REFERENCES `bdferreteria`.`producto` (`id_prod` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `bdferreteria` ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
