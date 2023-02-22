CREATE DATABASE  IF NOT EXISTS `online_b2b_marketplace_1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `online_b2b_marketplace_1`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: online_b2b_marketplace_1
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `business_types`
--

DROP TABLE IF EXISTS `business_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `business_types` (
  `id` varchar(90) NOT NULL,
  `name` varchar(90) DEFAULT NULL,
  `description` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `business_types`
--

LOCK TABLES `business_types` WRITE;
/*!40000 ALTER TABLE `business_types` DISABLE KEYS */;
INSERT INTO `business_types` VALUES ('d5018885-d585-4cdd-9ab1-7d39def483a0','wholesaler business','some description...');
/*!40000 ALTER TABLE `business_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_product`
--

DROP TABLE IF EXISTS `order_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_product` (
  `id` varchar(90) NOT NULL,
  `order_id` varchar(90) DEFAULT NULL,
  `wholesaler_product_id` varchar(90) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `quantity` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `order_id` (`order_id`),
  KEY `wholesaler_product_id` (`wholesaler_product_id`),
  CONSTRAINT `order_product_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),
  CONSTRAINT `order_product_ibfk_2` FOREIGN KEY (`wholesaler_product_id`) REFERENCES `wholesaler_has_products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_product`
--

LOCK TABLES `order_product` WRITE;
/*!40000 ALTER TABLE `order_product` DISABLE KEYS */;
INSERT INTO `order_product` VALUES ('079c88fe-74b1-4e55-a9ce-27b9f987b39d','d19287e1-2e80-482f-b6f7-edb8ddcd28c0','82b6f6ba-6a4d-4054-b7b8-c364f8ba844e',10000,2),('4f952296-fe7b-4fdb-aa25-8827730e572d','d19287e1-2e80-482f-b6f7-edb8ddcd28c0','82b6f6ba-6a4d-4054-b7b8-c364f8ba844e',10000,1),('55ed446b-8486-4a43-8f26-5eee3632adc0','d19287e1-2e80-482f-b6f7-edb8ddcd28c0','82b6f6ba-6a4d-4054-b7b8-c364f8ba844e',20000,4),('581922bb-a46a-4bca-b580-a056290f448b','d19287e1-2e80-482f-b6f7-edb8ddcd28c0','82b6f6ba-6a4d-4054-b7b8-c364f8ba844e',20000,3),('64f355ab-42ef-46ea-8f6a-ef6404c9844f','540d7c00-a762-4522-878d-f88a98be2c39','82b6f6ba-6a4d-4054-b7b8-c364f8ba844e',20000,10),('654eaf65-42d0-41f1-9e78-d234fb19c353','d19287e1-2e80-482f-b6f7-edb8ddcd28c0','82b6f6ba-6a4d-4054-b7b8-c364f8ba844e',10000,4),('b6bd7020-3d5c-4a9d-943e-dd463fa18404','d19287e1-2e80-482f-b6f7-edb8ddcd28c0','82b6f6ba-6a4d-4054-b7b8-c364f8ba844e',20000,3);
/*!40000 ALTER TABLE `order_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_status`
--

DROP TABLE IF EXISTS `order_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_status` (
  `id` varchar(90) NOT NULL,
  `status_code` varchar(90) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `date_and_time` varchar(90) DEFAULT NULL,
  `order_id` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `order_id` (`order_id`),
  CONSTRAINT `order_status_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_status`
--

LOCK TABLES `order_status` WRITE;
/*!40000 ALTER TABLE `order_status` DISABLE KEYS */;
INSERT INTO `order_status` VALUES ('f9340c38-df24-45ce-86f4-c57eb30a004c','Accepted','Order accepted by the wholesaler.','22-02-2023, 16:57:56','d19287e1-2e80-482f-b6f7-edb8ddcd28c0');
/*!40000 ALTER TABLE `order_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` varchar(90) NOT NULL,
  `type` varchar(90) DEFAULT NULL,
  `order_date` date DEFAULT NULL,
  `wholesaler_id` varchar(90) DEFAULT NULL,
  `retailer_id` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wholesaler_id` (`wholesaler_id`),
  KEY `retailer_id` (`retailer_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`wholesaler_id`) REFERENCES `wholesalers` (`id`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`retailer_id`) REFERENCES `retailers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES ('540d7c00-a762-4522-878d-f88a98be2c39','express','2023-02-25','beec3c22-0cbe-44a9-801d-c6bb84aa66dd','3fb6134a-ea63-48ee-9a2d-b4e66777e66e'),('d19287e1-2e80-482f-b6f7-edb8ddcd28c0','express','2023-05-02','beec3c22-0cbe-44a9-801d-c6bb84aa66dd','3fb6134a-ea63-48ee-9a2d-b4e66777e66e');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment_status`
--

DROP TABLE IF EXISTS `payment_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment_status` (
  `id` varchar(90) NOT NULL,
  `status_code` varchar(90) DEFAULT NULL,
  `status_description` varchar(200) DEFAULT NULL,
  `date_and_time` varchar(90) DEFAULT NULL,
  `payment_id` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `payment_id` (`payment_id`),
  CONSTRAINT `payment_status_ibfk_1` FOREIGN KEY (`payment_id`) REFERENCES `payments` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_status`
--

LOCK TABLES `payment_status` WRITE;
/*!40000 ALTER TABLE `payment_status` DISABLE KEYS */;
INSERT INTO `payment_status` VALUES ('3be388cb-d77c-430b-8afd-3cf08adc5852','CANCELLED','Payment refunded due to order cancellation.','22-02-2023, 15:12:19','71e1eee5-9277-4b89-8319-e4058c402f95'),('ef3c928a-5b3f-493b-930f-c5eb4f58c11e','COMPLETE','Payment succesfully completed.','22-02-2023, 03:18:31','71e1eee5-9277-4b89-8319-e4058c402f95');
/*!40000 ALTER TABLE `payment_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `id` varchar(90) NOT NULL,
  `payment_amount` float DEFAULT NULL,
  `order_id` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_id` (`order_id`),
  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES ('71e1eee5-9277-4b89-8319-e4058c402f95',270000,'d19287e1-2e80-482f-b6f7-edb8ddcd28c0'),('e0103494-5f27-48bd-a489-f73bda822cd4',200000,'540d7c00-a762-4522-878d-f88a98be2c39');
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_categories`
--

DROP TABLE IF EXISTS `product_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_categories` (
  `id` varchar(90) NOT NULL,
  `name` varchar(90) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_categories`
--

LOCK TABLES `product_categories` WRITE;
/*!40000 ALTER TABLE `product_categories` DISABLE KEYS */;
INSERT INTO `product_categories` VALUES ('fba24bd9-027a-4d25-98c1-c835498e3118','Cars','Car category description');
/*!40000 ALTER TABLE `product_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` varchar(90) NOT NULL,
  `name` varchar(90) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `product_category_id` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `product_category_id` (`product_category_id`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`product_category_id`) REFERENCES `product_categories` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('7d3ceb05-c675-4176-9747-f8cd5b411b3a','BMW 320d','BMw 320d, 2013, Fast and reliable','fba24bd9-027a-4d25-98c1-c835498e3118');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retailers`
--

DROP TABLE IF EXISTS `retailers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `retailers` (
  `id` varchar(90) NOT NULL,
  `name` varchar(90) DEFAULT NULL,
  `hq_location` varchar(90) DEFAULT NULL,
  `landline` varchar(90) DEFAULT NULL,
  `business_email` varchar(90) DEFAULT NULL,
  `business_type_id` varchar(90) DEFAULT NULL,
  `user_id` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `business_type_id` (`business_type_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `retailers_ibfk_1` FOREIGN KEY (`business_type_id`) REFERENCES `business_types` (`id`),
  CONSTRAINT `retailers_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retailers`
--

LOCK TABLES `retailers` WRITE;
/*!40000 ALTER TABLE `retailers` DISABLE KEYS */;
INSERT INTO `retailers` VALUES ('3fb6134a-ea63-48ee-9a2d-b4e66777e66e','AMAZON','New York, USA','78787878','amzn@gmail.com','256bd277-d6ff-4d67-8c0f-5a2c02aeac3b','91a491e7-63ea-4141-a2a1-43637373c851');
/*!40000 ALTER TABLE `retailers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(90) NOT NULL,
  `username` varchar(90) DEFAULT NULL,
  `email` varchar(90) DEFAULT NULL,
  `password` varchar(90) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `is_superuser` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('313ae57a-b057-4578-a821-18b1849e6827','super','super@gmail.com','73d1b1b1bc1dabfb97f216d897b7968e44b06457920f00f2dc6c1ed3be25ad4c',1,1),('8bcc44cc-e8ce-4e16-be26-d8d96d6b1f19','string','user@example.com','473287f8298dba7163a897908958f7c0eae733e25d2e027992ea2edc9bed2fa8',1,0),('91a491e7-63ea-4141-a2a1-43637373c851','string123','user1@example.com','93fedde43203e0a76172135221b8636313635d7afff96a490ae9066330505d47',1,0),('d30c9182-88b3-4256-8a3a-a7305e710c3b','superuser','superuser@gmail.com','382132701c4733c3402706cfdd3c8fc7f41f80a88dce5428d145259a41c5f12f',1,1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wholesaler_has_products`
--

DROP TABLE IF EXISTS `wholesaler_has_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wholesaler_has_products` (
  `id` varchar(90) NOT NULL,
  `wholesaler_id` varchar(90) DEFAULT NULL,
  `product_id` varchar(90) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `quantity_available` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wholesaler_id` (`wholesaler_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `wholesaler_has_products_ibfk_1` FOREIGN KEY (`wholesaler_id`) REFERENCES `wholesalers` (`id`),
  CONSTRAINT `wholesaler_has_products_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wholesaler_has_products`
--

LOCK TABLES `wholesaler_has_products` WRITE;
/*!40000 ALTER TABLE `wholesaler_has_products` DISABLE KEYS */;
INSERT INTO `wholesaler_has_products` VALUES ('82b6f6ba-6a4d-4054-b7b8-c364f8ba844e','beec3c22-0cbe-44a9-801d-c6bb84aa66dd','7d3ceb05-c675-4176-9747-f8cd5b411b3a',8000,15),('c857aadb-defe-492a-896c-9a2b1b8890c5','beec3c22-0cbe-44a9-801d-c6bb84aa66dd','7d3ceb05-c675-4176-9747-f8cd5b411b3a',20000,20);
/*!40000 ALTER TABLE `wholesaler_has_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wholesalers`
--

DROP TABLE IF EXISTS `wholesalers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wholesalers` (
  `id` varchar(90) NOT NULL,
  `name` varchar(90) DEFAULT NULL,
  `hq_location` varchar(90) DEFAULT NULL,
  `landline` varchar(90) DEFAULT NULL,
  `business_email` varchar(90) DEFAULT NULL,
  `business_type_id` varchar(90) DEFAULT NULL,
  `user_id` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `business_type_id` (`business_type_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `wholesalers_ibfk_1` FOREIGN KEY (`business_type_id`) REFERENCES `business_types` (`id`),
  CONSTRAINT `wholesalers_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wholesalers`
--

LOCK TABLES `wholesalers` WRITE;
/*!40000 ALTER TABLE `wholesalers` DISABLE KEYS */;
INSERT INTO `wholesalers` VALUES ('beec3c22-0cbe-44a9-801d-c6bb84aa66dd','Coca Cola','Somewhere in the US','111-222','cocacolacompany@gmail.com','1f3d42db-a13c-48fb-906a-d031b3b0b109','8bcc44cc-e8ce-4e16-be26-d8d96d6b1f19');
/*!40000 ALTER TABLE `wholesalers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-22 18:07:37
