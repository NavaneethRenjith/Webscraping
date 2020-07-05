from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(
    executable_path=r"C:\Users\Navaneeth R\programs\web scraping\projects\chromedriver_win32\chromedriver.exe"
)
driver.get("https://www.billboard.com/charts/hot-100")

songs = []
artists = []

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

for a in soup.find_all("li", {"class": "chart-list__element"}):
    song = a.find("span", {"class": "chart-element__information__song"})
    artist = a.find("span", {"class": "chart-element__information__artist"})
    songs.append(song.text)
    artists.append(artist.text)

time.sleep(10)
driver.close()

tracks = dict(zip(songs, artists))
for key, vals in tracks.items():
    print(key, " - ", vals)
