import psycopg2


def insert(persons: list):
    exit = True
    try:

        connection = psycopg2.connect(dbname='testdb', user='postgres', password='1234', host='127.0.0.1')
        with connection.cursor() as cursor:
            for person in persons:
                sql = "INSERT INTO public.persons (name, addtime) VALUES ('" + person[0] + "', '" + person[1] + "');"
                cursor.execute(sql)
            connection.commit()
            cursor.close()


    except psycopg2.OperationalError:
        print("Ошибка соединения с базой данных!")
        exit = False

    finally:
        if exit == True:
            connection.close()
    return exit


def select_all():
    exit = True

    try:
        sql = "SELECT id, name , addtime from persons;"
        connection = psycopg2.connect(dbname='testdb', user='postgres', password='1234', host='127.0.0.1')
        print(connection)
        # if connection.is_connected():
        #     print('Connected to PostgreSQL database')
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print("Id: ", row[0], " Имя: ", row[1], " Время: ", row[2])
            connection.commit()
            cursor.close()


    except psycopg2.OperationalError:
        print("Ошибка соединения с базой данных!")
        exit = False

    finally:
        if exit == True:
            connection.close()


def test_connection(dbname: str, user: str, password: str, host: str):
    exit = True

    try:
        connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

    except psycopg2.OperationalError:
        exit = False

    finally:
        if exit == True:
            connection.close()
    return exit


def select(info : list, sql : str):
    exit = True
    result = []
    try:
        connection = psycopg2.connect(dbname=info[0], user=info[1], password=info[2], host=info[3])
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
            column = len(rows[0])
            for row in rows:
                res = []
                for i in range(column):
                    res.append(row[i])
                result.append(res)
            connection.commit()
            cursor.close()


    except psycopg2.OperationalError:
        print("Ошибка соединения с базой данных!")
        exit = False

    finally:
        if exit == True:
            connection.close()
    return result
# print(check_connection(dbname='testdb', user='postgres', password='1234', host='127.0.0.1'))
