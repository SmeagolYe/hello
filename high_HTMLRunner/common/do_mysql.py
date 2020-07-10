import pymysql
from common.read_conf import ReadConfig
from common import pro_path

class DoMysql:
    def do_mysql(self, query_sql, state = 1):
        # 1.提供登录信息，字典形式
        config = eval(ReadConfig().read_config(pro_path.conf_path, "DATABASE", "database_config"))
        # 2.连接数据库
        cnn = pymysql.connect(**config)
        # 3.游标，获取操作数据的权限
        cursor = cnn.cursor()
        # 4.利用游标去查询数据
        cursor.execute(query_sql)

        # 5.利用游标获取获取查询结果
        if state == 1:
            res = cursor.fetchone() # 返回的一条数据，数据类型是元组
        else:
            res = cursor.fetchall() # 返回的是列表，返回所有数据

        # 6.操作完毕，关闭游标
        cursor.close()
        # 7.断开数据库连接
        cnn.close()

        return res