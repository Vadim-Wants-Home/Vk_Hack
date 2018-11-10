import sys

import MySQLdb

import db_utils


class SqlDatasetWorker:
    def __init__(self):
        pass

    @staticmethod
    def install():
        conn = db_utils.get_connection()

        conn.execute(
            """
            create table if not exists users (
                user_id int unique ,
                first_name varchar(255),
                last_name varchar(255),
                birthday date,
                photo varchar(255),
                bio varchar(2000),
                primary key (user_id)
            );
            """
        )

        conn.execute("""
            CREATE TABLE if not exists shelters (
                id int auto_increment,
                name varchar(255),
                address varchar(255),
                photo varchar(255),
                site varchar(255),
                primary key (id)
            ); 
        """)

        conn.execute(
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

        conn.execute(
            """CREATE TABLE if not exists tasks (
            id int auto_increment,
            name varchar(255),
            deadline timestamp,
            type int, 
            description varchar(255),
            user_id int,
            creator_id int,
            shelter_id int,
            done_key int,
            primary key(id),
            foreign key (user_id) references users(user_id),
            foreign key (creator_id) references representatives(user_id),
            foreign key (shelter_id) references shelters(id)
            );"""
        )

    @staticmethod
    def uninstall():
        conn = db_utils.get_connection()
        conn.execute("drop table if exists tasks")
        conn.execute("drop table if exists representatives")
        conn.execute("drop table if exists shelters")
        conn.execute("drop table if exists users")

    @staticmethod
    def sample_data_insert():
        conn = db_utils.get_connection()

        conn.execute(
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

        conn.execute(
            """
            insert into shelters (name, address, photo, site) VALUES 
            ('Yow', 'Saint Petersubtg 46, 2342/34', 'http://img.happy-giraffe.ru/v2/thumbs/e26e4ffdce15f4bc6711c767ffa68dac/69/03/e9ddc9480710e0d0eed71e0397bd.jpg', 'http://example.com');
            """
        )

        conn.execute(
            """
            insert into representatives (user_id, first_name, last_name, birthday, photo, shelter_id) VALUES 
            (1, 'name', 'surname', '2018-09-09', 'photka.png', 1)
            """
        )

        conn.execute(
            """
            insert into tasks (name, deadline, type, description, user_id, creator_id, shelter_id, done_key) VALUES 
            ('Yow Task First', 
            current_timestamp, 
            0, 
            'very very very very very very long desc desc desc desc of this task',
            1,
            1,
            1,
            45678765);
            """
        )

        conn.execute(
            """
            insert into tasks (name, deadline, type, description, user_id, creator_id, shelter_id, done_key) VALUES 
            ('Yow Second Task', 
            current_timestamp, 
            0, 
            'very very very very very very long desc desc desc desc of this task again',
            1,
            1,
            1,
            765876894);
            """
        )


        conn.execute("""
            insert
            into
            shelters(name, address, photo, site)
            VALUES
            ('Hello', 'Peterhof 64 corp2, 2342/34', 'https://www.w3schools.com/w3css/img_lights.jpg', 'asdf.ru');
        """
        )

        conn.execute("""
        insert into tasks (name, deadline, type, description, user_id, creator_id, shelter_id, done_key) VALUES
            ('Third',
            current_timestamp,
            0,
            'very very very very very very long desc desc desc desc of this task',
            1,
            1,
            2,
            68265443);
        """)
