import sys

import MySQLdb

class SqlWorker:
    def connect(self, args):
        self.db = MySQLdb.connect(host=args[0], user=args[1], passwd=args[2], db=args[3])
        return self

    def get_connection(self):
        return self.db

    def install(self):
        self.db.query(
            """
            create table if not exists users (
                user_id int unique ,
                first_name varchar(255),
                last_name varchar(255),
                birthday date,
                photo varchar(255),
                primary key (user_id)
            );
            """
        )

        self.db.query("""
            CREATE TABLE if not exists shelters (
                id int auto_increment,
                name varchar(255),
                address varchar(255),
                photo varchar(255),
                site varchar(255),
                primary key (id)
            ); 
        """)

        self.db.query(
            """
            create table if not exists representatives (
                user_id int unique,
                first_name varchar(255),
                last_name varchar(255),
                birthday date,
                photo varchar(255),
                shelter_id int,
                primary key (user_id),
                foreign key (shelter_id) references shelters(id)
            );
            """
        )

        self.db.query(
            """CREATE TABLE if not exists tasks (
            id int auto_increment,
            name varchar(255),
            deadline timestamp,
            type int, 
            description varchar(255),
            user_id int,
            creator_id int,
            shelter_id int,
            primary key(id),
            foreign key (user_id) references users(user_id),
            foreign key (creator_id) references representatives(user_id),
            foreign key (shelter_id) references shelters(id)
            );"""
        )



    def uninstall(self):
        self.db.query("drop table if exists tasks")
        self.db.query("drop table if exists representatives")
        self.db.query("drop table if exists shelters")
        self.db.query("drop table if exists users")

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
            "1, "
            "'slava', "
            "'vushev', "
            "'20000505', "
            "'user1.jpg'"
            ")"
        )

        self.db.cursor().execute(
            """
            insert into shelters (name, address, photo, site) VALUES 
            ('Yow', 'Saint Petersubtg 46, 2342/34', 'brokenlink', 'brokensitelink');
            """
        )

        self.db.commit()

        self.db.cursor().execute(
            """
            insert into representatives (user_id, first_name, last_name, birthday, photo, shelter_id) VALUES 
            (1, 'name', 'surname', '02948435', 'photka.png', 1)
            """
        )

        self.db.commit()

        self.db.cursor().execute(
            """
            insert into tasks (name, deadline, type, description, user_id, creator_id, shelter_id) VALUES 
            ('Yow Task First', 
            current_timestamp, 
            0, 
            'very very very very very very long desc desc desc desc of this task',
            1,
            1,
            1);
            """
        )

        self.db.cursor().execute(
            """
            insert into tasks (name, deadline, type, description, user_id, creator_id, shelter_id) VALUES 
            ('Yow Second Task', 
            current_timestamp, 
            0, 
            'very very very very very very long desc desc desc desc of this task again',
            1,
            1,
            1);
            """
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
    db = SqlWorker().connect(sys.argv[1:])
    # db.uninstall()
    # db.install()
    # db.sample_data_insert()
    db.sample_queries()
