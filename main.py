import tornado.ioloop
import tornado.web
import torndb
import sys

from api_handlers.shelters_handler import SheltersRequestHandler
from api_handlers.user_create_handler import UserCreateHandler
from api_handlers.users_handler import UsersRequestHandler
from sql_scripts.sql_worker import SqlDatasetWorker
from json_working.json_working import get_json_data
# from api_handlers.user_create_handler import UserCreateHandler
from api_handlers.tasks_handler import TasksRequestHandler
from api_handlers.representatives_create_handler import RepresentativesCreateHandler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/api/users/create", UserCreateHandler),
        (r'/api/tasks', TasksRequestHandler),
        (r'/api/(?P<owner>[^/]+)/(?P<id>[^/]+)/tasks', TasksRequestHandler),
        (r'/api/shelters', SheltersRequestHandler),
        (r'/api/shelters/(?P<id>[^/]+)', SheltersRequestHandler),
        (r'/api/users', UsersRequestHandler),
        (r'/api/users/(?P<id>[^/]+)', UsersRequestHandler),
        (r'/api/representatives/create', RepresentativesCreateHandler)
    ])


if __name__ == "__main__":
    SqlDatasetWorker.uninstall()
    SqlDatasetWorker.install()
    SqlDatasetWorker.sample_data_insert()
    #
    # db.uninstall()
    # db.install()
    # db.sample_data_insert()

    app = make_app()
    app.listen(get_json_data('server.json')['port'])
    tornado.ioloop.IOLoop.current().start()