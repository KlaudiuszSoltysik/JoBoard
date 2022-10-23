from django.shortcuts import render
import requests

url = ("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4e0ad1a0acb34407a06c85ae68a19813")

def home(request):
    response = requests.get(url).json()['articles']

    return render(request, 'home.html', {'response': response[0:5]})
