from tornado.web import RequestHandler
import json

#
# class UserCreateHandler(RequestHandler):
#     def initialize(self):
#
#     def get(self):
#         self.post()
#
#     def post(self):
#         conn =
#
#         data = json.loads(self.request.body)
#         query = """
#         insert into users(user_id, first_name, last_name, birthday, photo)
#         values({user_id}, '{first_name}', '{last_name}', '{birthday}', '{photo}');
#             """\
#             .format(**data)
#         try:
#             self.db.insert_query(query)
#             self.write(json.dumps({'result': 'ok'}))
#         except:
#             self.write(json.dumps({'result': 'fail'}))
