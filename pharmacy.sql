-- MySQL dump 10.13  Distrib 8.3.0, for Win64 (x86_64)
--
-- Host: localhost    Database: pharmacy
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `batch`
--

DROP TABLE IF EXISTS `batch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `batch` (
  `Batch_id` int NOT NULL,
  `Batch_timestamp` timestamp NULL DEFAULT NULL,
  `Supplier_id` int DEFAULT NULL,
  `Med_id` int DEFAULT NULL,
  `Batch_qty` int DEFAULT NULL,
  `Batch_expiry` date DEFAULT NULL,
  PRIMARY KEY (`Batch_id`),
  KEY `Supplier_id` (`Supplier_id`),
  KEY `Med_id` (`Med_id`),
  CONSTRAINT `batch_ibfk_1` FOREIGN KEY (`Supplier_id`) REFERENCES `supplier` (`Supplier_id`),
  CONSTRAINT `batch_ibfk_2` FOREIGN KEY (`Med_id`) REFERENCES `medicine` (`Med_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `batch`
--

LOCK TABLES `batch` WRITE;
/*!40000 ALTER TABLE `batch` DISABLE KEYS */;
INSERT INTO `batch` VALUES (101,'2024-03-10 06:36:40',101,101,389,'2025-03-10'),(102,'2024-03-10 06:37:10',102,102,294,'2025-03-09'),(103,'2024-03-10 06:38:11',103,103,188,'2025-03-08'),(104,'2024-03-10 06:38:50',104,104,392,'2025-01-01'),(106,'2024-03-10 06:39:44',102,106,144,'2025-03-05'),(107,'2024-03-10 06:40:24',103,107,245,'2025-03-04'),(108,'2024-03-10 06:41:15',104,108,174,'2026-01-01');
/*!40000 ALTER TABLE `batch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `billing`
--

DROP TABLE IF EXISTS `billing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `billing` (
  `Bill_id` int NOT NULL,
  `Presc_id` int DEFAULT NULL,
  `Total_cost` float DEFAULT NULL,
  `Bill_timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Bill_id`),
  KEY `Presc_id` (`Presc_id`),
  CONSTRAINT `billing_ibfk_1` FOREIGN KEY (`Presc_id`) REFERENCES `prescription` (`Presc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `billing`
--

LOCK TABLES `billing` WRITE;
/*!40000 ALTER TABLE `billing` DISABLE KEYS */;
INSERT INTO `billing` VALUES (1,1,330,'2024-03-10 19:39:59'),(2,2,470,'2024-03-10 19:43:10'),(3,3,560,'2024-03-10 19:45:15'),(4,3,560,'2024-03-10 19:45:23'),(5,4,120,'2024-03-11 06:45:30'),(6,1,330,'2024-03-11 07:04:33');
/*!40000 ALTER TABLE `billing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor` (
  `Doc_id` int NOT NULL,
  `Doc_name` varchar(50) NOT NULL,
  `Doc_mobile` varchar(10) DEFAULT NULL,
  `Doc_work_address` varchar(75) DEFAULT NULL,
  `Speciality` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Doc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES (101,'Dr. Olivia Smith','5551234567','123 Main Street, Cityville, State, Zip Code','Cardiology'),(102,'Dr. James Johnson','5559876543','456 Elm Street, Townsville, State, Zip Code','Pediatrics'),(103,'Dr. Emily Brown','5558765432','789 Oak Avenue, Villagetown, State, Zip Code','Dermatology'),(104,'Dr. Michael Lee','5552345678','101 Pine Road, Hamletville, State, Zip Code','Orthopedics'),(105,'Dr. Sophia Garcia','5557654321','202 Maple Lane, Boroughburg, State, Zip Code','Psychiatry'),(106,'Dr. Benjamin Martinez','5553456789','303 Cedar Court, Villageburg, State, Zip Code','Neurology'),(107,'Dr. Ava Taylor','5555432109','404 Birch Avenue, Citytown, State, Zip Code','Obstetrics and Gynecology'),(108,'Dr. Jacob White','5556789012','505 Walnut Street, Townville, State, Zip Code','Ophthalmology');
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicine`
--

DROP TABLE IF EXISTS `medicine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medicine` (
  `Med_id` int NOT NULL,
  `Med_name` varchar(50) NOT NULL,
  `Med_company` varchar(50) DEFAULT NULL,
  `Med_cost_unit` int NOT NULL,
  `Med_type` varchar(30) DEFAULT NULL,
  `Is_OTC` char(1) NOT NULL,
  PRIMARY KEY (`Med_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicine`
--

LOCK TABLES `medicine` WRITE;
/*!40000 ALTER TABLE `medicine` DISABLE KEYS */;
INSERT INTO `medicine` VALUES (101,'Ibuprofen','Generic Pharma',40,'Pain Reliever','Y'),(102,'Loratadine','Allergy Relief Inc.',40,'Antihistamine','Y'),(103,'Acetaminophen','PharmaCo',20,'Pain Reliever','Y'),(104,'Ranitidine','Digestive Health Labs',30,'Antacid','Y'),(105,'Omeprazole','GastroMed Solutions',190,'Proton Pump Inhibitor','N'),(106,'Simvastatin','CardioPharma',80,'Statin','N'),(107,'Metformin','DiabetesCare Inc.',50,'Antidiabetic','N'),(108,'Warfarin','Anticoagulant Labs',80,'Anticoagulant','N');
/*!40000 ALTER TABLE `medicine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifs`
--

DROP TABLE IF EXISTS `notifs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notifs` (
  `Notif_id` int NOT NULL,
  `Priority` int DEFAULT NULL,
  `Notif` mediumtext,
  PRIMARY KEY (`Notif_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifs`
--

LOCK TABLES `notifs` WRITE;
/*!40000 ALTER TABLE `notifs` DISABLE KEYS */;
INSERT INTO `notifs` VALUES (1,1,'Order essential medicines'),(2,1,'Remove expired medicines'),(3,2,'Add new list of doctors'),(4,3,'Add new list of patients'),(5,0,'Demo task'),(6,0,'Cutu is a bitch');
/*!40000 ALTER TABLE `notifs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `Patient_id` int NOT NULL,
  `Patient_name` varchar(50) NOT NULL,
  `patient_mobile` varchar(10) DEFAULT NULL,
  `Patient_address` varchar(75) DEFAULT NULL,
  `Sex` char(2) DEFAULT NULL,
  PRIMARY KEY (`Patient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES (101,'Emily Johnson','5551112222','123 Pine Street, Cityville, State, Zip Code','F'),(102,'Michael Brown','5553334444','456 Oak Avenue, Townsville, State, Zip Code','M'),(103,'Sophia Davis','5555556666','789 Elm Court, Villagetown, State, Zip Code','F'),(104,'James Wilson','5557778888','101 Maple Lane, Hamletville, State, Zip Code','M'),(105,'Ava Martinez','5559990000','202 Cedar Street, Boroughburg, State, Zip Code','F'),(106,'Benjamin Taylor','5551212121','303 Birch Avenue, Villageburg, State, Zip Code','M');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `presc_details`
--

DROP TABLE IF EXISTS `presc_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `presc_details` (
  `Presc_id` int NOT NULL,
  `Med_id` int NOT NULL,
  `Med_qty` int DEFAULT NULL,
  `Cost` int DEFAULT NULL,
  PRIMARY KEY (`Presc_id`,`Med_id`),
  KEY `Med_id` (`Med_id`),
  CONSTRAINT `presc_details_ibfk_1` FOREIGN KEY (`Presc_id`) REFERENCES `prescription` (`Presc_id`),
  CONSTRAINT `presc_details_ibfk_2` FOREIGN KEY (`Med_id`) REFERENCES `medicine` (`Med_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `presc_details`
--

LOCK TABLES `presc_details` WRITE;
/*!40000 ALTER TABLE `presc_details` DISABLE KEYS */;
INSERT INTO `presc_details` VALUES (1,102,3,120),(1,106,2,160),(1,107,1,50),(2,103,2,40),(2,107,3,150),(2,108,1,80),(3,101,3,120),(3,106,1,80),(3,108,2,160),(4,103,2,40),(4,108,1,80);
/*!40000 ALTER TABLE `presc_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prescription`
--

DROP TABLE IF EXISTS `prescription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prescription` (
  `Presc_id` int NOT NULL,
  `Patient_id` int NOT NULL,
  `Doc_id` int NOT NULL,
  `paid` char(1) DEFAULT NULL,
  PRIMARY KEY (`Presc_id`),
  KEY `Patient_id` (`Patient_id`),
  KEY `Doc_id` (`Doc_id`),
  CONSTRAINT `prescription_ibfk_1` FOREIGN KEY (`Patient_id`) REFERENCES `patient` (`Patient_id`),
  CONSTRAINT `prescription_ibfk_2` FOREIGN KEY (`Doc_id`) REFERENCES `doctor` (`Doc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prescription`
--

LOCK TABLES `prescription` WRITE;
/*!40000 ALTER TABLE `prescription` DISABLE KEYS */;
INSERT INTO `prescription` VALUES (1,102,102,'Y'),(2,103,103,'N'),(3,104,104,'N'),(4,105,105,'Y');
/*!40000 ALTER TABLE `prescription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `Supplier_id` int NOT NULL,
  `Supplier_name` varchar(50) NOT NULL,
  `Supplier_location` varchar(75) DEFAULT NULL,
  PRIMARY KEY (`Supplier_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (101,'MedTech Supplies','123 Medical Drive, Cityville, State, Zip Code'),(102,'PharmaHealth Solutions','456 Healthcare Avenue, Townsville, State, Zip Code'),(103,'MediCare Distributors','789 Hospital Street, Villagetown, State, Zip Code'),(104,'MedEquip Pro','101 Wellness Lane, Hamletville, State, Zip Code');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-11 23:22:07
