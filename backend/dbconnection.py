import mysql.connector

class DBConnect:
    def __init__(self):
        self.con=mysql.connector.connect(host="localhost", user="root", password="Current@3463", database="assignment")
        self.cur=self.con.cursor()

    def insert(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()

    def select(self, query, values):
        self.cur.execute(query, values)
        rows = self.cur.fetchall()
        return rows


class DBConnect_AddBook:
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", user="root", password="Current@3463",
                                           database="")
        self.cur = self.con.cursor()

    def insert(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()

    def select(self, query, values):
        self.cur.execute(query, values)
        rows = self.cur.fetchall()
        return rows
