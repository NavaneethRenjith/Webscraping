from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(
    executable_path=r"C:\Users\Navaneeth R\programs\web scraping\projects\chromedriver_win32\chromedriver.exe"
)
driver.get("https://www.imdb.com/chart/top")

movies = []
ratings = []

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

for data in soup.find_all("td", {"class": "titleColumn"}):
    movie = data.a
    movies.append(movie.text)

for data in soup.find_all("td", {"class": "imdbRating"}):
    rating = data.strong
    ratings.append(rating.text)

time.sleep(10)
driver.close()

imdb = dict(zip(movies, ratings))
for key, vals in imdb.items():
    print(key, " - ", vals)

