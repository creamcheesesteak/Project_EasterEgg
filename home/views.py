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

def analysis(request):
    return render(request, 'analysis.html')

def aid(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'home_copy.html')

def free(request):
    return render(request, 'free.html')

def paid(request):
    return render(request, 'paid.html')

def ml(request):
    return render(request, 'ml.html')

def sample(request):
    return render(request, 'sample.html')