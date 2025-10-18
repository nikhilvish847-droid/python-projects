import requests as r
import json

topic=["politics","crime","cricket","trading"]
#creating a greeting function
def greet(fx):
    def mfx():
        print("WELCOME TO NIKHIL NEWS, HERE YOU WILL GET DAILY REFRASHING NEWS!")
        print("just type which type of news you want to read")
        fx()
        print("BYE BYE SEE YOU NEXT TIME")
    return mfx
@greet

#creting a functiont to fetch news via api
def modify():
    print(f"press 1 for news related to {topic[0]}\npress 2 for news related to {topic[1]}\npress 3 for news related to {topic[2]}\npress 4 for news related to {topic[3]}")
    option=int(input("enter your option: "))

    #using a matching fetaure#
    match option:
        case _ if option==1:
            #callig a api from  news.api
            url=f"https://newsdata.io/api/1/latest?apikey=pub_d0d4187901f341549754d8eccd8c4ff9&q={topic[0]}&language=en&category={topic[0]}&country=in&timezone=Asia/Almaty"
            news=r.get(url)
            news=json.loads(news.text)
            #extracting data from dictionary
            for article in news["results"]: 
                print(article["title"])
                print(article["description"])
                print("------------------------------------------------------------------")
        case _ if option==2:
            url=f"https://newsdata.io/api/1/latest?apikey=pub_d0d4187901f341549754d8eccd8c4ff9&q={topic[1]}&language=en&category={topic[1]}&country=in&timezone=Asia/Almaty"
            news=r.get(url)
            news=json.loads(news.text)
            for article in news["results"]: 
                print(article["title"])
                print(article["description"])
                print("------------------------------------------------------------------")
        case _ if option==3:
            url=f"https://newsdata.io/api/1/latest?apikey=pub_d0d4187901f341549754d8eccd8c4ff9&q={topic[2]}&language=en&category={topic[2]}&country=in&timezone=Asia/Almaty"
            news=r.get(url)
            news=json.loads(news.text)
            for article in news["results"]: 
                print(article["title"])
                print(article["description"])
                print("------------------------------------------------------------------")
        case _ if option==4:
            url=f"https://newsdata.io/api/1/latest?apikey=pub_d0d4187901f341549754d8eccd8c4ff9&q={topic[3]}&language=en&category={topic[3]}&country=in&timezone=Asia/Almaty"
            news=r.get(url)
            news=json.loads(news.text)
            for article in news["results"]: 
                print(article["title"])
                print(article["description"])
                print("------------------------------------------------------------------")
        case _ :
            print("invalid option")
modify()
