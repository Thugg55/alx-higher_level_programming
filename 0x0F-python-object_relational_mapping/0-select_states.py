#!/usr/bin/python3
"""
Script list all states from the hbtn_0e_0_usa database
"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    user = sys.argv[1]
    pswd = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(user=user, pswd=pswd, db=dbname, host='localhost', port=3306)
    curs = db.cursor()
    curs.execute("SELECT * FROM `states` ORDER BY states.id;")
    [print(state) for state in curs.fetchall()]
