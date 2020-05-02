import psycopg2


def insert(info: list, event: list, student_id: list):
    exit = True
    try:
        connection = psycopg2.connect(dbname=info[0], user=info[1], password=info[2], host=info[3], port="5432")
        with connection.cursor() as cursor:
            sql1 = "INSERT INTO public.event(instructor_id, subject_id, class_type_id, classes_id, class_date, group_id) VALUES (" + str(
                event[0]) + "," + str(event[1]) + "," + str(
                event[2]) + "," + str(event[3]) + ",'" + str(event[4]) + "', " + str(event[5]) + ") RETURNING id;"
            cursor.execute(sql1)
            event_id = cursor.fetchone()[0]
            for stud_id in student_id:
                sql2 = "INSERT INTO public.attendance(event_id, student_id)	VALUES (" + str(event_id) + "," + str(
                    stud_id) + ");"
                cursor.execute(sql2)
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
        connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port="5432")

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
        connection = psycopg2.connect(dbname=info[0], user=info[1], password=info[2], host=info[3], port="5432")
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

            if len(rows) == 0:
                res = []
                result.append(res)
            else:
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
