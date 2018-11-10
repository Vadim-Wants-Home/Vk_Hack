import json

from tornado.web import RequestHandler

import db_utils


class TasksRequestHandler(RequestHandler):
    def get(self, owner=None, id=None):
        self.post(owner, id)

    def post(self, owner=None, id=None):
        where_statement = ""
        if owner == "users":
            where_statement += " where t.user_id = {}".format(id)
        elif owner == 'shelters':
            where_statement += " where t.shelter_id = {}".format(id)
        elif owner == 'representatives':
            where_statement += " where t.creator_id = {}".format(id)

        conn = db_utils.get_connection()
        rows = conn.query(
            """
                select 
                    t.id, 
                    t.name,
                    t.deadline, 
                    t.type, 
                    t.description,
                    
                    r.user_id as r_user_id,
                    r.first_name as r_first_name,
                    r.last_name as r_last_name,
                    r.birthday as r_birthday,
                    r.photo as r_photo,
                    
                    s.id as s_id,
                    s.name as s_name,
                    s.address as s_address,
                    s.photo as s_photo,
                    s.site as s_site
                from tasks as t
                join representatives as r on r.user_id = t.creator_id
                join shelters as s on s.id = t.shelter_id;
                {0}
            """.format(where_statement)
        )

        response_data = []
        for row in rows:
            response_data.append({
                'id': row.id,
                'name': row.name,
                'deadline': row.deadline.strftime("%s"),
                'type': row.type,
                'description': row.description,

                'representative': {
                    'user_id': row.r_user_id,
                    'first_name': row.r_first_name,
                    'last_name': row.r_last_name,
                    'birthday': row.r_birthday.strftime("%d/%m/%y"),
                    'photo': row.r_photo
                },

                'shelter': {
                    'id': row.s_id,
                    'name': row.s_name,
                    'address': row.s_address,
                    'photo': row.s_photo,
                    'site': row.s_site
                }
            })

        self.finish({
            'result': 'ok',
            'data': json.dumps(response_data)
        })