import requests as r
import bs4 as b
import json
def greet(fx):
    def mfx():
        print("WELCOME TO NIKHIL NEWS, HERE YOU WILL GET DAILY REFRASHING NEWS!")
        print("just type which type of news you want to read")
        fx()
        print("BYE BYE SEE YOU NEXT TIME")
    return mfx
@greet
def modify():
    print("press 1 for news related to politics\npress 2 for news related to crime\npress 3 for news related to drugs\npress 4 for news related to trading")
    option=int(input("enter your option: "))
    match option:
        case _ if option==1:
            url="https://newsdata.io/api/1/latest?apikey=pub_d0d4187901f341549754d8eccd8c4ff9&q=nepal"
            news=r.get(url)
            news=json.loads(news.text)
            # print(news)
            for article in news["results"]: 
                print(article["title"])
                print(article["description"])
                print("------------------------------------------------------------------")
        case _ if option==2:
            url="https://newsdata.io/api/1/latest?apikey=pub_d0d4187901f341549754d8eccd8c4ff9&q=politics&language=en&category=politics&country=in&timezone=Asia/Almaty"
            news=r.get(url)
            soup=b.BeautifulSoup(news.text,'html.parser')
            print(soup.prettify())
            # for headline in soup.find_all():
            #     print(headline.text)
        case _ if option==3:
            #url
            #news=r.get(url)
            soup=b.BeautifulSoup(url,'html.parser')
            for headline in soup.find_all(""):
                print(headline.text)
        case _ if option==4:
            #url
            #news=r.get(url)
            soup=b.BeautifulSoup(url,'html.parser')
            for headline in soup.find_all("p"):
                print(headline.text)
        case _ :
            print("invalid option")
modify()