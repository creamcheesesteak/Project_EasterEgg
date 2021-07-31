## :white_square_button:프로젝트 명 : Easter Egg

- [팀 구성원과 역할분담](https://github.com/creamcheesesteak/Project_EasterEgg/tree/master/home)

- :chart_with_upwards_trend:프로젝트 개요와 목적
  - 주제 : 모바일 애플리케이션 이용현황을 분석하여 시각화 서비스 제공
  - 개요 : 애플리케이션 순위 데이터(Google play, ios)를 스크래핑하여 카테고리 별로 분류한다. 데이터 수집 결과 상위 범주로서 무료/유료 앱으로 구분할 수 있었다. 이에 본 프로젝트는 무료 앱과 유료 앱을 구분하여 데이터 시각화 작업을 진행하고자 한다. 
    - 무료 앱 데이터에 대한 시각화 작업을 수행한다. 이를 통해 국가에 따라 앱 카테고리를 기준으로 이용자들의 앱 선호도와 비중의 분포를 파악할 수 있다. 
    - 데이터 수집 결과 유료 앱 순위에 랭크된 대부분이 게임 앱이라는 것을 확인할 수 있었다. 따라서 본 프로젝트에서는 유료 앱의 타 카테고리 간 비교분석이 유의미하지 않을 것이라고 판단되어, 유료 앱 중 '게임' 카테고리에 한정하여 게임 장르(롤플레잉, 아케이드, etc)의 선호도와 비중의 분포를 파악하고 이를시각화하고자 한다. 
    - 데이터 세트(“Google Play Store Apps” in kaggle)를 이용해 이용자들이 평가한 앱 평점에 영향을 주는 요인들을 파악하고 요인 간의 상관성을 분석한다. 

- 시연

  [![SC2 Video](https://raw.githubusercontent.com/creamcheesesteak/Project_EasterEgg/master/static/images/scaping/main_page.PNG )](https://www.youtube.com/watch?v=p70Zis63m28)



## :white_square_button:프로젝트 수행방법

* [스크래핑](https://github.com/creamcheesesteak/Project_EasterEgg/tree/master/scraping)
* [머신러닝](https://github.com/creamcheesesteak/Project_EasterEgg/tree/master/ML)
* [웹 구현](https://github.com/creamcheesesteak/Project_EasterEgg/tree/master/templates)
* [분석도구 개략](https://github.com/creamcheesesteak/Project_EasterEgg/tree/master/web_config)

## :white_square_button:일정

- 프로젝트 수립과 데이터 수집

  - 7/15 ~ 7/17 : 주제선정, 역할분담, 환경설정
  - 7/18 ~ 7/19 : 데이터 수집, 스크래핑, 통계
    - Selenium, BeautifulSoup, Pandas

- 데이터 전처리·분석

  - 7/20 ~ 7/23 : 머신러닝
    - Numpy, Pandas, sklearn(Regression, Kmeans), SQLite3
  - 7/24 ~ 7/25 : 사전 기획 내용과 머신러닝 결과 비교분석

- 웹 구현

  - 7/20 ~ 7/30 : 웹서버 구현
    - Django, Html5
  - 7/26 ~ 7/28 : 데이터 시각화
    - Highchart/Plotly, Matplotlib/pyecharts, seaborn, Heatmap, Folium

- 포트폴리오 작성 

  - 7/24 ~ 7/30 : PPT, 보고서 작성











