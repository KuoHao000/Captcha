from dbutils.pooled_db import PooledDB
import pymysql

pool = PooledDB(
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


def fetchall(sql, *args):
    conn = pool.connection()  # get conn
    cursor = conn.cursor()
    cursor.execute(sql, args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()  # release conn

    return result


def fetchone(sql, *args):
    conn = pool.connection()  # get conn
    cursor = conn.cursor()
    cursor.execute(sql, args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()  # release conn

    return result
