import sqlite3
import random

dbpath = "hw.sqlite3"

def insert_db(conn) :
    height = random.randint(130,180)
    weight = random.randint(30,100)

    type_no = 1
    bmi = weight / (height/100) ** 2
    if bmi < 18.5 :
        type_no = 0
    elif bmi < 25 :
        type_no = 1
    elif bmi < 30 :
        type_no = 2
    elif bmi < 35 :
        type_no = 3
    elif bmi < 40 :
        type_no = 4
    else :
        type_no = 5
    
    sql = '''
       insert into person(height, weight, typeno) values (?,?,?)
    '''
    values = (height, weight, type_no)
    print(values)
    conn.executemany(sql, [values])

with sqlite3.connect(dbpath) as conn :
    for i in range(15000) :
        insert_db(conn)
    c = conn.execute('select count(*) from person')
    cnt = c.fetchone()
    print(cnt[0])
