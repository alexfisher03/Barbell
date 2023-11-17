-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: accounts_db
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.22.04.1

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
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_emailaddress_user_id_email_987c8728_uniq` (`user_id`,`email`),
  KEY `account_emailaddress_upper` ((upper(`email`))),
  CONSTRAINT `account_emailaddress_user_id_2c513194_fk_gym_app_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `gym_app_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
  `key` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email_address_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`),
  KEY `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id`),
  CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add App user',1,'add_customuser'),(2,'Can change App user',1,'change_customuser'),(3,'Can delete App user',1,'delete_customuser'),(4,'Can view App user',1,'view_customuser'),(5,'Can add Stat Data',2,'add_tabledata'),(6,'Can change Stat Data',2,'change_tabledata'),(7,'Can delete Stat Data',2,'delete_tabledata'),(8,'Can view Stat Data',2,'view_tabledata'),(9,'Can add image metadata',3,'add_imagemetadata'),(10,'Can change image metadata',3,'change_imagemetadata'),(11,'Can delete image metadata',3,'delete_imagemetadata'),(12,'Can view image metadata',3,'view_imagemetadata'),(13,'Can add log entry',4,'add_logentry'),(14,'Can change log entry',4,'change_logentry'),(15,'Can delete log entry',4,'delete_logentry'),(16,'Can view log entry',4,'view_logentry'),(17,'Can add permission',5,'add_permission'),(18,'Can change permission',5,'change_permission'),(19,'Can delete permission',5,'delete_permission'),(20,'Can view permission',5,'view_permission'),(21,'Can add group',6,'add_group'),(22,'Can change group',6,'change_group'),(23,'Can delete group',6,'delete_group'),(24,'Can view group',6,'view_group'),(25,'Can add content type',7,'add_contenttype'),(26,'Can change content type',7,'change_contenttype'),(27,'Can delete content type',7,'delete_contenttype'),(28,'Can view content type',7,'view_contenttype'),(29,'Can add session',8,'add_session'),(30,'Can change session',8,'change_session'),(31,'Can delete session',8,'delete_session'),(32,'Can view session',8,'view_session'),(33,'Can add group',9,'add_group'),(34,'Can change group',9,'change_group'),(35,'Can delete group',9,'delete_group'),(36,'Can view group',9,'view_group'),(37,'Can add email address',10,'add_emailaddress'),(38,'Can change email address',10,'change_emailaddress'),(39,'Can delete email address',10,'delete_emailaddress'),(40,'Can view email address',10,'view_emailaddress'),(41,'Can add email confirmation',11,'add_emailconfirmation'),(42,'Can change email confirmation',11,'change_emailconfirmation'),(43,'Can delete email confirmation',11,'delete_emailconfirmation'),(44,'Can view email confirmation',11,'view_emailconfirmation');
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
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_gym_app_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_gym_app_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `gym_app_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (10,'account','emailaddress'),(11,'account','emailconfirmation'),(4,'admin','logentry'),(6,'auth','group'),(5,'auth','permission'),(7,'contenttypes','contenttype'),(1,'gym_app','customuser'),(9,'gym_app','group'),(3,'gym_app','imagemetadata'),(2,'gym_app','tabledata'),(8,'sessions','session');
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
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-09-13 07:07:36.409911'),(2,'contenttypes','0002_remove_content_type_name','2023-09-13 07:07:36.646277'),(3,'auth','0001_initial','2023-09-13 07:07:37.775205'),(4,'auth','0002_alter_permission_name_max_length','2023-09-13 07:07:37.992921'),(5,'auth','0003_alter_user_email_max_length','2023-09-13 07:07:38.020154'),(6,'auth','0004_alter_user_username_opts','2023-09-13 07:07:38.042939'),(7,'auth','0005_alter_user_last_login_null','2023-09-13 07:07:38.064147'),(8,'auth','0006_require_contenttypes_0002','2023-09-13 07:07:38.080070'),(9,'auth','0007_alter_validators_add_error_messages','2023-09-13 07:07:38.101536'),(10,'auth','0008_alter_user_username_max_length','2023-09-13 07:07:38.119508'),(11,'auth','0009_alter_user_last_name_max_length','2023-09-13 07:07:38.148451'),(12,'auth','0010_alter_group_name_max_length','2023-09-13 07:07:38.204509'),(13,'auth','0011_update_proxy_permissions','2023-09-13 07:07:38.241301'),(14,'auth','0012_alter_user_first_name_max_length','2023-09-13 07:07:38.264887'),(15,'gym_app','0001_initial','2023-09-13 07:07:39.894011'),(16,'admin','0001_initial','2023-09-13 07:07:40.362792'),(17,'admin','0002_logentry_remove_auto_add','2023-09-13 07:07:40.384444'),(18,'admin','0003_logentry_add_action_flag_choices','2023-09-13 07:07:40.407014'),(19,'gym_app','0002_customuser_bio_customuser_dob_tabledata_date_and_more','2023-09-13 07:07:40.943320'),(20,'gym_app','0003_alter_tabledata_date','2023-09-13 07:07:41.081812'),(21,'gym_app','0004_alter_tabledata_date','2023-09-13 07:07:41.288283'),(22,'gym_app','0005_alter_tabledata_date','2023-09-13 07:07:41.537146'),(23,'gym_app','0006_alter_customuser_options_alter_tabledata_options_and_more','2023-09-13 07:07:41.754971'),(24,'sessions','0001_initial','2023-09-13 07:07:41.872137'),(25,'account','0001_initial','2023-09-13 07:35:25.108901'),(26,'account','0002_email_max_length','2023-09-13 07:35:25.170696'),(27,'account','0003_alter_emailaddress_create_unique_verified_email','2023-09-13 07:35:25.252572'),(28,'account','0004_alter_emailaddress_drop_unique_email','2023-09-13 07:35:25.376086'),(29,'account','0005_emailaddress_idx_upper_email','2023-09-13 07:35:25.450171'),(30,'gym_app','0007_group','2023-09-13 07:35:25.766225'),(31,'gym_app','0008_remove_group_bio_group_groupbio','2023-09-13 07:35:25.906787'),(32,'gym_app','0009_alter_group_groupbio','2023-09-13 07:35:26.033025'),(33,'gym_app','0010_customuser_current_group_alter_customuser_groups','2023-09-13 07:35:26.209262'),(34,'gym_app','0011_alter_customuser_current_group','2023-09-13 07:35:26.590708');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
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
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `profile_picture` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `bio` longtext COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT (_utf8mb3''),
  `dob` date DEFAULT NULL,
  `gender` varchar(1) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `current_group_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `gym_app_customuser_current_group_id_d9b1da1f_fk_gym_app_group_id` (`current_group_id`),
  CONSTRAINT `gym_app_customuser_current_group_id_d9b1da1f_fk_gym_app_group_id` FOREIGN KEY (`current_group_id`) REFERENCES `gym_app_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gym_app_customuser`
