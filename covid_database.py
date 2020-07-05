import sqlite3
from selenium import webdriver
from bs4 import BeautifulSoup

conn = sqlite3.connect("covid_database.sqlite")
cur = conn.cursor()

cur.executescript(
    """
    DROP TABLE IF EXISTS Covid;

    CREATE TABLE Covid(
        country TEXT UNIQUE,
        cases   INTEGER,
        new     INTEGER
    );
    """
)

driver = webdriver.Chrome(
    executable_path=r"C:\Users\Navaneeth R\programs\web scraping\projects\chromedriver_win32\chromedriver.exe"
)
driver.get("https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?")
content = driver.page_source

soup = BeautifulSoup(content, "html.parser")

countries = []
cases = []
new_cases = []

for data in soup.find_all("tr", {"class": "odd"}):
    country = data.find_all("td")[1]
    case = data.find("td", {"class": "sorting_1"})
    new = data.find_all("td")[3]
    countries.append(country.text)
    cases.append(case.text)
    new_cases.append(new.text)

for data in soup.find_all("tr", {"class": "even"}):
    country = data.find_all("td")[1]
    case = data.find("td", {"class": "sorting_1"})
    new = data.find_all("td")[3]
    countries.append(country.text)
    cases.append(case.text)
    new_cases.append(new.text)

driver.close()

for i in range(len(countries)):
    if countries[i] is None or cases[i] is None:
        continue

    cur.execute(
        """INSERT OR IGNORE INTO Covid (country, cases, new) 
        VALUES ( ?, ?, ? )""",
        (countries[i], cases[i], new_cases[i]),
    )

    conn.commit()

cur.close()

