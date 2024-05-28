import pymysql
def get_wards_data(cursor):
    cursor.execute('''select * from wards''')
    for data in cursor:
        print(f'id: {data[0]}; name: {data[1]}; floor: {data[2]}; department id: {data[3]}')

def get_doctors_phone_and_lastname(cursor):
    cursor.execute('''select phone, last_name from doctors''')
    for data in cursor:
        print(f'Телефон: {data[0]}; Фамилия: {data[1]}')

def get_departnet_floors(cursor):
    cursor.execute('''select distinct floor from wards''')
    print('Этажи')
    for data in cursor:
        print(*data)

def get_diseases_and_severity(cursor):
    cursor.execute('''select severity, diseases_name from diseases''')
    for data in cursor:
        print(f':Название болезни {data[0]}; Степень тяжести: {data[1]}')

def get_doctors_salary(cursor):
    cursor.execute('''select last_name from doctors Where salary>350000''')
    for data in cursor:
        print(f'Фамилия: {data[0]}')

def get_depart_fin(cursor):
    cursor.execute('''select department_name from departments where (building = 3 and financing > 50000 and financing < 350000)''')
    for data in cursor:
        print(f'Название отделения: {data[0]}')

def get_case_7(cursor):
    cursor.execute('''select ward_name from wards where (department_id = 4 and department_id = 5 and floor = 1) ''')
    for data in cursor:
        print(f'Название палаты: {data[0]}')

def full_patients(cursor):
    cursor.execute('''select * from Patients''')
    for data in cursor:
        print(f'id: {data[0]};  first_name: {data[1]}; last_name: {data[2]}; date_of_birth: {data[3]}; date_of_admission: {data[4]}; ward_id: {data[5]}')

def patients_and_doctor(cursor):
    cursor.execute('''select * from Patient_Doctor''')
    for data in cursor:
        print(*data)