from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    path = request.path
    resultstr = ''
    if path == '/index':
        resultstr = '<h1>TEAM "EasterEgg"의 공간입니다.</h1>'
    else :
        resultstr = '<h1>Project_multi_A3</h1>'
    return HttpResponse(resultstr)

def home(request):
    result = {'first':'Multi_A3', 'second':'TEAM EasterEgg'}
    return render(request, 'home.html', context=result)