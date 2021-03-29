#!/usr/bin/python3
""" Sorts cities by state in a database """


if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    serv = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    c = serv.cursor()
    clean = []
    arg = argv[4]

    c.execute(
        "SELECT cities.name FROM cities JOIN states ON cities.state_id =\
        states.id WHERE states.name = %s ORDER BY states.id ASC;", (arg,))

    fields = c.fetchall()

    for field in fields:
        clean += field
    print(', '.join(clean))

    c.close()
    serv.close()
