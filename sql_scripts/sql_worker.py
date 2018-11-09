import MySQLdb


class SqlWorker:

    def connect(self, args):
        self.db = MySQLdb.connect(host=args[0], user=args[1], password=args[2], db=args[3])
        return self

    def install(self):
        self.db.query(
            "CREATE TABLE users ("
            "user_id int,"
            "first_name varchar(255),"
            "last_name varchar(255), "
            "birthday date, "
            "photo varchar(255),"
            "primary key(user_id)"
            ");"
        )

    def uninstall(self):
        self.db.query("drop table users")

    def sample_queries(self):
        cursor = self.db.cursor()
        cursor.execute("""SELECT * FROM users""")

        results = cursor.fetchall()

        for t in results:
            print(t)

    def sample_data_insert(self):
        self.db.cursor().execute(
            "insert into users("
            "user_id, "
            "first_name, "
            "last_name, "
            "birthday, "
            "photo"
            ") "
            "values("
            "2, "
            "'slava', "
            "'vushev', "
            "'20000505', "
            "'user1.jpg'"
            ")"
        )
        self.db.commit()

    def insert_query(self, query):
        self.db.cursor().execute(query)
        self.db.commit()

    def select_query(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)

        return cursor.fetchall()

if __name__ == "__main__":
    db = SqlWorker().connect()
    # db.uninstall()
    # db.install()
    # db.sample_data_insert()
    db.sample_queries()
