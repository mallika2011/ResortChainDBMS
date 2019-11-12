-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: RESORT
-- ------------------------------------------------------
-- Server version 5.7.23-0ubuntu0.18.04.1
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
--
-- Table structure for table DESTINATION
--
DROP DATABASE IF EXISTS RESORT;
CREATE SCHEMA RESORT;
USE RESORT;

DROP TABLE IF EXISTS DESTINATION;
CREATE TABLE DESTINATION (
  Hotel_ID varchar(4) NOT NULL,
  Hotel_Name varchar(100) NOT NULL,
  Location varchar(100) NOT NULL,
  Manager_ID varchar(4) NOT NULL,
  PRIMARY KEY (Hotel_ID),
  UNIQUE KEY Hotel_Name (Hotel_Name),
  UNIQUE KEY Manager_ID (Manager_ID),
  CONSTRAINT DESTINATION_ibfk_1 FOREIGN KEY (Manager_ID) REFERENCES EMPLOYEE (Employee_ID)
  ON UPDATE RESTRICT
  ON DELETE RESTRICT 
) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES DESTINATION WRITE;
INSERT INTO DESTINATION
VALUES
  (
    '1',
    'Whitefields',
    'Rangree, Manali, Himachal Pradesh, 2',
    '2'
  ),(
    '2',
    'Exotic Stay',
    'Plot F 8,Tiswadi, Panjim,Bainguinim, Goa, 403110',
    '1'
  ),(
    '3',
    'Palm Springs',
    '3rd Street, Raj Lane, Podicherry',
    '7'
  ),('4', 'Mountain View', '118,Raj-road,Shimla', '6');
UNLOCK TABLES;

