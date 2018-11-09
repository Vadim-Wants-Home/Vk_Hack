from tornado.web import RequestHandler
import json


class UserCreateHandler(RequestHandler):
    def initialize(self, db):
        self.db = db

    def get(self):
        self.post()

    def post(self):
        data = json.loads(self.request.body)
        query = "select * from users where user_id={'user_id'}"
        print(query)
        self.db.insert_query(query)
        self.write(json.dumps({'result': 'ok'}))

