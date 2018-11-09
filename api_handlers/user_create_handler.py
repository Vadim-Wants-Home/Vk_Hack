from tornado.web import RequestHandler
import json


class UserCreateHandler(RequestHandler):
    def initialize(self, db):
        self.db = db

    def get(self):
        self.post()

    def post(self):
        print(self.request.body)
        data = json.loads(self.request.body)
        print(data)
        query = """
        insert into users(user_id, first_name, last_name, birthday, photo) 
        values({user_id}, '{first_name}', '{last_name}', '{birthday}', '{photo}');
            """\
            .format(**data)
        print(query)
        self.db.insert_query(query)
        self.write(json.dumps({'result': 'ok'}))

