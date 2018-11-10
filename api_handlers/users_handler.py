import json

from tornado.web import RequestHandler

import db_utils


class UsersRequestHandler(RequestHandler):
    def get(self, id=None):
        self.post(id)

    def post(self, id=None):
        where_statement = ""
        if id:
            where_statement += " where s.user_id = {}".format(id)

        conn = db_utils.get_connection()
        rows = conn.query(
            """
                select *
                from users as s
                {0};
            """.format(where_statement)
        )

        for row in rows:
            row['birthday'] = row['birthday'].strftime("%d/%m/%y")

        self.finish({
            'result': 'ok',
            'data': json.dumps(rows[0])
        })