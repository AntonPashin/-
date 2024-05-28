import pymysql
def delete_database(cursor,connectoin):
    cursor.execute('''DROP DATABASE P312_hospital''')
    print('База данных удалена')
