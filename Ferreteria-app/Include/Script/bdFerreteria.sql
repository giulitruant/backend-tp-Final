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
  `nroSolicitud` INT(11) NOT NULL AUTO_INCREMENT ,
  `dniCliente` INT(11) NOT NULL ,
  `precio_total` FLOAT NULL ,
  `fecha_solicitud` DATETIME NOT NULL ,
  PRIMARY KEY (`nroSolicitud`) ,
  INDEX `fkSolicitudCliente1Idx` (`dniCliente` ASC) ,
  CONSTRAINT `fkSolicitudCliente1`
    FOREIGN KEY (`dniCliente` )
    REFERENCES `bdferreteria`.`cliente` (`dni`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `bdferreteria`.`factura`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `bdferreteria`.`factura` (
  `idFactura` INT(11) NOT NULL AUTO_INCREMENT ,
  `total` FLOAT NOT NULL ,
  `tipo` VARCHAR(10) NOT NULL ,
  `forma_pago` VARCHAR(45) NOT NULL ,
  `nom_tarjeta` VARCHAR(50) NULL ,
  `cuenta` VARCHAR(50) NULL ,
  `num_tarjeta` VARCHAR(50) NULL ,
  `cant_cuotas` INT(11) NULL ,
  `nroSolicitud` INT(11) NULL ,
  PRIMARY KEY (`idFactura`) ,
  INDEX `fkFacturaSolicitud1Idx` (`nroSolicitud` ASC) ,
  CONSTRAINT `fkFacturaSolicitud1`
    FOREIGN KEY (`nroSolicitud` )
    REFERENCES `bdferreteria`.`solicitud` (`nroSolicitud` )
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
  `idProd` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(20) NOT NULL ,
  `precio_uni` FLOAT NOT NULL ,
  `cant_stock` INT(11) NULL DEFAULT NULL ,
  `cant_min` INT(11) NULL DEFAULT NULL ,
  `cuit` CHAR(20) NOT NULL ,
  PRIMARY KEY (`idProd`) ,
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
CREATE  TABLE IF NOT EXISTS `bdferreteria`.`solicitudDetalle` (
  `idDetalle` INT NOT NULL AUTO_INCREMENT ,
  `nroSolicitud` INT(11) NOT NULL ,
  `cantidad` FLOAT NULL ,
  `idProd` INT(11) NOT NULL ,
  PRIMARY KEY (`idDetalle`, `nroSolicitud`) ,
  INDEX `fkSolicitudDetalleSolicitud1_idx` (`nroSolicitud` ASC) ,
  INDEX `fkSolicitudDetalleProducto1_idx` (`idProd` ASC) ,
  CONSTRAINT `fkSolicitudDetalleSolicitud1`
    FOREIGN KEY (`nroSolicitud` )
    REFERENCES `bdferreteria`.`solicitud` (`nroSolicitud` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fkSolicitudDetalleProducto1`
    FOREIGN KEY (`idProd` )
    REFERENCES `bdferreteria`.`producto` (`idProd` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

USE `bdferreteria` ;
