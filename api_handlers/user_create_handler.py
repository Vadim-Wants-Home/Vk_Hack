from tornado.web import RequestHandler
import json


class UserCreateHandler(RequestHandler):
    def get(self):
        self.post()

    def post(self):
        self.write(json.dumps({'result': 'ok'}))