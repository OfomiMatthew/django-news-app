from django.shortcuts import render
import requests

def index(request):
   
    category = request.GET.get('category', 'general')

    
    api_key = '987a63c01f5d42aabf479c02d492c0a9'
    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={api_key}"

    response = requests.get(url)
    json_response = response.json()

    articles = json_response['articles']

    return render(request, 'newsApp/index.html', {'articles': articles})
