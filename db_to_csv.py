import requests
import json
import psycopg2
import csv

conn = psycopg2.connect(
    host="arjuna.db.elephantsql.com",
    database="kpodyujx",
    user="kpodyujx",
    password="eYCCvsQlP4_M3mb1dIZonEqSdIQ2pS7C")

cur = conn.cursor()


subway_query = "Copy (SELECT * FROM subwayride) To '/Users/hyunchaiwon/Section3/project' With CSV DELIMITER ','";
with open("weather.csv", "w") as file:
        cur.copy_expert(subway_query, file)

weather_query = "Copy (SELECT * FROM weather) To '/Users/hyunchaiwon/Section3/project' With CSV DELIMITER ','";
with open("weather.csv", "w") as file:
        cur.copy_expert(weather_query, file)
