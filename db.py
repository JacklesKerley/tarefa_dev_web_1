import pymysql

def connect ():
    connection = None
    try:
        connection = pymysql.connect(
            user = "root",
            password = "adm12345",
            host = '127.0.0.1',
            port = 3306,
            database = 'project_unes',
            cursorclass=pymysql.cursors.DictCursor
        )
        connection.auto_reconnect = True
        connection.autocommit = True
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
    return connection