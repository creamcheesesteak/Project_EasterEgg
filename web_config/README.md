# 분석도구 개략

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
