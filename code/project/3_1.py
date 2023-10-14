from dbutils.pooled_db import PooledDB
import pymysql

pool = PooledDB(
    creator=pymysql,
    maxconnections=6,  # 0沒限制
    mincached=2,  # 初始化時創建的連結數，0不創建
    blocking=True,  # 連線數到上限時是否等待
    host='192.168.158.128',
    port=3306,
    user='root',
    password='1o3g; 284',
    database='project',
    charset='utf8'
)

conn = pool.connection()  # 獲取一個連接

cursor = conn.cursor()
cursor.execute('select * from user')
result = cursor.fetchall()
cursor.close()

conn.close()  # 將連接放回連接池

print(result)
