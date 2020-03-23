from pymongo import MongoClient

class DB:

    def __init__(self, database_name, collection):
        self.client = MongoClient('localhost', 27017)
        self.database_name = database_name
        self.collection = collection

    def find(self, tconst):
        return self.client[self.database_name][self.collection].find_one({'tconst': tconst})

    def filt(self, filter) :
        return self.client[self.database_name][self.collection].find(filter = filter)

    def find_all(self):
        return self.client[self.database_name][self.collection].find()

    def insert(self, data):
        self.client[self.database_name][self.collection].insert_one(data)

    def bulk_insert(self, datas):
        self.client[self.database_name][self.collection].insert_many(datas)

    def update(self, datas):
        self.client[self.database_name][self.collection].update_many(datas)