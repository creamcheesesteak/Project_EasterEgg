# 스크래퍼 설명 : 웹 스크래핑을 할 때, bs4은 정적 텍스트 분석을 하기 때문에 속도가 매우 빠릅니다.
# 이 때, selenium은 단지 의도한 웹페이지로 이동하는 수단으로만 활용됩니다. 하지만, Appannie 홈페이지는 일반 bs4를 이용한
# 웹 스크래핑이 거의 불가능하게 설정되어있어 여기서는 selenium만을 이용하였습니다. selenium은 실제 브라우저를
# 사용하는 동적 툴이라서 bs4보다 속도가 매우 느리다는 단점이 있지만, 우리조에 주제에 최적화된 정보를 Appannie에서 온전히
# 구할 수 있기 때문에 이를 이용한 스크래퍼를 만들게 되었습니다.

# 스크래퍼 작동시 유의사항
# Appannie : 'https://www.appannie.com/en/' 에 회원가입을 한다. 이때, 회사계정을 요구하는데 @naver.com으로 가입하면 무관함
# 스크래퍼 작동을 위해서는 로그인 값, 데이터 저장경로, 스크래핑할 데이터 정보를 입력하고 국가의 범위를 설정해주여야함
# 스크래퍼 작동을 위해 다른 창을 하단에 축소시키거나 내려주고, 작동 동안 컴퓨터 활용이 불가능함을 알림(마우스이동 금지)
# 팝업화면이 선택된 상태에서 Top에 위치 & 페이지크기 Full & 화면배율 100% 기준
# 시작부터 한 세트의 수집시간은 4분 내외로 소요되며, 점심시간이나 컴퓨터를 사용하지 않을 때 시간을 고려하여 작동시킬 국가 범위를 설정 하는 것이 현명
# 본 스크래퍼를 돌리기 전에 정상적으로 작동하는지 시험운행(함수)를 필수로 적용한 후 본세트를 돌릴 것
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time
import pyautogui as gui # 마우스 이동, 키보드 입력
import pyperclip # 클립보드 사용
import winsound as sd # 알림음
from auto_scraper import settings, trial, operation_gp, operation_ios

# 국가 리스트 정의 : intersection of ios market and google play store
total_nations = ['Algeria', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Belarus', 'Belgium', 'Bolivia',
           'Bosnia and Herzegovina', 'Brazil', 'Bulgaria', 'Cambodia', 'Chile', 'Colombia', 'Costa Rica', 'Croatia', 'Czech Republic',
           'Denmark', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Finland', 'France', 'Germany', 'Ghana', 'Greece',
           'Guatemala', 'Honduras', 'Hong Kong', 'Hungary', 'India', 'Indonesia', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan',
           'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyzstan', 'Latvia', 'Lebanon', 'Lithuania', 'Luxembourg', 'Macau', 'Malaysia', 'Mexico',
           'Moldova', 'Morocco', 'Nepal', 'Netherlands', 'New Zealand', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Paraguay',
           'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Saudi Arabia', 'Serbia', 'Singapore', 'Slovakia',
           'Slovenia', 'South Africa', 'South Korea', 'Spain', 'Sri Lanka', 'Sweden', 'Switzerland', 'Taiwan', 'Tanzania', 'Thailand',
           'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uruguay', 'Uzbekistan', 'Venezuela',
           'Vietnam', 'Yemen'] # list : 98
# 우선순위 40개국 선정 # list : 40
nations = ['Australia', 'Austria', 'Belgium', 'Brazil', 'Chile', 'Croatia', 'Czech Republic',
           'Finland', 'France', 'Germany', 'Egypt', 'Greece', 'Hong Kong', 'Hungary', 'India',
           'Indonesia', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Japan', 'Malaysia', 'Mexico',
           'Netherlands', 'New Zealand', 'Philippines', 'Poland', 'Portugal', 'Russia',
           'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Turkey',
           'Ukraine', 'United Kingdom', 'Uruguay', 'Vietnam']

# 링크 정의
i_f = 'https://www.appannie.com/intelligence/top-apps/store-rank/ios?store-rank.ios.view=free'
i_p = 'https://www.appannie.com/intelligence/top-apps/store-rank/ios?store-rank.ios.view=paid'
gp_f = 'https://www.appannie.com/intelligence/top-apps/store-rank/gp?store-rank.gp.view=free'
gp_p = 'https://www.appannie.com/intelligence/top-apps/store-rank/gp?store-rank.gp.view=paid'

# 아래의 내용은 꼭 입력해주어야함
# 로그인 데이터 yours = ['아이디', '비밀번호']  Ex.['abc@naver.com', 'qwe']
yours = ['####@###.###', '######']
# 목표 스크래핑 카테고리 설정 : ios/google play store - free/paid 로 조사할 시장을 설정해야함.
# i_p 는 ios_paid로 돌리겠다는 의미 data, data1 내용 동일하게 작성 다만, data1은 '##' 안에 입력할 것
data = i_f
data1 = 'i_f'
# 저장경로와 형식 설정 Ex.loot = 'C:/pl/scraping/', 지금은 파일형식 '.xls'로 고정
loot = 'C:/Users/###/###/###'
# 설정된 데이터는 data1 + '_' + nation + file 의 이름으로 저장됨 Ex.'시장_무료/유료_국가명_' = [gp_f_Austria.csv]
# 데이터가 개별로 저장되기 때문에 DB저장시나 데이터 선별시 for문을 통한 자동코드 작성추천
# 시험세트(0) 실행후 정상작동을 확인하고 본세트인(1,2)로 설정 하여 run 필요. 이때, 구글플레이는 '1'을 애플스토어는 '2'를 입력할 것
set = '0'
# 추출할 나라 길이 정하기 Ex. nations[:10] 9개국
nations = nations[1:17]

# ------------------------------r u n --------------------------------- #

browser = webdriver.Chrome('C:\chromedriver.exe')
html = browser.page_source
BeautifulSoup(html, 'html.parser')
# 실행문
if set == '0':
    settings(browser, yours)
    trial(browser, loot)  # 종료시 버저가 울립니다. 그러면 run table in python에서 출력된 내용을 읽어주세요.
elif set == '1':
    settings(browser, yours)
    for nation in nations:
        operation_gp(browser, data, data1, nation, loot)
elif set == '2':
    settings(browser, yours)
    for nation in nations:
        operation_ios(browser, data, data1, nation, loot)

sd.Beep(2000, 1000)
browser.quit()
# 로그인, 세팅
# settings(browser, yours)

