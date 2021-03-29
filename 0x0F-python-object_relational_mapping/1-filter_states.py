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

c.execute("SELECT * FROM states ORDER BY states.id ASC")
fields = c.fetchall()

for field in fields:
    if field[1].startswith("N"):
        print(field)

c.close()
serv.close()
