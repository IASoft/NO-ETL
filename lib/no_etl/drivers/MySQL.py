
import pymysql


class Driver:

    #
    conn = False
    listEntities = []

    def __init__(self,conn):
        self.conn = conn

    def getEntityListNames(self):

        if False:
            self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='test')

        cur = self.conn.cursor()
        sql = "SHOW TABLES"
        cur.execute(sql)

        for reg in cur:
            self.listEntities.append(reg[0])


    def start(self):
        self.getEntityListNames()
