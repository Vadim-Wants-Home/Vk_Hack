# -*- coding: utf-8 -*-

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

        conn.execute(
            """
            create table if not exists representative_codes (
            id int auto_increment,
            shelter_id int,
            code int,
            primary key (id),
            foreign key (shelter_id) references shelters(id)
            )
            """
        )

    @staticmethod
    def uninstall():
        conn = db_utils.get_connection()
        conn.execute("drop table if exists representative_codes")
        conn.execute("drop table if exists tasks")
        conn.execute("drop table if exists representatives")
        conn.execute("drop table if exists users")
        conn.execute("drop table if exists shelters")

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
            "insert into users("
            "user_id, "
            "first_name, "
            "last_name, "
            "birthday, "
            "photo"
            ") "
            "values("
            "181274867, "
            "'vasilisa', "
            "'lalal', "
            "'19900519', "
            "'user1.jpg'"
            ")"
        )

        conn.execute(
            "insert into users("
            "user_id, "
            "first_name, "
            "last_name, "
            "birthday, "
            "photo"
            ") "
            "values("
            "188438066, "
            "'vasilisa', "
            "'lalal', "
            "'19900519', "
            "'user1.jpg'"
            ")"
        )

        conn.execute(
            """
            insert into shelters (name, address, photo, site) VALUES 
            ('Гнездо', 'Дворцовая, 2', 'http://img.happy-giraffe.ru/v2/thumbs/e26e4ffdce15f4bc6711c767ffa68dac/69/03/e9ddc9480710e0d0eed71e0397bd.jpg', 'http://gnezdo.com');
            """
        )

        conn.execute("""
                    insert into shelters(name, address, photo, site)
                    VALUES
                    ('Надежда', 'Ботаническая, 66', 'https://www.w3schools.com/w3css/img_lights.jpg', 'nadezda.ru');
                """
                     )

        conn.execute(
            """
            insert into shelters (name, address, photo, site) VALUES 
            ('Солнышко', 'Гороховая, 5', 'https://cdn.fishki.net/upload/post/2017/03/19/2245758/tn/02-funny-cat-wallpapercat-wallpaper.jpg', 'http://priut_solnishko.com');
            """
        )

        conn.execute(
            """
            insert into shelters (name, address, photo, site) VALUES 
            ('Милый кот', 'Садовая, 12', 'https://humoraf.ru/wp-content/uploads/2017/08/23-14.jpg', 'mily_cat.ru');
            """
        )

        conn.execute(
            """
            insert into shelters (name, address, photo, site) VALUES 
            ('Дивный мир', 'Макарова, 130', 'http://bm.img.com.ua/img/prikol/images/large/0/0/307600.jpg', 'divny_world.ru');
            """
        )

        conn.execute(
            """
            insert into shelters (name, address, photo, site) VALUES 
            ('Уютный дом', 'Грибоедова, 15', 'https://bipbap.ru/wp-content/uploads/2017/10/0_8eb56_842bba74_XL-640x400.jpg', 'uyut.ru');
            """
        )


        conn.execute(
            """
            insert into representatives (user_id, first_name, last_name, birthday, photo, shelter_id) VALUES 
            (3, 'Bill', 'Gates', '2018-09-09', 'http://www.sncmedia.ru/upload/iblock/1bd/1bd85c62deedf241663b309d3790be17_w877_h500_crp.jpg', 1)
            """
        )

        conn.execute(
            """
            insert into representatives (user_id, first_name, last_name, birthday, photo, shelter_id) VALUES 
            (4, 'John', 'Doe', '2018-09-08', 'http://droplak.ru/wp-content/uploads/2016/04/3-8.jpg', 2)
            """
        )

        conn.execute(
            """
            insert into representatives (user_id, first_name, last_name, birthday, photo, shelter_id) VALUES 
            (1, 'Кот', 'Барсик', '2018-09-09', 'https://rozetked.me/images/uploads/dwoilp3BVjlE.jpg', 1)
            """
        )

        conn.execute(
            """
            insert into representatives (user_id, first_name, last_name, birthday, photo, shelter_id) VALUES 
            (2, 'Кошка', 'Муся', '2019-09-09', 'https://i.ytimg.com/vi/M-XtB0R3ri4/maxresdefault.jpg', 1)
            """
        )

        conn.execute(
            """
            insert into representatives (user_id, first_name, last_name, birthday, photo, shelter_id) VALUES 
            (5, 'Эдуард', 'Ерохин', '2019-09-09', 'https://i.ytimg.com/vi/M-XtB0R3ri4/maxresdefault.jpg', 4)
            """
        )

        conn.execute(
            """
            insert into representatives (user_id, first_name, last_name, birthday, photo, shelter_id) VALUES 
            (6, 'Мунира', 'Турсунова', '2019-09-09', 'https://i.ytimg.com/vi/M-XtB0R3ri4/maxresdefault.jpg', 3)
            """
        )

        conn.execute(
            """
            insert into representatives (user_id, first_name, last_name, birthday, photo, shelter_id) VALUES 
            (7, 'Игорь', 'Овсянов', '2019-09-09', 'https://i.ytimg.com/vi/M-XtB0R3ri4/maxresdefault.jpg', 3)
            """
        )

        conn.execute(
            """
            insert into representatives (user_id, first_name, last_name, birthday, photo, shelter_id) VALUES 
            (8, 'Руслан', 'Орехов', '2019-09-09', 'https://i.ytimg.com/vi/M-XtB0R3ri4/maxresdefault.jpg', 4)
            """
        )

        conn.execute(
            """
            insert into representatives (user_id, first_name, last_name, birthday, photo, shelter_id) VALUES 
            (9, 'Дуся', 'Котова', '2019-09-09', 'https://i.ytimg.com/vi/M-XtB0R3ri4/maxresdefault.jpg', 5)
            """
        )

        conn.execute(
            """
            insert into representatives (user_id, first_name, last_name, birthday, photo, shelter_id) VALUES 
            (10, 'Муся', 'Кошка', '2019-09-09', 'https://i.ytimg.com/vi/M-XtB0R3ri4/maxresdefault.jpg', 6)
            """
        )

        conn.execute(
            """
            insert into tasks (name, deadline, type, description, user_id, creator_id, shelter_id, done_key) VALUES 
            ('Помыть кошку Мусю', 
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
            ('Купить медикаменты песику Бобику', 
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
            ('Покормить котика Васю', 
            current_timestamp, 
            0, 
            'very very very very very very long desc desc desc desc of this task',
            188438066,
            1,
            1,
            45678765);
            """
        )

        conn.execute(
            """
            insert into tasks (name, deadline, type, description, user_id, creator_id, shelter_id, done_key) VALUES 
            ('Выгулять пса Шарика', 
            current_timestamp, 
            0, 
            'very very very very very very long desc desc desc desc of this task',
            188438066,
            1,
            1,
            45678765);
            """
        )

        conn.execute(
            """
            insert into tasks (name, deadline, type, description, user_id, creator_id, shelter_id, done_key) VALUES 
            ('Сделать домик для кошки Маши', 
            current_timestamp, 
            0, 
            'very very very very very very long desc desc desc desc of this task again',
            181274867,
            1,
            2,
            765876894);
            """
        )

        conn.execute(
            """
            insert into tasks (name, deadline, type, description, user_id, creator_id, shelter_id, done_key) VALUES 
            ('Перевязать лапку белочке', 
            current_timestamp, 
            0, 
            'very very very very very very long desc desc desc desc of this task again',
            181274867,
            1,
            2,
            555555);
            """
        )

        conn.execute("""
        insert into tasks (name, deadline, type, description, user_id, creator_id, shelter_id, done_key) VALUES
            ('Third',
            current_timestamp,
            0,
            'very very very very very very long desc desc desc desc of this task',
            181274867,
            1,
            3,
            68265443);
        """)

        conn.execute("""
        insert into representative_codes(shelter_id, code) values (1, 111111)
        """)

        conn.execute("""
        insert into representative_codes(shelter_id, code) values (2, 111112)
        """)

        conn.execute("""
                insert into representative_codes(shelter_id, code) values (3, 111113)
        """)

        conn.execute("""
                insert into representative_codes(shelter_id, code) values (4, 111114)
                """)

        conn.execute("""
                insert into representative_codes(shelter_id, code) values (5, 111115)
                """)


        conn.execute("""
                insert into representative_codes(shelter_id, code) values (6, 111116)
                """)