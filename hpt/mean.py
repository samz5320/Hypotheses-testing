from pymongo import MongoClient


class Mean:
    def __init__(self):
        self.client = MongoClient(
            "mongodb+srv://sanjayam:123@cluster0.icwhc.mongodb.net/test")
        self.db = self.client['mydb1']

        self.red_docs = self.db['hpt_red'].find({})
        self.blue_docs = self.db['hpt_blue'].find({})

        self.red_total = self.db['hpt_red'].count_documents(filter={})
        self.blue_total = self.db['hpt_blue'].count_documents(filter={})

        self.docs_total = self.red_total+self.blue_total
        # self.doc_total=self.red_total+self.blue_total
        
        #print(self.docs_total)
        self.red_time = 0
        self.blue_time = 0

        # self.x = self.db["hpt_red"].find({},{'_id': 0, 'id': 1,
        #          'count': 1, 'time': 1})

        # print(self.x)

        self.l = []
        self.l1 = []

        # time
        for x in self.red_docs:
            self.red_time += x['time']
            self.l.append(x['time'])

        # print(self.l)
        for y in self.blue_docs:
            self.blue_time += y['time']
            self.l1.append(y['time'])
        # print(self.l1)

        # print(self.blue_time)
        # print(self.red_time)

        # self.ind_time=[]
        # for x in (self.red_docs,self.blue_docs):
        #     print(x["time"])
        #     for i in x["time"]:
        #         self.ind_time.append(i)
        # print(self.ind_time)

        self.mean1 = (self.blue_time+self.red_time)/self.docs_total
        # print(self.mean1)
        # print(self.doc_total)
        # print(self.blue_time+self.red_time)
        # self.total_docs=int(self.red_docs)+self.blue_docs

        #print( str(total_docs))
m = Mean()
print(m)
