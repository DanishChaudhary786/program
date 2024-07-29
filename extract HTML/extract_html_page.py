import selectorlib
import requests
from datetime import datetime
import sqlite3

connection = sqlite3.connect("program.db")

URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def scrape(url):
    """Scrap the page scource from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def store(extracted):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO program VALUES (?,?)", (now, extracted))
    connection.commit()

def displaying():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM program")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    source = scrape(URL)
    extracted = extract(source)
    store(extracted)
    displaying()
