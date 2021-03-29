#!/usr/bin/python3
""" This module imports filterd objects from a database """

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

serv = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=argv[1],
    passwd=argv[2],
    db=argv[3])

""" this is to connect """

c = serv.cursor()
arg = argv[4]

c.execute(
    "SELECT * FROM states WHERE states.name LIKE '{}' ORDER BY states.id"
    .format(arg))
fields = c.fetchall()

for field in fields:
    print(field)

c.close()
serv.close()
