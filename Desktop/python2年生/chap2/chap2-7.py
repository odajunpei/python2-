import requests
from bs4 import BeautifulSoup

#webページを取得して解析する
load_url = "https://news.yahoo.co.jp/categories/it"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

#classで検索し、その中の全てのaタグを検索して表示する。
topic = soup.find(class_="topicsList_main")
for element in topic.find_all("a"):
    print(element.text)
