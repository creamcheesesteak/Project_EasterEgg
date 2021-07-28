from django.http import HttpResponse
from django.shortcuts import render

import sqlite3
import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt

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

def info(request):
    return render(request, 'info.html')


def free(request):
    return render(request, 'free.html')

def paid(request):
    return render(request, 'paid.html')

def ml(request):
    return render(request, 'ml.html')


def aid(request):
    return render(request, 'index.html')

def sample(request):
    return render(request, 'sample.html')

# def value(request):
#     nation = request.get('nation')
#     print(nation)
#     return render(request, 'analysis.html',contenxt=nation)

def analysis(request):
    nation = request.GET.get('nation')
    db_nation = sqlite3.connect('C:/Develops/Project_multi_A3/nation.db')
    c = db_nation.cursor()
    df_if = pd.read_sql("SELECT * FROM i_f_" +nation+ "", db_nation, index_col=None)
    df_ip = pd.read_sql("SELECT * FROM i_p_" +nation+ "", db_nation, index_col=None)
    df_gpf = pd.read_sql("SELECT * FROM gp_f_" +nation+ "", db_nation, index_col=None)
    df_gpp = pd.read_sql("SELECT * FROM gp_p_" +nation+ "", db_nation, index_col=None)

    counts_if = collections.Counter(df_if['App_cat'])
    counts_gpf = collections.Counter(df_gpf['App_cat'])
    dict = {'Life': ['Food and Drink (Applications)', 'Health and Fitness (Applications)', 'Lifestyle (Applications)',
                     'Weather (Applications)', 'Medical (Applications)', 'Navigation (Applications)',
                     'Finance (Applications)', 'Food & Drink (Applications)', 'Social (Applications)',
                     'Communication (Applications)', 'Maps & Navigation (Applications)'],
            'Leisure': ['Entertainment (Applications)', 'Shopping (Applications)', 'Social Networking (Applications)',
                        'Sports (Applications)', 'Travel (Applications)', 'Music (Applications)',
                        'Photo and Video (Applications)', 'Music & Audio (Applications)',
                        'Books & Reference (Applications)', 'Art & Design (Applications)'],
            'Work': ['Business (Applications)', 'Developer Tools (Applications)', 'Graphics & Design (Applications)',
                     'Productivity (Applications)', 'Video Players & Editors (Applications)', 'Tools (Applications)'],
            'Edu': ['Books (Applications)', 'Catalogs (Applications)', 'Education (Applications)',
                    'Reference (Applications)', ' Magazines and Newspapers (Applications)', 'News (Applications)',
                    'Utilities (Applications)']}
    fr_group = ['Life', 'Leisure', 'Work', 'Edu']
    count_if_group = []
    sum_if_c = 0
    for groupif in fr_group:  # group : key = Life
        groupif = dict[groupif]  # dict['Life']
        for category in groupif:  # Food and Drink (Applications)
            for key, value in counts_if.items():
                if key == category:
                    sum_if_c = value + sum_if_c
        count_if_group.append(sum_if_c)
        print(sum_if_c)
        sum_if_c = 0

    count_gdf_group = []
    sum_gdf_c = 0
    for groupgpf in fr_group:  # group : key = Life
        groupgpf = dict[groupgpf]  # dict['Life']
        for category in groupgpf:  # Food and Drink (Applications)
            for key, value in counts_gpf.items():
                if key == category:
                    sum_gdf_c = value + sum_gdf_c
        count_gdf_group.append(sum_gdf_c)
        print(sum_gdf_c)
        sum_gdf_c = 0

    xArray_if = fr_group;
    y_value_if = count_if_group;

    y_value_gdf = count_gdf_group;


    context = {
        'nation':nation,
        'x_group_f': xArray_if,
        'y_value_if': y_value_if,

        'y_value': y_value_gdf,

    }
    return render(request, 'analysis.html', context)
