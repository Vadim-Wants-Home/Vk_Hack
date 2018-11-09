from tornado.web import RequestHandler
import json


class UserCreateHandler(RequestHandler):
    def initialize(self, db):
        self.db = db

    def get(self):
        self.post()

    def post(self):
        data = json.loads(self.request.body)
        query = """
        insert into users(
            user_id, 
            first_name, 
            last_name, 
            birthday, 
            photo
            ) 
            values(
            {0}, 
            {1}, 
            {2}, 
            {3}, 
            {4}
            );
            """.format(
            data['user_id'],
            data['first_name'],
            data['last_name'],
            data['birthday'],
            data['photo']
        )
        self.db.insert_query(query)
        #self.write(json.dumps({'result': 'ok'}))

