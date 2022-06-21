import requests
import psycopg2
import logging
import sys
import json
import csv


conn = psycopg2.connect(
    host="arjuna.db.elephantsql.com",
    database="kpodyujx",
    user="kpodyujx",
    password="eYCCvsQlP4_M3mb1dIZonEqSdIQ2pS7C")

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS subwayride")
cur.execute(""" CREATE TABLE subwayride(
                    date DATE, 
                    ride_num INTEGER,
                    alight_num INTEGER
                    );
            """)