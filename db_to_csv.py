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

weather_query = "COPY (SELECT * FROM weather) To STDOUT With CSV DELIMITER ','"
with open("weather.csv", "w") as file:
        cur.copy_expert(weather_query, file)