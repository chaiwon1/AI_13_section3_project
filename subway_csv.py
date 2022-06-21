import requests
import json
import psycopg2
import csv


#postgre와 연결해서 db연결
conn = psycopg2.connect(
    host="arjuna.db.elephantsql.com",
    database="kpodyujx",
    user="kpodyujx",
    password="eYCCvsQlP4_M3mb1dIZonEqSdIQ2pS7C")

cur = conn.cursor()


#db에 저장
cur.execute("DROP TABLE IF EXISTS subway")
cur.execute(""" CREATE TABLE subway(
                    date DATE NOT NULL PRIMARY KEY, 
                    ride_num INTEGER, 
                    alight_num INTEGER
                    );
            """)

with open('subway_data.csv') as f:
    line = csv.reader(f)
    next(line)
    for row in line:
        temp = {}
        temp_list = []
        temp.update(
            {
                'date' : row[1],
                'ride_num' : row[2],
                'alight_num' : row[3]
            }
        )
        temp_list.append(list(temp.values()))

        for j in temp_list :
            cur.execute("INSERT INTO subway(date, ride_num, alight_num) VALUES (%s, %s, %s)", j)

conn.commit()