import json

from tornado.web import RequestHandler

import db_utils


class SheltersRequestHandler(RequestHandler):
    def get(self, id=None):
        self.post(id)

    def post(self, id=None):
        where_statement = ""
        if id:
            where_statement += " where s.id = {}".format(id)

        conn = db_utils.get_connection()
        rows = conn.query(
            """
                select 
                    s.id, 
                    s.name,
                    s.address, 
                    s.photo, 
                    s.site

                from shelters as s
                {0};
            """.format(where_statement)
        )

        self.finish({
            'result': 'ok',
            'data': json.dumps(rows)
        })