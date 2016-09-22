import pymongo


class Driver:


    #
    conn = False
    listEntities = []


    def __init__(self,conn):
        self.conn = conn


    def getEntityListNames(self):
        if False:
            self.conn = pymongo.MongoClient(host='localhost', port=27080,db='local')

        cur = self.conn
        sql = "SHOW TABLES"
        cur.execute(sql)

        for reg in cur:
            self.listEntities.append(reg[0])


    def start(self):
        self.getEntityListNames()
