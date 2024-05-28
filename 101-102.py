import pymysql
from sql_queries import creates_queries,delete_quries,get_data_queries
import decimal

if __name__=='__main__':
    try:
        with pymysql.connect(host = '127.0.0.1', port=3306, user='root', password='') as connection:
            print(connection,'ok')
            with connection.cursor() as cursor:
                while True:
                    print('-'*100)
                    print('1. Создать базу данных с таблицами.')
                    print('2. Подключиться к базе данных госпиталя.')
                    print('5. Особые запросы')
                    print('99. Удалить базу данных hospital')
                    print('0. Выход.')
                    user_choice = input('Ваш выбор: ')
                    match user_choice:
                        case '0':
                            connection.close()
                            quit()
                        case '1':
                            creates_queries.create_database(cursor,connection)
                        case '2':
                            cursor.execute('''use p312_hospital''')
                            print('Подключение успешно')
                        case '5':
                            print('1. Вывести содержимое таблицы палат')
                            print('2. Вывести фамилии и телефоны врачей')
                            print('3. Вывести все этажи(без повторов)')
                            print('4. Вывести названия болезней и их степень тяжести')
                            print('5. Вывести фамилии докторов, зарплата которых превышает 350000')
                            print('6. Вывести названия отделений в 3 корпусе и с фондом финансирования от 50тыс до 350тыс')
                            print('7. Вывести названия палат, расположенных в корпусах 4 и 5 на 1-м этаже')
                            print('8. Вывести всех пациентов')
                            print('9. Вывести докторов и их пациентов')
                            user_choice = input('Ваш выбор')
                            match user_choice:
                                case '1':
                                    get_data_queries.get_wards_data(cursor)
                                case '2':
                                    get_data_queries.get_doctors_phone_and_lastname(cursor)
                                case '3':
                                    get_data_queries.get_departnet_floors(cursor)
                                case '4':
                                    get_data_queries.get_diseases_and_severity(cursor)
                                case '5':
                                    get_data_queries.get_doctors_salary(cursor)
                                case '6':
                                    get_data_queries.get_depart_fin(cursor)
                                case '7':
                                    get_data_queries.get_case_7(cursor)
                                case '8':
                                    get_data_queries.full_patients(cursor)
                                case '9':
                                    get_data_queries.patients_and_doctor(cursor)
                                case _:
                                    print('Неизвестная команда')


                        case '99':
                            delete_quries.delete_database(cursor,connection)
                        case _:
                            print('Неизвестная команда')



    except pymysql.Error as e:
        print(e)