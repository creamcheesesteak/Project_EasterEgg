from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    path = request.path
    resultstr = ''
    if path == '/home':
        resultstr = '<h1>TEAM "EasterEgg"의 공간입니다.</h1>'
    else :
        resultstr = '<h1>Project_multi_A3</h1>'
    return HttpResponse(resultstr)

def index01(request):
    result = {'first':'Multi_A3', 'second':'TEAM EasterEgg'}
    return render(request, 'index.html', context=result)