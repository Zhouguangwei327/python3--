from elasticsearch import Elasticsearch

class Elasticsearch(object):
    def __init__(self) -> None:
        self.es = Elasticsearch()
    
    def search(self):
        result = self.es.indices.create(index='news', ignore=400)
        print(result)


es = Elasticsearch()


if __name__ == '__main__':
    es.search()