import logging

from tornado.web import RequestHandler
import json
import db_utils

class UserCreateHandler(RequestHandler):
    def get(self):
        self.post()

    def post(self):
        conn = db_utils.get_connection()

        try:
            data = json.loads(self.request.body)
            conn.execute("""
            insert into users(user_id, first_name, last_name, birthday, photo)
            values({user_id}, '{first_name}', '{last_name}', '{birthday}', '{photo}');
                """.format(**data))
            self.write(json.dumps({'result': 'ok'}))
        except Exception, e:
            logging.warn('cannot insert data: ' + str(e))
            self.write(json.dumps({'result': 'fail'}))
