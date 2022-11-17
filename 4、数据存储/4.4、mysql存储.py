import pymysql


class Mysql(object):
    def __init__(self):
        self.table = 'student'
        self.data = {
            'id': '10003',
            'name': '王二',
            'age': 50
        }
        self.db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, database='spiders')
        self.cursor = self.db.cursor()

    # 创建库
    def createDatabaseSpiders(self):
        self.cursor.execute("SELECT VERSION()")
        data = self.cursor.fetchone()
        print('Database version: {}'.format(data))
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS spiders DEFAULT CHARACTER SET utf8mb4")

    # 创建表
    def createTableStudents(self):
        sql = r'CREATE TABLE IF NOT EXISTS student(id VARCHAR(255) NOT NULL, name VARCHAR(255), age INT, PRIMARY KEY(' \
              r'id)) '
        self.cursor.execute(sql)

    # 插入数据
    def insertData(self):
        keys = ','.join(self.data.keys())
        values = ','.join(['%s'] * len(self.data))
        print(keys, values)
        sql = f'INSERT INTO {self.table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '
        update = ','.join(["{} = %s".format(key) for key in self.data])
        sql += update
        try:
            self.cursor.execute(sql, tuple(self.data.values())*2)
            print('Successful')
            self.db.commit()
        except Exception as e:
            print('Failed')
            print(e)
            self.db.rollback()

    # 更新数据
    def updateData(self):
        sql = 'UPDATE student SET age = %s WHERE name = %s'
        try:
            self.cursor.execute(sql, (30, '张三'))
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
    
    # 删除数据
    def deleteData(self):
        condition = 'age > 10'
        sql = f'DELETE FROM {self.table} WHERE {condition}'
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
    
    # 查询数据
    def queryData(self):
        sql = f'SELECT * FROM {self.table}'
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for result in results:
                print(result)
            self.db.commit()
        except Exception as e:
            self.db.rollback()

    # 关闭Mysql
    def closeMysql(self):
        self.db.close()


ms = Mysql()
if __name__ == '__main__':
    # ms.createDatabaseSpiders()
    # ms.createTableStudents()
    # ms.insertData()
    # ms.updateData()
    # ms.deleteData()
    ms.queryData()
    ms.closeMysql()

