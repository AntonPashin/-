import pymysql
def create_database(cursor,connection):
    cursor.execute('''CREATE DATABASE IF NOT EXISTS P312_hospital''')
    cursor.execute('''USE P312_hospital''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Departments(
    id INT AUTO_INCREMENT PRIMARY KEY,
    building INT NOT NULL CHECK(building BETWEEN 1 AND 5),
    financing decimal(10,2) not null check(financing >= 0),
    department_name varchar(100) not null unique
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Diseases(
    id INT AUTO_INCREMENT PRIMARY KEY,
    severity int not null default 1 check(severity >= 0),
    diseases_name varchar(100) not null unique
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Doctors(
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name varchar(100) not null,
        last_name varchar(100) not null,
        phone varchar(12) not null,
        salary decimal(10,2) not null check(salary > 0)
        )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Examinations(
            id INT AUTO_INCREMENT PRIMARY KEY,
            examinations_name varchar(100) not null unique,
            day_of_week INT NOT NULL CHECK(day_of_week BETWEEN 1 AND 7),
            start_time time not null check(start_time>= '08:00:00' and start_time< '18:00:00'),
            end_time time not null check(end_time > start_time)
            )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Wards(
            id INT AUTO_INCREMENT PRIMARY KEY,
            ward_name varchar(100) not null unique,
            floor int not null check(floor >= -1),
            department_id int,
            foreign key(department_id) references departments(id)
            )''')
    cursor.execute('''create table if not exists doctors_and_examinations(
    doctor_id int,
    examination_id int,
    primary key(doctor_id,examination_id),
    foreign key(doctor_id) references doctors(id),
    foreign key(examination_id) references examinations(id)
    )''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Patients (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            date_of_birth DATE,
            date_of_admission DATE,
            ward_id INT,
            FOREIGN KEY (ward_id) REFERENCES Wards(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Patient_Doctor (
            patient_id INT,
            doctor_id INT,
            FOREIGN KEY (patient_id) REFERENCES Patients(id),
            FOREIGN KEY (doctor_id) REFERENCES Doctors(id)
        )
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Patient_Disease (
            patient_id INT,
            disease_id INT,
            FOREIGN KEY (patient_id) REFERENCES Patients(id),
            FOREIGN KEY (disease_id) REFERENCES Diseases(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Patient_Examinations (
            patient_id INT,
            examinations_id INT,
            FOREIGN KEY (patient_id) REFERENCES Patients(id),
            FOREIGN KEY (examinations_id) REFERENCES Examinations(id)
        )
    ''')
    print("База данных про госпиталь со всеми таблицами добавлена.")