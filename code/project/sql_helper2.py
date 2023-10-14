from dbutils.pooled_db import PooledDB
import pymysql


class SqlHelper(object):
    def __init__(self):
        self.pool = PooledDB(
            creator=pymysql,
            maxconnections=6,  # 0 no limit
            mincached=2,  # pre init conn, 0=no
            blocking=True,  # when conn full, wait or no
            host='127.0.0.1',
            port=3306,
            user='test',
            password='1o3g; 284',
            database='test',
            charset='utf8'
        )

    def open(self):
        conn = self.pool.connection()  # get conn
        cursor = conn.cursor()

        return conn, cursor

    def close(self, cursor, conn):
        cursor.close()
        conn.close()  # release conn

    def fetchall(self, sql, *args):
        conn, cursor = self.open()
        cursor.execute(sql, args)
        result = cursor.fetchall()
        self.close(cursor, conn)

        return result

    def fetchone(self, sql, *args):
        conn, cursor = self.open()
        cursor.execute(sql, args)
        result = cursor.fetchone()
        self.close(cursor, conn)

        return result

    def insert(self, sql, *args):
        conn, cursor = self.open()
        cursor.execute(sql, args)
        conn.commit()
        self.close(cursor, conn)


db = SqlHelper()

User = db.fetchone('select * from user where user=%s', 'a')
Users = db.fetchall('select * from user')
