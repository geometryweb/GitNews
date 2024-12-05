import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import random

titleList = []

# User-Agent 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

for j in range(1, 5):
    res = req.get("https://search.daum.net/search?w=news&nil_search=btn&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EC%86%8D%EB%B3%B4&p=" + str(j), headers=headers)
    
    # 요청 후 무작위 시간 지연
    time.sleep(random.uniform(2, 5))  # 2초에서 5초 사이의 랜덤 시간
    
    soup = bs(res.text, "lxml")
    title = soup.select("div.item-title > strong > a")
    
    for i in title:
        titleList.append(i.text)

print(titleList)
dic = {"뉴스제목": titleList}
df = pd.DataFrame(dic)
df.to_csv("data.csv", encoding="euc-kr", index=False)
