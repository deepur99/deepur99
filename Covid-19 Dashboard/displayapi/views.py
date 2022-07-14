from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    response=requests.get('https://api.covid19api.com/summary').json()
    responses = response['Countries'] 
    GlobalResponses = response['Global'] 
    context= {'responses':responses,'GlobalResponses':GlobalResponses}
    return render(request,'index.html',context)

def inner(request,Country):
    response=requests.get("https://api.covid19api.com/live/country/Spain").json()
    responses = response
    context= {'Country':Country,'responses':responses}
    return render(request,'inner.html',context)

