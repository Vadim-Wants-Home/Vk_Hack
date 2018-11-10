import logging

import torndb

host = "db"
db = "testvk"
user = "root"
password = "password"

def get_connection():
    try:
        connection = torndb.Connection(host, db, user, password)
        connection.execute('set time_zone=SYSTEM')
        connection.execute('SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci')

        return connection
    except:
        logging.error("Can not connect to db")