import sqlite3

conn = sqlite3.connect("quotes.db")
c = conn.cursor()
#c.execute('''CREATE TABLE qoutes(qoute TEXT, author TEXT, tablenumber INT)''')

#c.execute('''DROP TABLE qoutes''')

qoute = "hello"
author = "A very wise man"
tablenumber = 3

c.execute('''INSERT INTO qoutes VALUES(?,?, ?)''', (qoute, author, tablenumber))

conn.commit()
c.execute('''SELECT * FROM qoutes''')
results = c.fetchall()
print(results)