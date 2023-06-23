DROP DATABASE IF EXISTS ssis;
CREATE DATABASE ssis;
USE ssis;

CREATE TABLE courses (
    code VARCHAR(10) NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (code)
);

CREATE TABLE students (
	id_num VARCHAR(9) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    year_level INT,
    gender ENUM('Male', 'Female', 'Lesbian', 'Gay', 'Bisexual', 'Transgender', 'Prefer not to say'),
    course VARCHAR(10) NOT NULL,
    PRIMARY KEY (id_num),
    FOREIGN KEY (course) REFERENCES courses(code) ON DELETE CASCADE
);

INSERT INTO courses (code, name)
VALUES 	('BSCS', 'Bachelor of Science in Computer Science'), 
		('BSIT', 'Bachelor of Science in Information Technology'),
        ('BSCA', 'Bachelor of Science in Computer Application'),
        ('BSIS', 'Bachelor of Science in Informations Systems'),
        ('BAPS','Bachelor of Arts in Political Science'),
        ('BSBIO','Bachelor of Science in Biology'),
        ('BAHIS','Bachelor of Arts in History'),
        ('BAFIL','Bachelor of Arts in Filipino'),
        ('BAELS','Bachelor of Arts in English Language Studies'),
        ('BSCHEM','Bachelor of Science in Chemistry');

INSERT INTO students (id_num, first_name, last_name, year_level, gender, course)
VALUES 	('2021-1732', 'Salazar', 'Slytherin', '2', 'Male', 'BSCS'),
		('2019-2393', 'Rowena', 'Ravenclaw', '4', 'Female', 'BSCS'),
        ('2019-2362', 'Godrick', 'Gryffindor', '4', 'Male', 'BSCS'),
        ('2020-1071', 'Helga', 'Hufflepuff', '2', 'Female', 'BSCS'),
        ('2021-0035', 'Albus', 'Dumbledore', '2', 'Gay', 'BSCS'),
        
        ('2021-1235', 'Harry', 'Potter', '2', 'Male', 'BAELS'),
        ('2021-0228', 'Ronald', 'Weasley', '2', 'Male', 'BAELS'),
        ('2021-2123', 'Hermione', 'Granger', '2', 'Female', 'BAELS'),
        ('2020-2186', 'Neville', 'Longbottom', '2', 'Male', 'BAELS'),
        ('2022-2127', 'Dean', 'Thomas', '1', 'Gay', 'BAELS'),        
        
        ('2019-2190', 'Sirius', 'Black', '4', 'Bisexual', 'BAFIL'),
        ('2019-0995', 'Lily', 'Evans', '4', 'Female', 'BAFIL'),
        ('2019-2194', 'Remus', 'Lupin', '4', 'Prefer not to say', 'BAFIL'),
        ('2019-1283', 'James', 'Potter', '4', 'Male', 'BAFIL'),
        ('2021-1284', 'Mary', 'Mcdonald', '2', 'Lesbian', 'BAFIL'),
        
        ('2019-2085', 'Severus', 'Snape', '4', 'Male', 'BAHIS'),
        ('2020-1790', 'Regulus', 'Black', '3', 'Male', 'BAHIS'),
        ('2021-2237', 'Marlene', 'Mckinnon', '2', 'Lesbian', 'BAHIS'),
        ('2019-0195', 'Narcissa', 'Black', '4', 'Female', 'BAHIS'),
        ('2019-2806', 'Peter', 'Pettigrew', '3', 'Male', 'BAHIS'),        
        
        ('2022-0206', 'Millicent', 'Bulstrode', '1', 'Female', 'BAPS'),
        ('2021-0243', 'Pansy', 'Parkinson', '2', 'Bisexual', 'BAPS'),
        ('2022-1792', 'Theodore', 'Nott', '1', 'Male', 'BAPS'),
        ('2021-0256', 'Blaise', 'Zabini', '2', 'Gay', 'BAPS'),
        ('2021-0882', 'Draco', 'Malfoy', '2', 'Male', 'BAPS'),        
        
        ('2022-2547', 'Luna', 'Lovegood', '1', 'Female', 'BSBIO'),
        ('2022-1885', 'Ginny', 'Weasley', '1', 'Male', 'BSBIO'),
        ('2021-2000', 'Padma', 'Patil', '2', 'Female', 'BSBIO'),
        ('2020-1172', 'Cho', 'Chang', '3', 'Female', 'BSBIO'),
        ('2020-1412', 'Eddie', 'Carmichael', '3', 'Male', 'BSBIO'),
        
        ('2020-1200', 'George', 'Weasley', '3', 'Male', 'BSCA'),
        ('2020-1267', 'Fred', 'Weasley', '3', 'Male', 'BSCA'),
        ('2021-0389', 'Patricia', 'Stimpson', '2', 'Female', 'BSCA'),
        ('2021-0336', 'Cormac', 'Mclaggen', '2', 'Male', 'BSCA'),
        ('2022-1340', 'Lavender', 'Brown', '1', 'Female', 'BSCA'),        
        
        ('2019-1355', 'Hannah', 'Abbot', '4', 'Female', 'BSCHEM'),
        ('2020-1486', 'Susan', 'Bones', '3', 'Female', 'BSCHEM'),
        ('2021-1547', 'Justin Finch', 'Fletchely', '2', 'Male', 'BSCHEM'),
        ('2018-1373', 'Megan', 'Jones', '4', 'Female', 'BSCHEM'),
        ('2021-2714', 'Zacharias', 'Smith', '2', 'Male', 'BSCHEM'),        
        
        ('2022-1386', 'Teddy', 'Lupin', '1', 'Bisexual', 'BSIS'),
        ('2022-1746', 'Rose', 'Granger-Weasley', '1', 'Female', 'BSIS'),
        ('2021-0395', 'James Sirius', 'Potter', '2', 'Male', 'BSIS'),
        ('2022-2723', 'Albus Severus', 'Potter', '1', 'Bisexual', 'BSIS'),
        ('2022-0399', 'Scorpius', 'Malfoy', '1', 'Male', 'BSIS'),        
        
        ('2020-0677', 'Cedric', 'Diggory', '3', 'Male', 'BSIT'),
        ('2020-1434', 'Nymphadora', 'Tonks', '3', 'Prefer not to say', 'BSIT'),
        ('2019-0424', 'Pomona', 'Sprout', '4', 'Female', 'BSIT'),
        ('2018-1569', 'Newt', 'Scamander', '4', 'Male', 'BSIT'),
        ('2018-1832', 'Minerva', 'Mcgonagall', '4', 'Female', 'BSIT');
