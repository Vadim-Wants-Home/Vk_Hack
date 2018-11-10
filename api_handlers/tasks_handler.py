import json

from tornado.web import RequestHandler
from sql_scripts.sql_worker import SqlDatasetWorker

import db_utils


class TasksRequestHandler(RequestHandler):

    def get(self):
        self.post()

    def post(self):
        query = """
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
            """

        rows = SqlDatasetWorker().select_query(query)

        response_data = []
        for row in rows:
            print(row)
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