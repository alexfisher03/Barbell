-- MySQL dump 10.13  Distrib 8.1.0, for Win64 (x86_64)
--
-- Host: localhost    Database: accounts_db
-- ------------------------------------------------------
-- Server version	8.1.0

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
-- Table structure for table `account_emailaddress`
--

DROP TABLE IF EXISTS `account_emailaddress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account_emailaddress` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_emailaddress_user_id_email_987c8728_uniq` (`user_id`,`email`),
  KEY `account_emailaddress_upper` ((upper(`email`))),
  CONSTRAINT `account_emailaddress_user_id_2c513194_fk_gym_app_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `gym_app_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_emailaddress`
--

LOCK TABLES `account_emailaddress` WRITE;
/*!40000 ALTER TABLE `account_emailaddress` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_emailaddress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_emailconfirmation`
--

DROP TABLE IF EXISTS `account_emailconfirmation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account_emailconfirmation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `sent` datetime(6) DEFAULT NULL,
  `key` varchar(64) NOT NULL,
  `email_address_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`),
  KEY `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id`),
  CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_emailconfirmation`
--

LOCK TABLES `account_emailconfirmation` WRITE;
/*!40000 ALTER TABLE `account_emailconfirmation` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_emailconfirmation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add App user',1,'add_customuser'),(2,'Can change App user',1,'change_customuser'),(3,'Can delete App user',1,'delete_customuser'),(4,'Can view App user',1,'view_customuser'),(5,'Can add Stat Data',2,'add_tabledata'),(6,'Can change Stat Data',2,'change_tabledata'),(7,'Can delete Stat Data',2,'delete_tabledata'),(8,'Can view Stat Data',2,'view_tabledata'),(9,'Can add image metadata',3,'add_imagemetadata'),(10,'Can change image metadata',3,'change_imagemetadata'),(11,'Can delete image metadata',3,'delete_imagemetadata'),(12,'Can view image metadata',3,'view_imagemetadata'),(13,'Can add group',4,'add_group'),(14,'Can change group',4,'change_group'),(15,'Can delete group',4,'delete_group'),(16,'Can view group',4,'view_group'),(17,'Can add stat data',5,'add_statdata'),(18,'Can change stat data',5,'change_statdata'),(19,'Can delete stat data',5,'delete_statdata'),(20,'Can view stat data',5,'view_statdata'),(21,'Can add email address',6,'add_emailaddress'),(22,'Can change email address',6,'change_emailaddress'),(23,'Can delete email address',6,'delete_emailaddress'),(24,'Can view email address',6,'view_emailaddress'),(25,'Can add email confirmation',7,'add_emailconfirmation'),(26,'Can change email confirmation',7,'change_emailconfirmation'),(27,'Can delete email confirmation',7,'delete_emailconfirmation'),(28,'Can view email confirmation',7,'view_emailconfirmation'),(29,'Can add log entry',8,'add_logentry'),(30,'Can change log entry',8,'change_logentry'),(31,'Can delete log entry',8,'delete_logentry'),(32,'Can view log entry',8,'view_logentry'),(33,'Can add permission',9,'add_permission'),(34,'Can change permission',9,'change_permission'),(35,'Can delete permission',9,'delete_permission'),(36,'Can view permission',9,'view_permission'),(37,'Can add group',10,'add_group'),(38,'Can change group',10,'change_group'),(39,'Can delete group',10,'delete_group'),(40,'Can view group',10,'view_group'),(41,'Can add content type',11,'add_contenttype'),(42,'Can change content type',11,'change_contenttype'),(43,'Can delete content type',11,'delete_contenttype'),(44,'Can view content type',11,'view_contenttype'),(45,'Can add session',12,'add_session'),(46,'Can change session',12,'change_session'),(47,'Can delete session',12,'delete_session'),(48,'Can view session',12,'view_session'),(49,'Can add workout',13,'add_workout'),(50,'Can change workout',13,'change_workout'),(51,'Can delete workout',13,'delete_workout'),(52,'Can view workout',13,'view_workout'),(53,'Can add exercise',13,'add_exercise'),(54,'Can change exercise',13,'change_exercise'),(55,'Can delete exercise',13,'delete_exercise'),(56,'Can view exercise',13,'view_exercise'),(57,'Can add workout',14,'add_workout'),(58,'Can change workout',14,'change_workout'),(59,'Can delete workout',14,'delete_workout'),(60,'Can view workout',14,'view_workout');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_gym_app_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_gym_app_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `gym_app_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (6,'account','emailaddress'),(7,'account','emailconfirmation'),(8,'admin','logentry'),(10,'auth','group'),(9,'auth','permission'),(11,'contenttypes','contenttype'),(1,'gym_app','customuser'),(13,'gym_app','exercise'),(4,'gym_app','group'),(3,'gym_app','imagemetadata'),(5,'gym_app','statdata'),(2,'gym_app','tabledata'),(14,'gym_app','workout'),(12,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-07-06 03:21:00.487921'),(2,'contenttypes','0002_remove_content_type_name','2024-07-06 03:21:00.537346'),(3,'auth','0001_initial','2024-07-06 03:21:00.801833'),(4,'auth','0002_alter_permission_name_max_length','2024-07-06 03:21:00.852155'),(5,'auth','0003_alter_user_email_max_length','2024-07-06 03:21:00.858088'),(6,'auth','0004_alter_user_username_opts','2024-07-06 03:21:00.865073'),(7,'auth','0005_alter_user_last_login_null','2024-07-06 03:21:00.871082'),(8,'auth','0006_require_contenttypes_0002','2024-07-06 03:21:00.874047'),(9,'auth','0007_alter_validators_add_error_messages','2024-07-06 03:21:00.881307'),(10,'auth','0008_alter_user_username_max_length','2024-07-06 03:21:00.887683'),(11,'auth','0009_alter_user_last_name_max_length','2024-07-06 03:21:00.893990'),(12,'auth','0010_alter_group_name_max_length','2024-07-06 03:21:00.907969'),(13,'auth','0011_update_proxy_permissions','2024-07-06 03:21:00.914936'),(14,'auth','0012_alter_user_first_name_max_length','2024-07-06 03:21:00.920928'),(24,'gym_app','0002_customuser_bio_customuser_dob_tabledata_date_and_more','2024-07-06 03:21:01.759576'),(25,'gym_app','0003_alter_tabledata_date','2024-07-06 03:21:01.824304'),(26,'gym_app','0004_alter_tabledata_date','2024-07-06 03:21:01.868751'),(27,'gym_app','0005_alter_tabledata_date','2024-07-06 03:21:01.916501'),(28,'gym_app','0006_alter_customuser_options_alter_tabledata_options_and_more','2024-07-06 03:21:01.979103'),(29,'gym_app','0007_group','2024-07-06 03:21:02.043933'),(30,'gym_app','0008_remove_group_bio_group_groupbio','2024-07-06 03:21:02.078778'),(31,'gym_app','0009_alter_group_groupbio','2024-07-06 03:21:02.130638'),(32,'gym_app','0010_customuser_current_group_alter_customuser_groups','2024-07-06 03:21:02.235426'),(33,'gym_app','0011_alter_customuser_current_group','2024-07-06 03:21:02.363250'),(34,'gym_app','0007_statdata','2024-07-06 03:21:02.420937'),(35,'gym_app','0012_merge_20230912_2319','2024-07-06 03:21:02.423929'),(36,'gym_app','0013_customuser_points','2024-07-06 03:21:02.476647'),(37,'gym_app','0014_alter_customuser_profile_picture','2024-07-06 03:21:02.486620'),(38,'sessions','0001_initial','2024-07-06 03:21:02.527120'),(39,'gym_app','0015_delete_imagemetadata','2024-07-07 22:27:38.224049'),(40,'gym_app','0016_imagemetadata','2024-07-08 00:01:46.130710'),(41,'gym_app','0017_workout_remove_tabledata_user_delete_statdata_and_more','2024-07-31 05:03:32.782638'),(42,'gym_app','0018_rename_workout_exercise','2024-08-04 03:51:56.932686');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('6ghergczucw4z5g9cfxz9qck4cqkelyp','.eJxVjEEOwiAQRe_C2hCYgRRduvcMZBgGqRqalHbVeHdt0oVu_3vvbyrSutS4dpnjmNVFWXX63RLxU9oO8oPafdI8tWUek94VfdCub1OW1_Vw_w4q9fqt2bG3FBwRDMBIZCEFI1xA_GCIRBAhOCAoaKyX4s4lZF-Q0RuHRb0_8gk4EQ:1sbYV6:d6EuY2_LLK7WwH8ZgA-1_jXHgUkjWNU2OgBtc5M-r9E','2024-08-21 04:42:16.947911'),('9vfvvdh2iianvaa1ntbog9pudnalpdyo','.eJxVjEEOwiAQRe_C2hCYgRRduvcMZBgGqRqalHbVeHdt0oVu_3vvbyrSutS4dpnjmNVFWXX63RLxU9oO8oPafdI8tWUek94VfdCub1OW1_Vw_w4q9fqt2bG3FBwRDMBIZCEFI1xA_GCIRBAhOCAoaKyX4s4lZF-Q0RuHRb0_8gk4EQ:1sRJj9:jT2MSU-0Lxxrexb28BZWh_nGfxbcP8hcOqYHcV_L2l0','2024-07-23 22:54:27.297941'),('f50wjlzhzd54ror0ivd4cti6by6lwaw7','.eJxVjEEOwiAQRe_C2hCYgRRduvcMZBgGqRqalHbVeHdt0oVu_3vvbyrSutS4dpnjmNVFWXX63RLxU9oO8oPafdI8tWUek94VfdCub1OW1_Vw_w4q9fqt2bG3FBwRDMBIZCEFI1xA_GCIRBAhOCAoaKyX4s4lZF-Q0RuHRb0_8gk4EQ:1sQdfG:QZB3B0W4zYkI5zT6RQCQ3INcnKZpOkAfUXNvO_BuBVI','2024-07-22 01:59:38.577067'),('y0vlrv31sbaqk3bl7lw72dwsyop55q2q','.eJxVjEEOwiAQRe_C2hCYgRRduvcMZBgGqRqalHbVeHdt0oVu_3vvbyrSutS4dpnjmNVFWXX63RLxU9oO8oPafdI8tWUek94VfdCub1OW1_Vw_w4q9fqt2bG3FBwRDMBIZCEFI1xA_GCIRBAhOCAoaKyX4s4lZF-Q0RuHRb0_8gk4EQ:1sa889:d70lDfFkwGFWC-L5Fcz-ZEGLRQNM1LguXTSF-RRpoRU','2024-08-17 06:20:41.033439');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gym_app_customuser`
--

DROP TABLE IF EXISTS `gym_app_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gym_app_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `profile_picture` varchar(100) DEFAULT NULL,
  `bio` longtext NOT NULL DEFAULT (_utf8mb3''),
  `dob` date DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `current_group_id` bigint DEFAULT NULL,
  `points` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `gym_app_customuser_current_group_id_d9b1da1f_fk_gym_app_group_id` (`current_group_id`),
  CONSTRAINT `gym_app_customuser_current_group_id_d9b1da1f_fk_gym_app_group_id` FOREIGN KEY (`current_group_id`) REFERENCES `gym_app_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gym_app_customuser`
--

LOCK TABLES `gym_app_customuser` WRITE;
/*!40000 ALTER TABLE `gym_app_customuser` DISABLE KEYS */;
INSERT INTO `gym_app_customuser` VALUES (1,'pbkdf2_sha256$600000$IyYaxPI5Nk0g2THEEUVbTL$CTSnV8aczG3QneqcpgTjGpKYlq5a1/oIQA+NoDyX5NU=','2024-08-07 04:42:16.942924',1,'pcadmin','','','local@local.com',1,1,'2024-07-06 03:22:13.013309','userProfilePictures/user_pcadmin/2024/7/98A81340-EC2C-4A46-BD9A-A562D8D0E9FC.jpg','BarbellAdmin Bio',NULL,NULL,NULL,1,0);
/*!40000 ALTER TABLE `gym_app_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gym_app_customuser_groups`
--

DROP TABLE IF EXISTS `gym_app_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gym_app_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `gym_app_customuser_groups_customuser_id_group_id_38fe1471_uniq` (`customuser_id`,`group_id`),
  KEY `gym_app_customuser_groups_group_id_e839fd5a_fk_auth_group_id` (`group_id`),
  CONSTRAINT `gym_app_customuser_g_customuser_id_33738ae0_fk_gym_app_c` FOREIGN KEY (`customuser_id`) REFERENCES `gym_app_customuser` (`id`),
  CONSTRAINT `gym_app_customuser_groups_group_id_e839fd5a_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gym_app_customuser_groups`
--

LOCK TABLES `gym_app_customuser_groups` WRITE;
/*!40000 ALTER TABLE `gym_app_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `gym_app_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gym_app_customuser_user_permissions`
--

DROP TABLE IF EXISTS `gym_app_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gym_app_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `gym_app_customuser_user__customuser_id_permission_54619dda_uniq` (`customuser_id`,`permission_id`),
  KEY `gym_app_customuser_u_permission_id_a417fd8d_fk_auth_perm` (`permission_id`),
  CONSTRAINT `gym_app_customuser_u_customuser_id_f104f3f5_fk_gym_app_c` FOREIGN KEY (`customuser_id`) REFERENCES `gym_app_customuser` (`id`),
  CONSTRAINT `gym_app_customuser_u_permission_id_a417fd8d_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gym_app_customuser_user_permissions`
--

LOCK TABLES `gym_app_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `gym_app_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `gym_app_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gym_app_group`
--

DROP TABLE IF EXISTS `gym_app_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gym_app_group` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `privacy` varchar(3) NOT NULL,
  `created_by_id` bigint NOT NULL,
  `groupbio` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gym_app_group_created_by_id_964b192e_fk_gym_app_customuser_id` (`created_by_id`),
  CONSTRAINT `gym_app_group_created_by_id_964b192e_fk_gym_app_customuser_id` FOREIGN KEY (`created_by_id`) REFERENCES `gym_app_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gym_app_group`
--

LOCK TABLES `gym_app_group` WRITE;
/*!40000 ALTER TABLE `gym_app_group` DISABLE KEYS */;
INSERT INTO `gym_app_group` VALUES (1,'The Republic','PRV',1,'Group Bio');
/*!40000 ALTER TABLE `gym_app_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gym_app_imagemetadata`
--

DROP TABLE IF EXISTS `gym_app_imagemetadata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gym_app_imagemetadata` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `caption` varchar(200) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gym_app_imagemetadata_user_id_cb8eca4c_fk_gym_app_customuser_id` (`user_id`),
  CONSTRAINT `gym_app_imagemetadata_user_id_cb8eca4c_fk_gym_app_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `gym_app_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gym_app_imagemetadata`
--

LOCK TABLES `gym_app_imagemetadata` WRITE;
/*!40000 ALTER TABLE `gym_app_imagemetadata` DISABLE KEYS */;
/*!40000 ALTER TABLE `gym_app_imagemetadata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gym_app_statdata`
--

DROP TABLE IF EXISTS `gym_app_statdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gym_app_statdata` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `exercise_name` varchar(20) NOT NULL,
  `num_sets` int NOT NULL,
  `num_reps` int NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gym_app_statdata`
--

LOCK TABLES `gym_app_statdata` WRITE;
/*!40000 ALTER TABLE `gym_app_statdata` DISABLE KEYS */;
/*!40000 ALTER TABLE `gym_app_statdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gym_app_tabledata`
--

DROP TABLE IF EXISTS `gym_app_tabledata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gym_app_tabledata` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `data_title` varchar(100) NOT NULL,
  `data_value` decimal(10,2) NOT NULL,
  `date` date NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gym_app_tabledata_user_id_aa4296ff_fk_gym_app_customuser_id` (`user_id`),
  CONSTRAINT `gym_app_tabledata_user_id_aa4296ff_fk_gym_app_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `gym_app_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gym_app_tabledata`
--

LOCK TABLES `gym_app_tabledata` WRITE;
/*!40000 ALTER TABLE `gym_app_tabledata` DISABLE KEYS */;
/*!40000 ALTER TABLE `gym_app_tabledata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gym_app_workout`
--

DROP TABLE IF EXISTS `gym_app_workout`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gym_app_workout` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `day` varchar(3) DEFAULT NULL,
  `order` int NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gym_app_workout_user_id_26f4a0ee_fk_gym_app_customuser_id` (`user_id`),
  CONSTRAINT `gym_app_workout_user_id_26f4a0ee_fk_gym_app_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `gym_app_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=162 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gym_app_workout`
--

LOCK TABLES `gym_app_workout` WRITE;
/*!40000 ALTER TABLE `gym_app_workout` DISABLE KEYS */;
INSERT INTO `gym_app_workout` VALUES (160,'Test Workout 1',NULL,0,1),(161,'Test Workout 2',NULL,0,1);
/*!40000 ALTER TABLE `gym_app_workout` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-07  1:42:08
