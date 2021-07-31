# 분석 도구 개략

1. Django 환경 구축 
   - Pycharm
   - Groom


2. 데이터 수집과  전처리
    - 스크래핑 : https://www.appannie.com/,  https://sensortower.com/
      - BeautifulSoup : 정적 HTML 문서 parsing, 데이터 추출 -> `parser`, `select`
      - Requests: HTML source 다운로드 -> `get content`, `status_code`
      - Pandas : 데이터프레임 생성
      - SQLite3 : 데이터베이스 관리
      - Seaborn `heatmap` : 변수 간 상관관계 분석
      - Matplotlib : 그래프 시각화
    
    - 머신러닝 : https://www.kaggle.com/lava18/google-play-store-apps
      - Pandas : 캐글 데이터 load -> `read_csv`
      - 연속형, 분류형 변수 구분 : `info()`, `describe()`, `value_counts()`
      - One-hot encoding `get_dummies`: 분류형 변수 처리
      - 종속변수, 독립변수 결정
      - Seaborn `heatmap`: 변수 간 상관관계 분석
      - Sklearn : 데이터 표준화 -> `preprocessing`
      - Sklearn : 데이터 구분 -> `train_test_split`
      - Sklearn : 예측값 도출 -> xgboost `predict`    





[<Main>](https://github.com/creamcheesesteak/Project_EasterEgg)
