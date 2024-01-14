#!/usr/bin/python3
"""
connecting using mysql db
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host = "localhost", user = sys.argv[1], port = 3306, passwd = sys.argv[2], db = sys.argv[3], charset = "utf8")
    query = db.cursor()
    query.execute("SELECT * FROM states WHERE BINARY NAME = '{}'\ORDER BY id ASC".format(x))
    output = query.fetchall()
    for i in output:
        print(i)
    query.close()
    db.close()
