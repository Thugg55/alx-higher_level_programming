#!/usr/bin/python3
""" Script takes in the name of the state as an argument and 
list all cities ofthe state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
            host='localhost', port=3306)
    c = db.cursor()

    c.execute("""SELECT cities.name FROM cities
              INNER JOIN states
              ON cities.state_id = states.id
              WHERE states.name = %s
              ORDER BY cities.id ASC;""", (state,))

    tally = 0
    for i in c.fetchall():
        for y in i:
            if tally != 0:
                print(", ", end="")
            print(y, end="")
            tally = tally + 1
    print()
