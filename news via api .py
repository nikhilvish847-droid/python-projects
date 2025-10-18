#importing a library which are going to use#
import requests as r
import json

topic=["politics","crime","cricket","trading"]
#creating a greeting function#
def greet(fx):
    def mfx():
        print("WELCOME TO NIKHIL NEWS, HERE YOU WILL GET DAILY REFRASHING NEWS!")
        print("just type which type of news you want to read")
        fx()
        print("BYE BYE SEE YOU NEXT TIME")
    return mfx
@greet

#creating a function to fetch news#
def modify():

    # taking a topic as input from user
    topic=input("news of which topic you want ?")
    
    #calling via api from news.api
    url=f"https://newsdata.io/api/1/latest?apikey=pub_d0d4187901f341549754d8eccd8c4ff9&q={topic}&language=en&category={topic}&country=in&timezone=Asia/Almaty"
    news=r.get(url)
    news=json.loads(news.text)
    
    #extracting data from dictionary
    for article in news["results"]: 
        print(article["title"])
        print(article["description"])
        print("------------------------------------------------------------------")

#calling function
modify()
