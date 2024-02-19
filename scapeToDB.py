from bs4 import BeautifulSoup
import requests
import sqlite3

conn = sqlite3.connect('qoutesTest.db')
c = conn.cursor()



page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

for quote, author in zip(quotes, authors):
    quote_text = quote.text.strip()
    author_name = author.text.strip()
    c.execute('''INSERT INTO qoutesFull VALUES(?,?)''',(quote_text, author_name))
    print(quote.text + " --" + author.text)

conn.commit()
print('done')

c.execute('''SELECT * FROM qoutesFULL''')
results = c.fetchall()
print(len(results))
conn.close()