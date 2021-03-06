-- MySQL Script generated by MySQL Workbench
-- Mon Nov  9 19:39:05 2015
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema login_register_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema login_register_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `login_register_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `login_register_db` ;

-- -----------------------------------------------------
-- Table `login_register_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `login_register_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `first_name` VARCHAR(255) NULL COMMENT '',
  `last_name` VARCHAR(255) NULL COMMENT '',
  `email` VARCHAR(255) NULL COMMENT '',
  `pw_hash` VARCHAR(255) NULL COMMENT '',
  `created_at` DATETIME NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
