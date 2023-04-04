from bs4 import BeautifulSoup
import requests

url = "https://music.douban.com/top250?start="
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62"
}
for num in range(0,250,25):
    res = requests.get(url+str(num),headers=header)
    html = res.text
    content = BeautifulSoup(html,"html.parser")
    tables = content.find_all("table")
    for table in tables:
        a = table.find("a")["title"]
        print(a)