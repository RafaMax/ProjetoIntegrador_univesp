from peewee import MySQLDatabase

#db = MySQLDatabase('univesp_pi.db')
db = MySQLDatabase(
    'univesp_db',
    user='root',
    password='GCruUsgoPnknKFPZLewtKKWftSVPNYtD',
    host='interchange.proxy.rlwy.net',
    port=45565 
)