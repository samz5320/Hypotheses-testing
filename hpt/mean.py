from pymongo import MongoClient

class Mean:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://sanjayam:123@cluster0.icwhc.mongodb.net/test")
        self.db = self.client['mydb1']

        self.red_docs = self.db['hpt_red'].find({})
        self.blue_docs = self.db['hpt_blue'].find({})

        self.red_total = self.db['hpt_red'].count_documents(filter={})
        self.blue_total = self.db['hpt_blue'].count_documents(filter={})

        self.red_time = 0
        self.blue_time = 0

        for x in self.red_docs:
            self.red_time += x['time']

        for x in self.blue_docs:
            self.blue_time += x['time']