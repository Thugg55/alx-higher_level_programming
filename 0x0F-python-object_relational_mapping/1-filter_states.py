#!/usr/bin/python3
"""
Script list all states with a name starting with N fro thw database
"""

import MYSQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1], pswd=sys.argv[2], db=sys.argv[3], host='localhost', port=3306)
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id")
    [print(state) for state in curs.fetchall()]