--

LOCK TABLES `gym_app_customuser` WRITE;
/*!40000 ALTER TABLE `gym_app_customuser` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `privacy` varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_by_id` bigint NOT NULL,
  `groupbio` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gym_app_group_created_by_id_964b192e_fk_gym_app_customuser_id` (`created_by_id`),
  CONSTRAINT `gym_app_group_created_by_id_964b192e_fk_gym_app_customuser_id` FOREIGN KEY (`created_by_id`) REFERENCES `gym_app_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gym_app_group`
--

LOCK TABLES `gym_app_group` WRITE;
/*!40000 ALTER TABLE `gym_app_group` DISABLE KEYS */;
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
  `image` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `caption` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gym_app_imagemetadata_user_id_cb8eca4c_fk_gym_app_customuser_id` (`user_id`),
  CONSTRAINT `gym_app_imagemetadata_user_id_cb8eca4c_fk_gym_app_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `gym_app_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gym_app_imagemetadata`
--

LOCK TABLES `gym_app_imagemetadata` WRITE;
/*!40000 ALTER TABLE `gym_app_imagemetadata` DISABLE KEYS */;
/*!40000 ALTER TABLE `gym_app_imagemetadata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gym_app_tabledata`
--

DROP TABLE IF EXISTS `gym_app_tabledata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gym_app_tabledata` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `data_title` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `data_value` decimal(10,2) NOT NULL,
  `user_id` bigint NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gym_app_tabledata_user_id_aa4296ff_fk_gym_app_customuser_id` (`user_id`),
  CONSTRAINT `gym_app_tabledata_user_id_aa4296ff_fk_gym_app_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `gym_app_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gym_app_tabledata`
--

LOCK TABLES `gym_app_tabledata` WRITE;
/*!40000 ALTER TABLE `gym_app_tabledata` DISABLE KEYS */;
/*!40000 ALTER TABLE `gym_app_tabledata` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-18 17:50:03
