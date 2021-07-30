# 머신러닝

EasterEgg는 데이터 세트(“Google Play Store Apps”  in kaggle)를 이용한 머신러닝을 통해 이용자들이 평가한 앱 평점에 영향을 주는 요인들이 무엇인지 변수들을 파악하고 상관성을 분석하였습니다.

머신러닝은 다음과 같은 순서로 진행하였습니다.

1. pandas로 Kaggle의 “Google Play Store Apps” 데이터를 불러옵니다.

![image-20210728213338972](https://user-images.githubusercontent.com/85269812/127595503-dde1898a-4925-4d27-bc9d-b8c3e72493ed.png)

2.  불러온 데이터의 머신러닝을 진행하기 위하여 데이터 전처리를 진행하였습니다. 

 info(), describe()를 통해 결측치가 있는 데이터를 찾아 mean값을 넣어서 결측치를 제거하였고, data 에 포함 된 문자를 제거 후 단위를 통합해주었습니다. 또한 'Rating' 을 종속변수로 사용하기 위한 범주화하여 새롭게 'preprocessed_Rating'로 저장하였습니다.

3.  데이터를 info(), describe(), value_counts() 를 통해 연속형, 분류형 변수로 구분하였습니다.

* 연속형 : 'Rating', 'Reviews', 'Size', 'Price'
* 분류형 : 'Installs', 'Content Rating', 'Genres'

3. 앱 평점에 영향을 주는 변수는 무엇인지 상관성, 결정력을 파악하기위해 종속변수를 'Rating'으로하고 독립변수를 'Reviews', 'Size', 'Installs', 'Price', 'Content Rating', 'Genres'로  설정하였습니다.
4. seaborn의 heatmap 사용하여 변수간 상관관계를 분석하였습니다.

![image-20210728221810886](https://user-images.githubusercontent.com/85269812/127595517-426d46da-473e-4c1e-9b3d-3a12fb15afd4.png)

​	이를 통해 Rating과 Installs가 가장 상관성이 높음을 알수있었습니다.

다음은 머신러닝의 교육 단계입니다.

1. 머신러닝은 문자열 값들을 숫자형으로 인코딩하는 전처리 작업(Preprocessing) 후에 학습을 시켜야 하기 때문에 분류형 컬럼만을 선택하여  get_dummies (Onehot encoding)을 진행하였습니다.

![image-20210728231146138](https://user-images.githubusercontent.com/85269812/127595548-e67ecf08-a124-4578-8439-a43501c47524.png)

2. 회귀분석을 위해 standard scaler를 사용하여 범위를 같게 만들었습니다.

3. 모델의 성능평가를 진행하기위해 훈련 데이터셋을 훈련용 데이터와 성능평가용 데이터로 나눈 후(data split), 성능평가 단계에서는 모델 학습에 이용하지 않은 성능평가용 데이터를 사용합니다.

   (이때 훈련용 데이터를 훈련세트(training set), 성능평가용 데이터를 테스트세트(test set)이라고 합니다.)

![image-20210728225346467](https://user-images.githubusercontent.com/85269812/127595539-d8c558b6-43d0-46f5-b2d9-0671b43b2ad0.png)

4. model learning

   * 먼저 로지스틱 회귀 분석을 진행하여 score를 측정하였습니다.

   (로지스틱사용을 위해 'Content Rating', 'Genres'을 숫자로 범주화한 후에 분석 진행)

![image-20210728225647024](https://user-images.githubusercontent.com/85269812/127595541-8250606f-cb0e-4a52-bd43-3df94ae7fc35.png)

   * 로지스틱 회귀분석보다 향상된 점수를 위해 xgboost 적용하여  score를 측정하였습니다.

![image-20210728225757897](https://user-images.githubusercontent.com/85269812/127595543-854699f2-d291-4f1f-af30-ed65cdd286d1.png)

   * 분석의 정확도를 향상시키기 위하여 k fold 교차검증을 적용해 score를 측정하였습니다.

![image-20210728225901668](https://user-images.githubusercontent.com/85269812/127595545-b60239cc-99dd-4329-bd13-f7cf74b3bb4d.png)

5. predict

   위에서 훈련시킨 모델을 사용하여 예측하는 순서입니다. 메트릭스에서  머신러닝 예측, 분류 모델의 학습 성능 평가를 위한 표현 모델인 f1 score를 확인하였습니다.

![image-20210728224517219](https://user-images.githubusercontent.com/85269812/127595533-7df473e1-b5c1-48a7-8926-5132f1d9d3bb.png)



## Visualization

우리는 앞서 머신러닝을 통해 이용자들이 평가한 앱 평점에 영향을 주는 요인들이 무엇인지 변수들을 파악하고 상관성 분석하였습니다. 본 페이지는 그 결과를 바탕으로한 시각화 자료입니다.

1.  Rating의 분포

![image-20210729094153246](https://user-images.githubusercontent.com/85269812/127595474-7cb519e1-249a-4a10-926a-43b3d4c800e3.png)

이를 통해 대부분의 어플이 4점대에 분포되어있음을 알수있었습니다.

2. Rating과 Reviews의 상관 관계

![image-20210729094502409](https://user-images.githubusercontent.com/85269812/127595481-acd7a845-72d4-479e-b594-f627b217b8e0.png)

이를 통해 많은 사람들에게 알려진 어플일수록 좋은 평점을 받는것을 알수있었습니다.

3. Rating과 Size의 상관관계

![image-20210729095046431](https://user-images.githubusercontent.com/85269812/127595483-510564ec-09cc-4c3c-8294-3bc0ec6ec629.png)

본 차트를 통해 두 변수의 상관관계를 찾기는 어려웠습니다.

4. Rating과 Installs의 상관관계

![image-20210729095226144](https://user-images.githubusercontent.com/85269812/127595488-3241b68a-73fd-4458-a9de-7edfefd13f3b.png)

이를 통해 설치 횟수가 평점에 영향을 미치는 것을 알수있었습니다.

5. Rating과 Price의 상관관계

![image-20210729095408424](https://user-images.githubusercontent.com/85269812/127595494-5e7e883b-877a-4095-b474-99afe04298f7.png)

![image-20210729095434747](https://user-images.githubusercontent.com/85269812/127596075-eb8874d0-52d8-4a5d-8642-a0ad9df61cc7.png)

Scatter plot 그래프만으로는 가격이 평점에 큰 영향을 미치는것이라고 판단하기는 어려우나, 아래 Band 그래프를 통해 가격이 과도하게 높을경우 평점이 낮아지는것을 알수있었습니다.
