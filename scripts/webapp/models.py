import sqlite3

conn = sqlite3.connect('rest_server.db')


class Participant:
    def __init__(self):
        try:
            conn.execute('''CREATE TABLE WORKSHOP
                        (ID INT PRIMARY KEY     NOT NULL,
                         NAME           TEXT    NOT NULL,
                         AGE            INT     NOT NULL,
                         CITY           CHAR(50));''')
        except Exception as e:
            print('Table creation error')

    def creat_participant(self, name, age, city):
        last_id = conn.execute("SELECT MAX(id) from WORKSHOP").fetchone()[0]
        last_id = 0 if last_id is None else last_id
        conn.execute("INSERT INTO WORKSHOP (ID,NAME,AGE,CITY)"
                      "VALUES ({}, '{}', {}, '{}')".format(last_id + 1, name, age, city))

        conn.commit()

    def list_participants(self):

        participants = []
        cursor = conn.execute("SELECT id, name, city from WORKSHOP")
        for row in cursor:
            participants.append({"id": row[0],
                                 "name": row[1],
                                 "city": row[2]})
        return participants
