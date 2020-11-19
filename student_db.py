import pymysql
from read_config import read_config

class student_db(object):
    def connect_mysql(self):
        '''

        :return:
        '''
        config = {
            # 'host': '192.168.109.34',
            'host': read_config().get_option_of_section('db','host'),
            'port': 3306,
            'user': read_config().get_option_of_section('db', 'user'),
            'password': read_config().get_option_of_section('db', 'password'),
            'db': read_config().get_option_of_section('db', 'db_name'),
            'charset': 'utf8'
        }

        print(config)

        db = pymysql.connect(**config)
        cursor = db.cursor()  # cursor() 方法获取操作游标
        cursor.execute(self.sql_string())  # 执行SQL语句
        results = cursor.fetchall()  # 获取所有记录列表

        db.commit()  # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        # 除了查询其他操作都需要保存执行
        cursor.close()
        db.close()  # 关闭数据库连接
        return results

    def sql_string(self):
        sql = "SELECT * FROM class_15"
        return sql