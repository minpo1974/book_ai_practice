import sqlite3

dbpath = "hw.sqlite3"
sql = '''
    create table if not exists person (
        id integer primary key,
        height number,
        weight number,
        typeno integer
    )
'''

with sqlite3.connect(dbpath) as conn :
    conn.execute(sql)