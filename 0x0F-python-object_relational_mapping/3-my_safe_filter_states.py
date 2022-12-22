#!/usr/bin/python3
# DISPLAYS ALL VALUES IN THE STATES TABLE OF THE DATABASE HBTN_0E_0_USA
# WHOSE NAME MATCHES THAT SUPPLIED AS ARGUMENT.
# SAFE FROM SQL INJECTIONS.
# USAGE: ./3-MY_SAFE_FILTER_STATES.PY <MYSQL USERNAME> \
#                                     <MYSQL PASSWORD> \
#                                     <DATABASE NAME> \
#                                     <STATE NAME SEARCHED>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
