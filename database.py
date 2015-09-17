# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 23:14:57 2015

@author: Kruthika
"""

import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db')
with con:
    
    cur = con.cursor() 
    
    #Creating table weather and printing the rows
    #cur.executescript("""
    #DROP TABLE IF EXISTS weather;
    cur.execute("DROP TABLE IF EXISTS weather")
    cur.execute("CREATE TABLE weather(city TEXT, year INT, warm_month TEXT, cold_month TEXT, average_high INT)");
    cur.execute("INSERT INTO weather VALUES('New York City',   2013  ,  'July'  ,      'January'   ,  62)");
    cur.execute("INSERT INTO weather VALUES('Boston',          2013  ,  'July'  ,      'January'   ,  59)");
    cur.execute("INSERT INTO weather VALUES('Chicago',         2013    , 'July ' ,     'January'   ,  59)");
    cur.execute("INSERT INTO weather VALUES('Miami' ,           2013  ,  'August' ,    ' January'  ,   84)");
    cur.execute("INSERT INTO weather VALUES('Dallas' ,          2013 ,   'July'  ,      'January'  ,   77)");
    cur.execute("INSERT INTO weather VALUES('Seattle' ,         2013  ,  'July'   ,     'January'  ,   61)");
    cur.execute("INSERT INTO weather VALUES('Portland' ,       2013   , 'July'   ,     'December'  ,  63)");
    cur.execute("INSERT INTO weather VALUES('San Francisco' ,   2013  ,  'September' ,   'December' ,    64)");
    cur.execute("INSERT INTO weather VALUES('Los Angeles'  ,   2013  ,  'September' ,  'December' ,    75)");
    #""")

    con.commit()
    
    cur.execute("SELECT * FROM weather")

    rows = cur.fetchall()
    for row in rows:
        print row
    
    #Creating the table 'cities' and printing the rows
    cities = (('New York City', 'NY'),
               ('Boston', 'MA'),
                ('Chicago', 'IL'),
                 ('Miami', 'FL'),
                   ('Dallas', 'TX'),
                    ('Seattle', 'WA'),
                      ('Portland', 'OR'),
                       ('San Francisco', 'CA'),
                        ('Los Angeles', 'CA'))
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute("CREATE TABLE cities(name text, state text)");    
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.execute("SELECT * FROM cities")
    rows1 = cur.fetchall()

    for row1 in rows1:
        print row1
        
        
    #Joining the tables
    cur.execute ("""select name, state FROM cities 
INNER JOIN weather ON name = city WHERE warm_month = 'July'""")
    rows2 = cur.fetchall()
    for row2 in rows2:
        print ("The cities that are warmest in July are:{}".format(row2))
        
    #Storing in panda dataframe
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(row2, columns=cols)
    