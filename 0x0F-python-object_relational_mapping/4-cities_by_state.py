#!/usr/bin/python3
""" Displays all values in the states table of hbtn_0e_0_usa filtered by name"""


if __name__ == '__main__':

    import MySQLdb
    from sys import argv

serv = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

c = serv.cursor()

c.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
fields = c.fetchall()

for field in fields:
    print(field)

c.close()
serv.close()