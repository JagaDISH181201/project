from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    city=request.GET.get('city')
    api_key='1b3f22d3b5efc31c3645c2fb0a9db806'
    api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    print(api_url)
    api = requests.get(api_url).json()
    temprature=api['main']['temp']
    city=api['name']
    country=api['sys']['country']
    
    return render(request,'index.html',{'temprature':temprature,'city':city,'country':country})
