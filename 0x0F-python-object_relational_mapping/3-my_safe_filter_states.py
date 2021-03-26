#!/usr/bin/python3
""" Displays all values in the states table of hbtn_0e_0_usa filtered by name"""


if __name__ == '__main__':

    import MySQLdb
    from sys import argv

serv = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

c = serv.cursor()
arg = argv[4]


c.execute("SELECT * FROM states WHERE states.name = %s ORDER BY states.id;", (arg,))
fields = c.fetchall()

for field in fields:
    print(field)

c.close()
serv.close()
