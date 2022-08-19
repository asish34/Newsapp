from django.shortcuts import render
# from .news import News
import random
import requests

apikey="7d52afdc586c4a2587d8f53d80aed4bf"
endpoint="https://newsapi.org/v2/top-headlines"

# Create your views here.

def home(request):
    p=request.GET.get("q")
    if p==None:    
        parameter={
            "apiKey":apikey,
            "country":"in",
            "category":"general",
        }
    else:
        parameter={
            "apiKey":apikey,
            "country":"in",
            "category":p,
        }  
    response=requests.get(endpoint,params=parameter)
    news=response.json()["articles"]
    list1=[]
    for i in news:
        if i["urlToImage"] !=None:
            list1.append(i["urlToImage"])  

    return render(request,"home.html",{
        "news":news,
        "carsol1":random.choice(list1),
        "carsol2":random.choice(list1),
        "carsol3":random.choice(list1),
    })


def about_me(request):
    return render(request,"about_me.html")
