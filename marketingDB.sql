CREATE TABLE information (
    objectID int primary key,
    town varchar(20),
    streetaddress varchar(30),
    zipcode char(5),
    age int,
    amount decimal(10,2) not null,
    race varchar(20),
    popCount int not null,
    lng varchar(20),
    lat varchar(20)
);

/* Zip Code data from Python imported */

/* Test Data 

INSERT INTO information VALUES(1, "Houston", "670 McKinney St", "77067", 30, 5000.00, "White", 5000);
INSERT INTO information VALUES(2, "San Antonio", "670 McKinney St", "77067", 30, 78500.52, "White", 5000);
INSERT INTO information VALUES(3, "Dallas", "670 McKinney St", "77067", 30, 0, "White", 5000);
INSERT INTO information VALUES(4, "El Paso", "670 McKinney St", "77067", 30, 0, "White", 5000);
INSERT INTO information VALUES(5, "New York", "670 McKinney St", "77067", 30, 9, "White", 5000);

SELECT * FROM information

*/

