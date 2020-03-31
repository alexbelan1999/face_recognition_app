import psycopg2


def insert(info: list, students: list):
    exit = True
    try:
        connection = psycopg2.connect(dbname=info[0], user=info[1], password=info[2], host=info[3])
        with connection.cursor() as cursor:
            for student in students:
                sql = "INSERT INTO public.attendance(student_id, instructor_id, subject_id, class_type_id, classes_id, class_date) VALUES (" + \
                      str(student[0]) + "," + str(student[1]) + "," + str(student[2]) + "," + str(
                    student[3]) + "," + str(student[4]) + ",'" + str(student[5]) + "');"
                cursor.execute(sql)
            connection.commit()
            cursor.close()

    except psycopg2.OperationalError:
        exit = False

    finally:
        if exit == True:
            connection.close()
    return exit


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


def select(info: list, sql: str):
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
        exit = False

    finally:
        if exit == True:
            connection.close()
    return result
