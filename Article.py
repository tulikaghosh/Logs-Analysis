#!/usr/bin/env python3

import psycopg2 as pg2
import sys

# Most popular article
connect = pg2.connect(database='news')

cursor = connect.cursor()
cursor.execute('SELECT * FROM most_popular_articles LIMIT 3;')
data = cursor.fetchall()
for line in data:
    print('"' + str(line[0]) + '"' + ' - ' + str(line[1]) + 'views')
print '\n'
cursor.close()


# Most popular author
connect = pg2.connect(database='news')
cursor = connect.cursor()
cursor.execute('SELECT * FROM most_popular_author;')
data = cursor.fetchall()
for line in data:
    print('"' + str(line[0]) + '"' + ' - ' + str(line[1]) + 'views')
print '\n'
cursor.close()


# Most error day
connect = pg2.connect(database='news')
cursor = connect.cursor()
cursor.execute('SELECT * FROM errors_day;')
data = cursor.fetchall()
for line in data:
    print(str(line[0]) + ' - ' + str(line[1]) + 'errors')
print("")
cursor.close()
