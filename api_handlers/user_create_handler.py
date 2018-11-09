from tornado.web import RequestHandler
import json


class UserCreateHandler(RequestHandler):
    def get(self):
        self.post()

    def post(self):
        data = self.request.body
        print(data['user_id'])
        query = """
        insert into users(
            user_id, 
            first_name, 
            last_name, 
            birthday, 
            photo
            ) 
            values(
            2, 
            'slava', 
            'vushev', 
            '20000505', 
            'user1.jpg'
            );
            """
        print(query)
        self.write(self.request.body)
        #self.write(json.dumps({'result': 'ok'}))

