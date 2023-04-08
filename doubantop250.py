from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool

url = "https://music.douban.com/top250?start="
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62"
}

def get_album_title(num):
    res = requests.get(url+str(num),headers=header)
    html = res.text
    content = BeautifulSoup(html,"html.parser")
    tables = content.find_all("table")
    album_titles = []
    for table in tables:
        a = table.find("a")["title"]
        album_titles.append(a)
    return album_titles

if __name__ == '__main__':
    with Pool(5) as p:
        results = p.map(get_album_title, range(0, 250, 25))
        for result in results:
            for title in result:
                print(title)
