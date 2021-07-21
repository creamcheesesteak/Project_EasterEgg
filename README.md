# :chart_with_upwards_trend:프로젝트 : 모바일 애플리케이션 이용현황을 분석하여 시각화 분석서비스 제공

- 개요

  애플리케이션 순위 데이터(Google play, ios)를 스크래핑하여 카테고리 별로 분류한다. 자료 수집결과 상위 범주로서 무료/유료 앱으로 구분할 수 있었다. 이에 본 프로젝트는 무료 앱과 유료 앱을 구분하여 데이터 시각화 작업을 진행하고자 한다. 

  - 분류된 무료 앱 데이터에 대한 시각화 작업을 수행한다. 이를 통해 국가별 이용자들의 이용어플 비중의 분포와 선호를 파악할 수 있다. 
  - 자료 조사 결과 유료 앱 순위에 랭크된 대부분이 게임앱이라는 것을 확인할 수 있었다. 따라서 본 프로젝트에서는 유료앱의 타 카테고리 간 비교분석이 유의미하지 않을 것이라고 판단되어 유료 앱 중 '게임' 카테고리에 한정하여 게임 장르(롤플레잉, 아케이드, etc)의 선호도 비중을 시각화하여 분포와 선호도를 파악하고자 한다. 
  - 데이터 세트(“Google Play Store Apps” in kaggle)를 이용해 이용자들이 평가한 앱 평점에 영향을 주는 요인들이 무엇인지 변수들을 파악하고 상관성을 분석한다. 

 

## :white_square_button:팀 이름 : EasterEgg

- 구성

  - 팀 매니저 : [임태혁](https://github.com/creamcheesesteak) :link:(프로젝트 관리, 웹 구현 프론트엔드)
  - 구성원
    - [서미오](https://github.com/mmeooo) :link:(웹 스크래핑, 전처리)
    - [최솔비](https://github.com/SolbiChoi) :link:(웹 구현 백엔드)
    - [김정휴](https://github.com/aidsfintech) :link:(DB)

* 각오 : 데이터 분석을 통해서 사람들이 잘 알지 못했던 사실을 발견하거나 내용을 해석하고 의미를 부여해가나고자 함 
  * cf) 이스터에그 : 개발자가 재미로 숨겨둔 메세지나 기능 등을 이름

## :white_square_button:프로젝트 수행 방법/도구

데이터 수집, 환경구축(Django)

①스크래핑 : https://www.appannie.com/ , https://sensortower.com/

②데이터셋 : https://www.kaggle.com/lava18/google-play-store-apps

 

① 스크래핑

데이터수집과 전처리

- BeautifulSoup: 정적 HTML문서 파싱     /원하는 데이터 추출. parser, select
- Requests: HTML 소스 다운로드. get     content, status_code
- Pandas : 데이터프레임 생성
- Numpy

데이터 분석 : 상관관계 분석

- Pandas
- SQLites

시각화

- Matplotlib:     그래프

- Seaborn: heatmap(상관관계)

② 데이터셋

- pandas → 캐글 데이터 `read_csv`로 로드

- info(), describe(),     value_counts() 로 연속형, 분류형 변수 구분

  → 분류형은 one-hot encoding(get_dummies)

- 종속변수, 독립변수 결정

- seaborn → heatmap으로 변수 간 상관관계     분석

- Sklearn → preprocessing으로 데이터     표준화

- Sklearn →     train_test_split히여 데이터 나눔. shape으로     확인

- sklearn → xgboost: predict해     예측값 도출



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
    - Django, Html5, Highchart
  - 7/26 ~ 7/28 : 데이터 시각화
    - Matplotlib, seaborn, Heatmap, Folium, pyecharts

- 포트폴리오 작성 

  - 7/24 ~ 7/30 : PPT, 보고서 작성

