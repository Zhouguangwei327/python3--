from redis import StrictRedis

class Redis(object):
    def __init__(self) -> None:
        self.redis = StrictRedis(host='localhost', port=6379, db=0, password=None)

    
    def test(self):
        # self.redis.set('name', 'Bob')
        print(self.redis.get('name'))
        self.redis


rds = Redis()
if __name__ == '__main__':
    rds.test()