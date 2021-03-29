#!/usr/bin/python3
"""This module imports MySQLdb and returns a sorted list of states by id"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

serv = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                       passwd=argv[2], db=argv[3])
""" Connect to MySQLdb """

c = serv.cursor()
""" serv """

c.execute("SELECT * FROM states ORDER BY states.id ASC")
fields = c.fetchall()

for field in fields:
    print(field)

serv.close()
c.close()
