import pymongo
from bson.objectid import ObjectId


class Mongodb(object):
    def __init__(self) -> None:
        pass

        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.client.test
        self.collection = self.db.student

    # 插入数据
    def _insertData(self):
        student = {
            'id': '10001',
            'name': '王二',
            'age': 20,
            'gender': 'male'
        }
        result = self.collection.insert_one(student)
        print(result)
        print(result.inserted_id)

        student1 = {
            'id': '10002',
            'name': '张三',
            'age': 10,
            'gender': 'male'
        }
        student2 = {
            'id': '10003',
            'name': '李四',
            'age': 20,
            'gender': 'male'
        }

        results = self.collection.insert_many([student1, student2])
        print(results)
        print(results.inserted_ids)

    # 查询数据
    def queryData(self):
        result = self.collection.find_one({'name': '张三'})
        print(result)

        result = self.collection.find_one({'_id': ObjectId('634d6db59acec978b631f1fb')})
        print(result)

        results = self.collection.find({'age': 20})
        for result in results:
            print(result)

    # 计数
    def countData(self):
        count = self.collection.count_documents({'age': 20})

        print(count)

    # 排序
    def sortData(self):
        results = self.collection.find().sort('name', pymongo.DESCENDING).skip(2).limit(2)
        print([result['name'] for result in results])

    # 更新
    def updateData(self):
        # condition = {'name': '王二'}
        condition = {'age': {'$gt': 20}}
        # student = self.collection.find_one(condition)
        # student['age'] = 25
        result = self.collection.update_many(condition, {'$inc': {'age': 1}})
        print(result)
        print(result.matched_count, result.modified_count)

    # 删除
    def deleteData(self):
        result = self.collection.delete_one({'name': '王二'})
        print(result)
        result = self.collection.delete_many({'age': {'$gt': 25}})
        print(result.deleted_count)


mg = Mongodb()
if __name__ == '__main__':
    # mg._insertData()
    # mg.queryData()
    # mg.countData()
    # mg.sortData()
    # mg.updateData()
    mg.deleteData()