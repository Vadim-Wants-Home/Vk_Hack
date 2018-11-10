import tornado.ioloop
import tornado.web
import torndb
import sys

from sql_scripts.sql_worker import SqlWorker
# from api_handlers.user_create_handler import UserCreateHandler
from api_handlers.tasks_handler import TasksRequestHandler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        # (r"/api/users/create", UserCreateHandler),
        (r'/api/tasks', TasksRequestHandler),
        (r'/api/(?P<owner>[^/]+)/(?P<id>[^/]+)/tasks', TasksRequestHandler),
    ])


if __name__ == "__main__":
    #
    # db.uninstall()
    # db.install()
    # db.sample_data_insert()

    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()