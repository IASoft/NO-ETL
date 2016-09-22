
import sys

#libFolder = "../lib/no_etl/no_etl"
sys.path.insert(0, "../lib/no_etl")

#import MySQLdb



from no_etl.ETL import ETL

#from pymysql.connections import Connection
import pymysql


# import no_etl.ETL

parmsOrigin = {
    'type' : 'MySQL',
    'parms' : {
        'host':'localhost', 'port':3306, 'user':'root', 'passwd':'', 'db':'test'
    }
}


parmsDestination = {
    'type' : 'MongoDB',
    'parms' : {
        'host':'localhost', 'port':27080, 'db':'new_test'
    }
}


etl = ETL(parmsOrigin, parmsDestination)

etl.dumpOrigin()

print etl.driverOrigin.listEntities

#con = Connection("mysql://root@localhost")
'''
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='test')

cur = conn.cursor()

sql = "SELECT * FROM scb_saldos_centro_custo limit 1"
sql = "SHOW TABLES"

cur.execute(sql)

#print cur.description



for row in cur:
    print(row)

cur.close()
conn.close()
'''