DROP TABLE IF EXISTS MEMBERS;
CREATE TABLE MEMBERS (
    Member_ID varchar(4) NOT NULL,
    First_Name varchar(100) NOT NULL,
    Last_Name varchar(100) NOT NULL,
    Date_of_Reg date NOT NULL,
    DOB date NOT NULL,
    Email_ID varchar(100) NOT NULL,
    Monthly_Fee int(5) NOT NULL,
    PRIMARY KEY (Member_ID)
  ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES MEMBERS WRITE;
INSERT INTO MEMBERS
VALUES
  (
    '1',
    'Raj',
    'Dewan',
    '2017-01-18',
    '1998-02-19',
    'raj.dewan@gmail.com',
    '500'
  ),(
    '2',
    'Yaseen',
    'Hafish',
    '2001-11-29',
    '1988-02-14',
    'yas.hash@yahoo.com',
    '330'
  );
UNLOCK TABLES;

DROP TABLE IF EXISTS MEMBER_PACKAGE;
CREATE TABLE MEMBER_PACKAGE (
    Member_ID varchar(4) NOT NULL,
    Package varchar(8) NOT NULL,
    PRIMARY KEY (Member_ID, Package),
    CONSTRAINT MEMBER_PACKAGE_ibfk_1 FOREIGN KEY (Member_ID) REFERENCES MEMBERS (Member_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
  ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES MEMBER_PACKAGE WRITE;
INSERT INTO MEMBER_PACKAGE
VALUES
  ('1', 'Red'),('1', 'Blue'),('2', 'Green');
UNLOCK TABLES;

DROP TABLE IF EXISTS MEMBER_ADDRESS;
CREATE TABLE MEMBER_ADDRESS (
    Member_ID varchar(4) NOT NULL,
    Address varchar(100) NOT NULL,
    PRIMARY KEY (Member_ID, Address),
    CONSTRAINT MEMBER_ADDRESS_ibfk_1 FOREIGN KEY (Member_ID) REFERENCES MEMBERS (Member_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
  ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES MEMBER_ADDRESS WRITE;
INSERT INTO MEMBER_ADDRESS
VALUES
  (
    '1',
    'C 29, Part 2, South Extn, Bangalore, India-412932'
  ),(
    '2',
    'Flat No. 100,Triveni Apartments, itam Pura, India-411002'
  ),(
    '2',
    'Ispat Bhavan, Lodhi Road, Bikaner, India-411057'
  );
UNLOCK TABLES;

DROP TABLE IF EXISTS MEMBER_PHONE;
CREATE TABLE MEMBER_PHONE (
    Member_ID varchar(4) NOT NULL,
    Ph_No varchar(10) NOT NULL,
    PRIMARY KEY (Member_ID, Ph_No),
    CONSTRAINT MEMBER_PHONE_ibfk_1 FOREIGN KEY (Member_ID) REFERENCES MEMBERS (Member_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
  ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES MEMBER_PHONE WRITE;
INSERT INTO MEMBER_PHONE
VALUES
  ('1', '9932394392'),(1, '7023143824'),('2', '9328348283');
UNLOCK TABLES;

DROP TABLE IF EXISTS FINANCE;
CREATE TABLE FINANCE (
    Hotel_ID varchar(4) NOT NULL,
    Expenditure int(10) NOT NULL,
    Income int(10) NOT NULL,
    Month varchar(10) NOT NULL,
    Profit int(10) NOT NULL,
    PRIMARY KEY (Hotel_ID, Month),
    CONSTRAINT FINANCE_ibfk_1 FOREIGN KEY (Hotel_ID) REFERENCES DESTINATION (Hotel_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
  ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES FINANCE WRITE;
INSERT INTO FINANCE
VALUES
  ('1', 1000000, 2000000, 'July', '1000000'),('2', 1000000, 2100000, 'July', '1100000');
UNLOCK TABLES;

DROP TABLE IF EXISTS EMPLOYEE;
CREATE TABLE EMPLOYEE (
    Employee_ID varchar(4) NOT NULL,
    First_Name varchar(100) NOT NULL,
    Last_Name varchar(100) NOT NULL,
    Salary int(9) NOT NULL,
    DOB date NOT NULL,
    Hotel_ID varchar(4) NOT NULL,
    Email_ID varchar(100) NOT NULL,
    PRIMARY KEY (Employee_ID)
  ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES EMPLOYEE WRITE;
INSERT INTO EMPLOYEE
VALUES
  (
    '1',
    'A',
    'B',
    '20000',
    '1988-02-09',
    '2',
    'abc@gmail.com'
  ),(
    '2',
    'X',
    'Y',
    '20000',
    '1988-02-09',
    '1',
    'def@gmail.com'
  ),(
    '3',
    'C',
    'D',
    '30000',
    '1998-02-14',
    '1',
    'pqr@gmail.com'
  ),(
    '4',
    'E',
    'F',
    '25000',
    '1988-02-09',
    '2',
    'xyz@gmail.com'
  ),(
    '5',
    'Q',
    'T',
    '70000',
    '1988-02-19',
    '2',
    'qwe1@gmail.com'
  ),(
    '6',
    'K',
    'L',
    '45000',
    '1988-02-09',
    '4',
    'rty@gmail.com'
  ),(
    '7',
    'M',
    'N',
    '27000',
    '1988-02-09',
    '3',
    'lmn@gmail.com'
  );
UNLOCK TABLES;

DROP TABLE IF EXISTS EMPLOYEE_ADDRESS;
CREATE TABLE EMPLOYEE_ADDRESS (
    Employee_ID varchar(4) NOT NULL,
    Address varchar(100) NOT NULL,
    PRIMARY KEY (Employee_ID, Address),
    CONSTRAINT EMPLOYEE_ADDRESS_ibfk_1 FOREIGN KEY (Employee_ID) REFERENCES EMPLOYEE (Employee_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
  ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES EMPLOYEE_ADDRESS WRITE;
INSERT INTO EMPLOYEE_ADDRESS
VALUES
  ('1', 'Noida Delhi'),('1', 'Madurai, Tamil Nadu'),('2', 'Banglore, Karnataka'),('3', 'Banglore, Karnataka'),('3', 'Chennai, Tamil Nadu'),('4', 'Pune, Maharashtra'),('5', 'Madurai, Tamil Nadu'),('6', 'Madurai, Tamil Nadu'),('7', 'Hyderabad, Telangana');
UNLOCK TABLES;

DROP TABLE IF EXISTS EMPLOYEE_PHONE;
CREATE TABLE EMPLOYEE_PHONE (
    Employee_ID varchar(4) NOT NULL,
    Ph_No varchar(10) NOT NULL,
    PRIMARY KEY (Employee_ID, Ph_No),
    CONSTRAINT EMPLOYEE_PHONE_ibfk_1 FOREIGN KEY (Employee_ID) REFERENCES EMPLOYEE (Employee_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
  ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES EMPLOYEE_PHONE WRITE;
INSERT INTO EMPLOYEE_PHONE
VALUES
  ('1', '9273183746'),('1', '8234567892'),('2', '8234567891'),('3', '7634566666'),('3', '7634566655'),('4', '9292929292'),('5', '8282828282'),('6', '9123929123'),('7', '8237465748');
UNLOCK TABLES;

DROP TABLE IF EXISTS MEMBER_GUESTS;
CREATE TABLE MEMBER_GUESTS (
    Hotel_ID varchar(4) NOT NULL,
    Room_No varchar(5) NOT NULL,
    Member_ID varchar(4) NOT NULL,
    Check_In_Date date NOT NULL,
    Check_Out_Date date NOT NULL,
    Cost_Of_Staying int(5) NOT NULL,
    PRIMARY KEY (Hotel_ID, Room_No),
    CONSTRAINT MEMBER_GUESTS_ibfk_1 FOREIGN KEY (Hotel_ID) REFERENCES DESTINATION (Hotel_ID)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,  -- CANNOT DELETE HOTEL IF PPL ARE STAYING   
    CONSTRAINT MEMBER_GUESTS_ibfk_2 FOREIGN KEY (Member_ID) REFERENCES MEMBERS (Member_ID)
    ON UPDATE CASCADE  
    ON DELETE RESTRICT  -- CANNOT CANCEL MEMBERSHIP WHILE STAYING IN HOTEL 
  ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES MEMBER_GUESTS WRITE;
INSERT INTO MEMBER_GUESTS
VALUES
  ('1', '2', '2', '2019-11-01', '2019-11-28', 5000),('2', '2', '1', '2019-11-02', '2019-11-20', 5600);
UNLOCK TABLES;

DROP TABLE IF EXISTS NON_MEMBER_GUESTS;
CREATE TABLE NON_MEMBER_GUESTS (
    Hotel_ID varchar(4) NOT NULL,
    Room_No varchar(5) NOT NULL,
    First_Name varchar(100) NOT NULL,
    Last_Name varchar(100) NOT NULL,
    Check_In_Date date NOT NULL,
    Check_Out_Date date NOT NULL,
    Cost_Of_Staying int(5) NOT NULL,
    Phone_Number varchar(10) DEFAULT NULL,
    PRIMARY KEY (Hotel_ID, Room_No),
    CONSTRAINT NON_MEMBER_GUESTS_ibfk_1 FOREIGN KEY (Hotel_ID) REFERENCES DESTINATION (Hotel_ID)
    ON UPDATE CASCADE
    ON DELETE RESTRICT -- CANNOT DELETE HOTEL IF PPL ARE STAYING
  ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES NON_MEMBER_GUESTS WRITE;
INSERT INTO NON_MEMBER_GUESTS
VALUES
  (
    '1',
    '1',
    'Manish',
    'Mamma',
    '2019-10-29',
    '2019-11-29',
    9600,
    '9123219231'
  );
UNLOCK TABLES;

DROP TABLE IF EXISTS RECREATION;
CREATE TABLE RECREATION (
    Hotel_ID varchar(4) NOT NULL,
    Service_Provider varchar(100) NOT NULL,
    Supervisor_ID varchar(4) NOT NULL,
    Profit int(10) NOT NULL,
    PRIMARY KEY (Hotel_ID, Service_Provider),
    CONSTRAINT RECREATION_ibfk_1 FOREIGN KEY (Hotel_ID) REFERENCES DESTINATION (Hotel_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT RECREATION_ibfk_2 FOREIGN KEY (Service_Provider) REFERENCES PROVIDERS_SERVICES (Service_Provider) 
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT RECREATION_ibfk_3 FOREIGN KEY (Supervisor_ID) REFERENCES EMPLOYEE (Employee_ID)
    ON UPDATE RESTRICT
    ON DELETE RESTRICT
  ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES RECREATION WRITE;
INSERT INTO RECREATION
VALUES
  ('1', 'Ching Ma', '1', 500),('1', 'Udipi', '2', 1000),('2', 'Ching Ma', '5', 500);
UNLOCK TABLES;

DROP TABLE IF EXISTS PROVIDERS_SERVICES;
CREATE TABLE PROVIDERS_SERVICES (
    Service_Provider varchar(100) NOT NULL,
    Service_Description varchar(100) NOT NULL,
    Service_Price int(10) NOT NULL,
    PRIMARY KEY (Service_Provider)
  ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES PROVIDERS_SERVICES WRITE;
INSERT INTO PROVIDERS_SERVICES
VALUES
  ('Ching Ma', 'Chinese Restaurant', 123),('Udipi', 'South Indian Restaurant', 23);
UNLOCK TABLES;

DROP TABLE IF EXISTS HOTEL_I;
CREATE TABLE HOTEL_I (
    isMember BOOL,
    isOccupied BOOL NOT NULL,
    Room_Type varchar(100) NOT NULL,
    Price_Day int(5) NOT NULL,
    Room_Number varchar(5) NOT NULL,
    Hotel_ID varchar(4) NOT NULL,
    PRIMARY KEY (Room_Number, Hotel_ID),
    CONSTRAINT HOTEL_I_ibfk_1 FOREIGN KEY (Hotel_ID) REFERENCES DESTINATION (Hotel_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
  ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES HOTEL_I WRITE;
INSERT INTO HOTEL_I
VALUES
  (FALSE, TRUE, 'Studio', 300, '1', '1'),(TRUE, TRUE, 'Duplex', 500, '2', '1'),(NULL, FALSE, 'Studio', 500, '1', '2'),(TRUE, TRUE, 'Duplex', 800, '2', '2'),(NULL, FALSE, 'Studio', 500, '1', '3'),(NULL, FALSE, 'Studio', 500, '2', '3'),(NULL, FALSE, 'Studio', 500, '1', '4'),(NULL, FALSE, 'Studio', 500, '2', '4');
UNLOCK TABLES;

DROP TABLE IF EXISTS FACILITIES_AVAILED;
CREATE TABLE FACILITIES_AVAILED (
    Member_ID varchar(4) NOT NULL,
    Service_Provider varchar(100) NOT NULL,
    Number_of_times int(2) NOT NULL,
    PRIMARY KEY (Member_ID, Service_Provider),
    CONSTRAINT FACILITIES_AVAILED_ibfk_1 FOREIGN KEY (Service_Provider) REFERENCES PROVIDERS_SERVICES (Service_Provider)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    CONSTRAINT FACILITIES_AVAILED_ibfk_2 FOREIGN KEY (Member_ID) REFERENCES MEMBERS (Member_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
  ) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES FACILITIES_AVAILED WRITE;
INSERT INTO FACILITIES_AVAILED
VALUES
  ('1', 'Ching Ma', 2),('2', 'Ching Ma', 1);
UNLOCK TABLES;