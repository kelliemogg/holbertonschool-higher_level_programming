#!/usr/bin/python3
""" This module imports MySQLdb and returns a sorted list of states by id """

    import MySQLdb
    from sys import argv

if __name__ == '__main__':

serv = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                       passwd=argv[2], db=argv[3])

c = serv.cursor()

c.execute("SELECT * FROM states ORDER BY states.id ASC")
fields = c.fetchall()
for field in fields:
    print(field)

# close all cursors
serv.close()
# close db
c.close()
