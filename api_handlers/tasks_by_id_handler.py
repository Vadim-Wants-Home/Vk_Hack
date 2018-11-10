from tornado.web import RequestHandler
from sql_scripts.sql_worker import SqlDatasetWorker
import json

class TasksByIdDHandler(RequestHandler):
    def get(self, owner, id):
        self.post(owner, id)

    def post(self, owner, id):
        where_statement = ""
        if owner == "users":
            where_statement += " where tasks.user_id = {}".format(id)
        elif owner == 'shelters':
            where_statement += " where tasks.shelter_id = {}".format(id)
        elif owner == 'representatives':
            where_statement += " where tasks.creator_id = {}".format(id)
        else:
            self.finish({
                'result': 'fail',
                'error': 'wrong user type'
            })
            return

        query = """
                            select 
                                tasks.id, 
                                tasks.name,
                                tasks.deadline, 
                                tasks.type, 
                                tasks.description
                            from tasks
                            {0}
                        """.format(where_statement)

        rows = SqlDatasetWorker().select_query(query)
        for row in rows:
            print(row)
            row['deadline'] = row['deadline'].strftime("%d/%m/%y")
        self.finish({
            'result': 'ok',
            'data': json.dumps(rows)
        })