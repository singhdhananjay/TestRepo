# Advance concept to show Generator, Decorator and Context manager in action 
#

from sqlite3 import connect
from contextlib import contextmanager 

@contextmanager
def tempTable(cur):
    cur.execute("create table points(x int, y int)")
    try:
        yield
    finally:
        cur.execute("drop table points")     

with connect("test.db") as conn:
    cur = conn.cursor()
    with tempTable(cur):
        cur.execute("insert into points (x, y) values(10, 20)")
        cur.execute("insert into points (x, y) values(20, 30)")
        for row in cur.execute("select x, y from points"):
            print(row)         