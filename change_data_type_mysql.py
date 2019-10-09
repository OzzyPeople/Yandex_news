import pymysql

def change_data_type(host, user, password, db_name):

    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=db_name,
        charset='utf8mb4',
    )

    try:
        with connection.cursor() as conn:

            sql1 = "ALTER TABLE news_yandex\
            MODIFY id INT NOT NULL,\
            MODIFY title VARCHAR(512) NULL DEFAULT NULL, \
            MODIFY date DATE NULL DEFAULT NULL,\
            ADD PRIMARY KEY(id);"

            conn.execute(sql1)
            connection.commit()

    finally:
        connection.close()