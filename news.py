import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
titleList =[]
for j in range(1, 5):
    res = req.get("https://search.daum.net/search?w=news&nil_search=btn&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EC%86%8D%EB%B3%B4&p=" + str(j))
    # print(res)
    # time.sleep(1)
    soup = bs(res.text, "lxml")
    # print(soup)
    title = soup.select("div.item-title > strong > a")
    # print(title[0].text)
    for i in title:
        titleList.append(i.text)
       
  
# print(titleList)
dic = {"뉴스제목" : titleList}
df = pd.DataFrame(dic)
df.to_csv("data.csv", encoding="euc-kr", index =False)
