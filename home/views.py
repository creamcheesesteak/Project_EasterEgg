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

def ml(request):
    return render(request, 'ml.html')



def free(request):
    return render(request, 'free.html')

def paid(request):
    return render(request, 'paid.html')

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
    df_if = pd.read_sql("SELECT * FROM i_f_"+nation+"", db_nation, index_col=None)
    df_ip = pd.read_sql("SELECT * FROM i_p_"+nation+"", db_nation, index_col=None)
    df_gpf = pd.read_sql("SELECT * FROM gp_f_"+nation+"", db_nation, index_col=None)
    df_gpp = pd.read_sql("SELECT * FROM gp_p_"+nation+"", db_nation, index_col=None)

    # overview 100 stacked bar
    counts_if = collections.Counter(df_if['App_cat'])
    counts_ip = collections.Counter(df_ip['App_cat'])
    counts_gpf = collections.Counter(df_gpf['App_cat'])
    counts_gpp = collections.Counter(df_gpp['App_cat'])
    dict_gpf = {'Games_gpf': ['Action (Games)', 'Adventure (Games)', 'Board (Games)', 'Card (Games)', 'Casino (Games)',
                              'Casual (Games)', 'Dice (Games)', 'Education (Games)', 'Family (Games)', 'Family (Games)',
                              'Kids (Games)', 'Music (Games)', 'Puzzle (Games)', 'Racing (Games)', 'Role (Games)',
                              'Playing (Games)', 'Simulation (Games)', 'Sports (Games)', 'Strategy (Games)',
                              'Trivia (Games)', 'Word (Games)', 'Arcade (Games)', 'Educational (Games)',
                              'Role Playing (Games)'],
                'Application_gpf': ['Food and Drink (Applications)', 'Health and Fitness (Applications)',
                                    'Lifestyle (Applications)',
                                    'Weather (Applications)', 'Medical (Applications)', 'Navigation (Applications)',
                                    'Finance (Applications)', 'Entertainment (Applications)', 'Shopping (Applications)',
                                    'Social Networking (Applications)', 'Sports (Applications)',
                                    'Travel (Applications)',
                                    'Music (Applications)', 'Photo and Video (Applications)', 'Business (Applications)',
                                    'Developer Tools (Applications)', 'Graphics & Design (Applications)',
                                    'Productivity (Applications)',
                                    'Books (Applications)', 'Catalogs (Applications)', 'Education (Applications)',
                                    'Reference (Applications)',
                                    'Magazines and Newspapers (Applications)', 'News (Applications)',
                                    'Utilities (Applications)']}
    dict_gpp = {'Games_gpp': ['Action (Games)', 'Adventure (Games)', 'Board (Games)', 'Card (Games)', 'Casino (Games)',
                              'Casual (Games)', 'Dice (Games)', 'Education (Games)', 'Family (Games)', 'Family (Games)',
                              'Kids (Games)', 'Music (Games)', 'Puzzle (Games)', 'Racing (Games)', 'Role (Games)',
                              'Playing (Games)', 'Simulation (Games)', 'Sports (Games)', 'Strategy (Games)',
                              'Trivia (Games)', 'Word (Games)', 'Arcade (Games)', 'Educational (Games)',
                              'Role Playing (Games)'],
                'Application_gpp': ['Food and Drink (Applications)', 'Health and Fitness (Applications)',
                                    'Lifestyle (Applications)',
                                    'Weather (Applications)', 'Medical (Applications)', 'Navigation (Applications)',
                                    'Finance (Applications)', 'Entertainment (Applications)', 'Shopping (Applications)',
                                    'Social Networking (Applications)', 'Sports (Applications)',
                                    'Travel (Applications)',
                                    'Music (Applications)', 'Photo and Video (Applications)', 'Business (Applications)',
                                    'Developer Tools (Applications)', 'Graphics & Design (Applications)',
                                    'Productivity (Applications)',
                                    'Books (Applications)', 'Catalogs (Applications)', 'Education (Applications)',
                                    'Reference (Applications)',
                                    'Magazines and Newspapers (Applications)', 'News (Applications)',
                                    'Utilities (Applications)']}
    gpf_g = 0
    gpp_g = 0
    sum_gpf_b = 0
    sum_gpp_b = 0

    for category in dict_gpf['Games_gpf']:
        for key, value in counts_gpf.items():
            if key == category:
                sum_gpf_b = value + sum_gpf_b
    gpf_g = sum_gpf_b
    print(sum_gpf_b)

    for category in dict_gpp['Games_gpp']:
        for key, value in counts_gpp.items():
            if key == category:
                sum_gpp_b = value + sum_gpp_b
    gpp_g = sum_gpp_b
    print(sum_gpp_b)

    if_g = counts_if['Games']
    ip_g = counts_ip['Games']
    if_a = 100 - counts_if['Games']
    ip_a = 100 - counts_ip['Games']
    gpf_a = 100 - gpf_g
    gpp_a = 100 - gpp_g
    cnt_g_list = [gpp_g, gpf_g, ip_g, if_g]
    cnt_a_list = [gpp_a, gpf_a, ip_a, if_a]
    y_bar = ['Googe Play (paid)', 'Googe Play (free)', 'App Store (paid)', 'App Store (free)']

    y_group_ov = y_bar
    x_game = cnt_g_list
    x_app = cnt_a_list

    # free circle chart
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


    # paid sunburst chart
    labels = ['Total', 'Apps', 'Games']
    parents = ['', 'Total', 'Total']
    values = [len(df_gpp), gpp_a, gpp_g, ]
    for category in dict_gpp['Games_gpp']:
        for key, value in counts_gpp.items():
            if key == category:
                labels.append(key)
                parents.append('Games')
                values.append(value)

    labels_sun = labels
    parents_sun = parents
    values_sun = values

    context = {
        'nation':nation,
        'x_group_f': xArray_if,
        'y_value_if': y_value_if,

        'y_value': y_value_gdf,

        'y_group_ov': y_group_ov,
        'x_game': x_game,
        'x_app': x_app,

        'labels_sun': labels_sun,
        'parents_sun': parents_sun,
        'values_sun': values_sun,
    }
    return render(request, 'analysis.html', context)

