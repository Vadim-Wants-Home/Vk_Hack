
import logging

from tornado.web import RequestHandler
import json
import db_utils

class RepresentativesCreateHandler(RequestHandler):
    def get(self):
        self.post()

    def get_shelter_id(self, conn, code):
        rows = conn.query(
            """
                select *
                from codes as s
                {0};
            """.format(where_statement)
        )

    def post(self):
        conn = db_utils.get_connection()

        try:
            data = json.loads(self.request.body)
            data['shelter_id'] = self.get_shelter_id(conn, data['code'])
            birthday = ''
            for el in reversed(data['birthday'].split('.')):
                birthday += '-' + el
            birthday = birthday[1:]

            data['birthday'] = birthday

            conn.execute(u"""
            insert into representatives(user_id, first_name, last_name, birthday, photo, shelter_id)
            values({user_id}, '{first_name}', '{last_name}', '{birthday}', '{photo}', '{shelter_id}')
            on duplicate key update first_name='{first_name}', last_name='{last_name}', birthday='{birthday}', photo='{photo}', shelter_id='{shelter_id}';
                """.format(**data))
            self.write(json.dumps({'result': 'ok'}))
        except Exception, e:
            logging.warn('cannot insert data: ' + str(e))
            self.write(json.dumps({'result': 'fail'}))
