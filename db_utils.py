import logging
from json_working.json_working import get_json_data

import torndb

def get_connection():
    try:
        data = get_json_data('db.json')
        connection = torndb.Connection(data['host'], data['db'], data['user'], data['password'])
        connection.execute('set time_zone=SYSTEM')
        connection.execute('SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci')

        return connection
    except:
        logging.error("Can not connect to db")