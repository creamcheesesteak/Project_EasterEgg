# 스크래핑



##### :white_square_button:개요

* 구글과 애플의 홈페이지를 스크래핑한 후에 타켓 국가를 설정하고 웹 스크래퍼를 만들어서 웹에서 모바일 애플리케이션 데이터를 스크래핑했습니다. 이때, 자동으로 .xls로 저장후 sqlite3에 DB로 저장하는 과정을 거쳤습니다. 이후 저장된 DB를 활용해 시각화 작업을 진행하였습니다.

<img src="https://raw.githubusercontent.com/creamcheesesteak/Project_EasterEgg/master/static/images/scaping/1.overview.PNG"  width="70%" height="70%">



##### :white_square_button:국가목록

* 모바일 애플리케이션 서비스를 제공하기위해 먼저 구글과 애플의 홈페이지에서 서비스하는 국가리스트를 스크래핑하였습니다.
  * [구글서비스국가목록스크래핑](https://github.com/creamcheesesteak/Project_EasterEgg/blob/master/scraping/1.extract_nations_in_googleplay.ipynb)
  * [애플서비스국가목록스크래핑](https://github.com/creamcheesesteak/Project_EasterEgg/blob/master/scraping/2.extract_nations_in_applestore.ipynb)

<img src="https://raw.githubusercontent.com/creamcheesesteak/Project_EasterEgg/master/static/images/scaping/2.extract_nations.PNG"  width="60%" height="60%">




* 정보를 스크래핑하고자하는 사이트(Appannie.com)에서 서비스하는 국가와 매칭하였고 애플과 구글국가목록의 교집합으로 98개의 동일한 데이터 세트(구글무료, 구글유료, 애플무료, 애플유료)를 구할 수 있음을 확인하였습니다. 이 중 40개국을 선별해 코딩을 진행하였습니다.

  <img src="https://raw.githubusercontent.com/creamcheesesteak/Project_EasterEgg/master/static/images/scaping/3.matching_nations.PNG"  width="70%" height="70%">

  * [앱애니와구글국가목매칭](https://github.com/creamcheesesteak/Project_EasterEgg/blob/master/scraping/1-2.matching_nations_googleplay.ipynb)
  * [앱애니와애플국가목록매칭](https://github.com/creamcheesesteak/Project_EasterEgg/blob/master/scraping/2-2.matching_nations_applestore.ipynb)
  * [국가목록](https://github.com/creamcheesesteak/Project_EasterEgg/blob/master/scraping/3.setting_intersection_of_nations.ipynb)



##### :white_square_button:스크래퍼

* 사전설명 : 웹 스크래핑을 할 때, `bs4`는 정적 텍스트 분석을 하기 때문에 속도가 매우 빠릅니다. 이때,`Selenium`은 단지 의도한 웹 페이지로 이동하는 수단으로만 활용됩니다. 하지만, 'Appannie' 홈페이지는 일반 `bs4`을 활용한 스크래핑이 거의 불가능하게 설정되어있어 여기서는 `Selenium `을 주로 이용하였습니다. `Selenium`은 실제 브라우저를 사용하는 동적 툴이라서 `bs4`보다 속도가 매우 느리다는 단점이 있지만, 우리 주의 주제에 최적화된 정보를 'Appannie'에서 온전히 구할 수 있기 때문에 이를 이용한 스크래퍼를 만들게 되었습니다.



* 구성 : 스크래퍼는 스크래퍼의 내용이 정의된 [auto_scraper.py](https://github.com/creamcheesesteak/Project_EasterEgg/blob/master/scraping/auto_scraper.py) 와 개인이 스크래퍼를 돌릴 수 있도록 [auto_scraper_operator](https://github.com/creamcheesesteak/Project_EasterEgg/blob/master/scraping/auto_scraper_operator.py) 런파일로 나뉘어져 있습니다.

  <img src="https://raw.githubusercontent.com/creamcheesesteak/Project_EasterEgg/master/static/images/scaping/4-1.scraper_operator_input.PNG"  width="60%" height="60%">

  * 개별국가의 정보를 일일이 스크래핑 할 때, 시간이 소요되기 때문에 팀원들에게 분석 범위를 지정하여 빠르게 스크래핑 할 수 있도록 런파일을 작성하였습니다.  각자 자신의 입력값과 범위를 지정하면 스크래핑이 가능합니다.

    <img src="https://raw.githubusercontent.com/creamcheesesteak/Project_EasterEgg/master/static/images/scaping/4-2.scraper_operator_run.PNG"  width="60%" height="60%">
  



* 각 1~100위까지의 랭킹 정보를 스크래핑하는 코드입니다.  `Selenium`의 사용한계가 존재하기 때문에 경우에 수에 따라 달라지더라도 원하는 정보를 가져올 수 있도록 추가적 코딩을 넣었습니다. 결과적으로 모든 정보를 의도한 대로 스크래핑할 수 있었습니다.

  <img src="https://raw.githubusercontent.com/creamcheesesteak/Project_EasterEgg/master/static/images/scaping/4-3.scraper_method.PNG"  width="60%" height="60%">

  

* 스크래핑의 정보는 자동으로 파일로 저장되고 파일의 이름은 애초에 런파일입력 정보에 따라 결정됩니다.

  <img src="https://raw.githubusercontent.com/creamcheesesteak/Project_EasterEgg/master/static/images/scaping/4-4.scraper_result.PNG"  width="60%" height="60%">



##### :white_square_button:sqlite3

* 사전에 설정한 국가리스트에대해 for문을 돌려 sqlite3 DB에 저장하였습니다. 오른쪽은 DB browser상에 제대로 저장된 사진입니다.

  <img src="https://raw.githubusercontent.com/creamcheesesteak/Project_EasterEgg/master/static/images/scaping/5.save_in_sqlite.PNG"  width="70%" height="70%">



##### :white_square_button:웹 페이지 구현

* 먼저  메인  페이지에서 이용자가 원하는 국가정보를 입력하면 해당 정보가 분석창으로 전달되도록 하였습니다. 아래의 사진을 보면, 화면은 오른편으로 이동하게 됩니다.

  ```python
  <form name="search" action="/analysis" method="GET">
  ```

  <img src="https://raw.githubusercontent.com/creamcheesesteak/Project_EasterEgg/master/static/images/scaping/6.input_in_html.PNG"  width="80%" height="80%">



* 분석창의 코드

  * 경로는 아래와 같으며, [home.views.py](https://github.com/creamcheesesteak/Project_EasterEgg/blob/master/home/views.py) 의 `def analysis`는 아래와 같습니다

      ```python
      # web_config.urls
        path('analysis', views.analysis),
      
      # home.views
        def analysis(request):
              return render(request, 'analysis.html', context)
      ```

      <img src="https://raw.githubusercontent.com/creamcheesesteak/Project_EasterEgg/master/static/images/scaping/7.def_analysis_detail.PNG"  width="60%" height="60%">
  



##### :white_square_button:시각화

* 시각화는 `plotly`를 사용했고 각 국가 검색에 따라 5개의 분석 그래프가 나타나도록 하였습니다.

  ```python
  # home.views.analysis
      context = {
              'nation':nation,
              'x_group_f': xArray_if,
              'y_value_if': y_value_if,
  
              'y_value': y_value_gpf,
  
              'y_group_ov': y_group_ov,
              'x_game': x_game,
              'x_app': x_app,
  
              'labels_sun': labels_sun,
              'parents_sun': parents_sun,
              'values_gpf': values_gpf,
  
              'labels_if': labels_if,
              'parents_if': parents_if,
              'values_if': values_if,
              'labels_gpf': labels_gpf,
              'parents_gpf': parents_gpf,
              'values_sun': values_sun,
          }
          return render(request, 'analysis.html', context)
  ```

  ```html
  <!-- analysis.html -->
  Ex. <script src='https://cdn.plot.ly/plotly-2.3.0.min.js'></script>
  Ex. <div id='overview_stacked'style="width:90%;max-width:700px"></div>
  Ex. <script>JavaScript</script>
  ```

  <img src="https://raw.githubusercontent.com/creamcheesesteak/Project_EasterEgg/master/static/images/scaping/8.visualizations.PNG"  width="70%" height="70%">





[Main](https://github.com/creamcheesesteak/Project_EasterEgg)

