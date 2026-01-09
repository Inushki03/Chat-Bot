-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: chatbot
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `food_items`
--

DROP TABLE IF EXISTS `food_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `food_items` (
  `Food_ID` int NOT NULL,
  `Food_Name` varchar(30) DEFAULT NULL,
  `Pizza_Size` varchar(10) DEFAULT NULL,
  `Price_per_serving` double DEFAULT NULL,
  PRIMARY KEY (`Food_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food_items`
--

LOCK TABLES `food_items` WRITE;
/*!40000 ALTER TABLE `food_items` DISABLE KEYS */;
INSERT INTO `food_items` VALUES (100,'Cheesy Pizza','Large',2000),(101,'Cheesy Pizza','Medium',1500),(102,'Cheesy Pizza','Small',850),(103,'Mushroom Pizza','Large',2500),(104,'Mushroom Pizza','Medium',1800),(105,'Mushroom Pizza','Small',950),(106,'Tandoori Chicken Pizza','Large',3000),(107,'Tandoori Chicken Pizza','Medium',2500),(108,'Tandoori Chicken Pizza','Small',1500),(109,'Paneer Pizza','Large',2500),(110,'Paneer Pizza','Medium',1800),(111,'Paneer Pizza','Small',950),(112,'Veg Pizza','Large',2000),(113,'Veg Pizza','Medium',1500),(114,'Veg Pizza','Small',850),(115,'Lava Cake','null',600),(116,'Cocacola','null',550),(117,'Pepsi','null',550);
/*!40000 ALTER TABLE `food_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food_order`
--

DROP TABLE IF EXISTS `food_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `food_order` (
  `Oredr_ID` int NOT NULL,
  `Food_ID` int NOT NULL,
  `quantity` int DEFAULT NULL,
  `Total_Amount` double DEFAULT NULL,
  PRIMARY KEY (`Oredr_ID`,`Food_ID`),
  KEY `Food_ID` (`Food_ID`),
  CONSTRAINT `food_order_ibfk_1` FOREIGN KEY (`Food_ID`) REFERENCES `food_items` (`Food_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food_order`
--

LOCK TABLES `food_order` WRITE;
/*!40000 ALTER TABLE `food_order` DISABLE KEYS */;
INSERT INTO `food_order` VALUES (1000,106,2,6000),(1000,115,1,600),(1001,114,3,2550),(1002,104,1,1800),(1002,117,1,550),(1003,100,4,8000),(1003,116,4,2200);
/*!40000 ALTER TABLE `food_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_tracking`
--

DROP TABLE IF EXISTS `order_tracking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_tracking` (
  `Order_ID` int NOT NULL,
  `Status_of_Order` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Order_ID`),
  CONSTRAINT `order_tracking_ibfk_1` FOREIGN KEY (`Order_ID`) REFERENCES `food_order` (`Oredr_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_tracking`
--

LOCK TABLES `order_tracking` WRITE;
/*!40000 ALTER TABLE `order_tracking` DISABLE KEYS */;
INSERT INTO `order_tracking` VALUES (1000,'Delivared'),(1001,'Preparing'),(1002,'In transit'),(1003,'in Progress');
/*!40000 ALTER TABLE `order_tracking` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-09 18:02:57
