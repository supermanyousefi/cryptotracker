from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def home(request):
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    btc_price = data['bitcoin']['usd']
    context = {'btc_price':btc_price}
    return render(request,'tracker/home.html',context)