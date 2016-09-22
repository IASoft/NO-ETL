
import pymysql
import no_etl

class ETL:

    defOrigin = {}
    defDestination = {}

    driverOrigin = {}
    driverDestination = {}


    def __init__(self, origin, destination):
        self.defOrigin = origin
        self.defDestination = destination

        if origin['type'] == 'MySQL':
            from no_etl.drivers.MySQL import Driver
            conn = pymysql.connect(host=origin['parms']['host'], port=origin['parms']['port'], user=origin['parms']['user'], passwd=origin['parms']['passwd'], db=origin['parms']['db'])
            self.driverOrigin = Driver(conn)
        elif origin['type'] == 'MongoDB':
            import pymongo
            from no_etl.drivers.MongoDB import Driver
            conn = pymongo.MongoClient(host=destination['parms']['host'],port=destination['parms']['port'])
            self.driverDestination = Driver(conn)

    def dumpOrigin(self):
        self.driverOrigin.start()
        print "ok"

