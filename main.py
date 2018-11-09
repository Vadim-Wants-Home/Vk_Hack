import tornado.ioloop
import tornado.web
import sys
from sql_scripts.sql_worker import SqlWorker
from api_handlers.user_create_handler import UserCreateHandler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/api/users/create", UserCreateHandler, dict(db=db)),
    ])

if __name__ == "__main__":
    print(sys.argv)
    db = SqlWorker().connect(sys.argv[1:])
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()