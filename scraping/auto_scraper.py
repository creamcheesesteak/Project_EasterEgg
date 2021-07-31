# Appannie 용 스크래퍼
# 작동을 위해서는 사전에 로그인 값과 스크래핑할 데이터 정보 입력 필요
# 스크래퍼 작동을 위해 다른 창은 내려 주시고, 작동 동안 컴퓨터 활용이 불가능함을 알림
# 팝업화면이 top에 위치 & 페이지크기 full & 화면배울 100% 기준
# 시작부터 .xls 저장까지 한 사이클 4:15분 소요

# 이용 라이브러리
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

# 함수 정의부
def settings(browser, yours):
    browser.get('https://www.appannie.com/account/login')
    browser.maximize_window()
    browser.find_element_by_name("username").send_keys(yours[0])
    browser.find_element_by_xpath("//input[@type='password']").send_keys(yours[1])
    browser.find_element_by_xpath("//button[@type='submit']").click()
    return
# browser.get('https://www.appannie.com/dashboard/home')

def trial(browser, loot):
    time.sleep(2)
    wait = WebDriverWait(browser, 7)

    browser.get('https://www.appannie.com/intelligence/top-apps/store-rank/gp?store-rank.gp.view=free')

    place = browser.find_element_by_xpath(
        "//input[@aria-activedescendant='react-select-SingleCountryPicker--store_rank_release_time_as_date_capacity--value']")
    place.send_keys('spain')  # 국가명 입력
    place.send_keys(Keys.RETURN)
    browser.execute_script("window.scrollTo(0, 800)")
    time.sleep(2)
    browser.find_element_by_css_selector(
        'div.flexview__FlexView-sc-15q74yn-0.TableHeader__TableRow-sc-137foek-2.TableHeader__StickyTableRow-sc-137foek-3.ftNqTk.TableHead_Row.TableHead_StickyTableRow.FlexView > div:nth-child(1) > div > div > label > div > svg').click()
    browser.execute_script("window.scrollTo(0, 890)")

    contents = []
    # 1 ~ 11 순위까지
    for i in range(1, 5):
        gui.moveTo(490, 236, 0.4)
        gui.dragTo(1080, 295, 0.8, button='left')
        gui.hotkey('ctrl', 'c')
        a = pyperclip.paste()
        gui.click()
        gui.scroll(-60)
        list = a.split('\r')
        list = [i.strip('\n') for i in list]
        if len(list) == 3:
            list.insert(2, '없음')
            contents.append(list)
            continue
        elif list[-1] == '':
            del list[-1]
            list.insert(2, '없음')
            continue
        elif len(list) == 4:
            contents.append(list)
            continue

    # 드래그시 열의 마지막 str에서 긴 (Application) 의 경우 1~2문자의 누락가능성 확인 -> 조정하기위한 for문
    for content in contents:
        if content[-1][-1] == 'n':
            content[-1] = content[-1] + 's)'
        elif content[-1][-1] == 'o':
            content[-1] = content[-1] + 'ns)'
        elif content[-1][-1] == 's':
            if (content[-1] == 'Games') or (content[-1] == 'Kids'):
                break
            else:
                content[-1] = content[-1] + ')'

    df = pd.DataFrame(data=contents)
    df = df.drop(columns=[0])
    # df.index = df.index + 1
    # 회사명 中 None 은 '없음' 으로 본다

    # 데이터에 맞는 이름으로 엑셀 생성 Ex. '시장_국가명_무료/유료'
    file = '.xls'
    name = loot + 'gp_f' + '_' + 'spain' + file
    df.to_excel(name, header=None,index=False)

    if len(contents) == '9' or '10':
        print('기존 테스트 창을 닫고 본세트를 진행하세요')
        print('테스트파일', name, '삭제필요')
    else:
        print('문제가 있네요. trial 함수의 gui.moveTo, gui.dragTo 의 괄호에서 0.4, 0.8을 1로 변경해보시거나, 제게 물어봐주세요')
    sd.Beep(2000, 500)
    return browser.quit()

def operation_gp(browser, data, data1, nation, loot):
    time.sleep(2)
    wait = WebDriverWait(browser, 7)

    browser.get(data)

    place = browser.find_element_by_xpath(
        "//input[@aria-activedescendant='react-select-SingleCountryPicker--store_rank_release_time_as_date_capacity--value']")
    place.send_keys(nation)  # 국가명 입력
    place.send_keys(Keys.RETURN)
    browser.execute_script("window.scrollTo(0, 800)")
    time.sleep(2)
    browser.find_element_by_css_selector(
        'div.flexview__FlexView-sc-15q74yn-0.TableHeader__TableRow-sc-137foek-2.TableHeader__StickyTableRow-sc-137foek-3.ftNqTk.TableHead_Row.TableHead_StickyTableRow.FlexView > div:nth-child(1) > div > div > label > div > svg').click()
    browser.execute_script("window.scrollTo(0, 890)")

    contents = []
    # 1 ~ 91 순위까지
    for i in range(1, 92):
        gui.moveTo(490, 236, 0.4)
        gui.dragTo(1080, 295, 0.8, button='left')
        gui.hotkey('ctrl', 'c')
        a = pyperclip.paste()
        gui.click()
        gui.scroll(-60)
        list = a.split('\r')
        list = [i.strip('\n') for i in list]
        if len(list) == 3:
            list.insert(2, '없음')
            contents.append(list)
            continue
        elif list[-1] == '':
            del list[-1]
            list.insert(2, '없음')
            continue
        elif len(list) == 4:
            contents.append(list)
            continue

    # 92 ~ 100 순위 까지 (마지막은 스크롤을 내릴 수 없어서 따로 for문 작성)
    for i in range(1, 10):
        n = 75 * (i - 1)
        gui.moveTo(490, 236 + int(n), 0.5)
        gui.dragTo(1080, 285 + int(n), 1, button='left')
        gui.hotkey('ctrl', 'c')
        a = pyperclip.paste()
        gui.click()
        list = a.split('\r')
        list = [i.strip('\n') for i in list]
        if len(list) == 3:
            list.insert(2, '없음')
            contents.append(list)
            continue
        elif list[-1] == '':
            del list[-1]
            list.insert(2, '없음')
            continue
        elif len(list) == 4:
            contents.append(list)
            continue

    # 드래그시 열의 마지막 str에서 긴 (Application) 의 경우 1~2문자의 누락가능성 확인 -> 조정하기위한 for문
    for content in contents:
        if content[-1][-1] == 'n':
            content[-1] = content[-1] + 's)'
        elif content[-1][-1] == 'o':
            content[-1] = content[-1] + 'ns)'
        elif content[-1][-1] == 's':
            if (content[-1] == 'Games') or (content[-1] == 'Kids'):
                break
            else:
                content[-1] = content[-1] + ')'

    for content in contents:
        if content[-1][-1] == 'n':
            content[-1] = content[-1] + 's)'

    for content in contents:
        if content[-1][-1] == 'o':
            content[-1] = content[-1] + 'ns)'

    df = pd.DataFrame(data=contents)
    df = df.drop(columns=[0])
    # 회사명 中 None 은 '없음' 으로 본다

    # 데이터에 맞는 이름으로 엑셀 생성 Ex. '시장_국가명_무료/유료'
    file = '.xls'
    name = loot + data1 + '_' + nation + file
    df.to_excel(name, header=None, index=False)
    return

def operation_ios(browser, data, data1, nation, loot):
    time.sleep(2)
    wait = WebDriverWait(browser, 7)

    browser.get(data)

    place = browser.find_element_by_xpath(
        "//input[@aria-activedescendant='react-select-SingleCountryPicker--store_rank_release_time_as_date_capacity--value']")
    place.send_keys(nation)  # 국가명 입력
    place.send_keys(Keys.RETURN)
    browser.execute_script("window.scrollTo(0, 800)")
    time.sleep(2)
    browser.find_element_by_css_selector(
        'div.flexview__FlexView-sc-15q74yn-0.TableHeader__TableRow-sc-137foek-2.TableHeader__StickyTableRow-sc-137foek-3.ftNqTk.TableHead_Row.TableHead_StickyTableRow.FlexView > div:nth-child(1) > div > div > label > div > svg').click()
    browser.execute_script("window.scrollTo(0, 890)")

    contents = []
    # 1 ~ 91 순위까지
    for i in range(1, 92):
        gui.moveTo(490, 236, 0.4)
        gui.dragTo(1173, 280, 0.8, button='left')
        gui.hotkey('ctrl', 'c')
        a = pyperclip.paste()
        gui.click()
        gui.scroll(-60)
        list = a.split('\r')
        list = [i.strip('\n') for i in list]
        if len(list) == 3:
            list.insert(2, '없음')
            contents.append(list)
            continue
        elif list[-1] == '':
            del list[-1]
            list.insert(2, '없음')
            continue
        elif len(list) == 4:
            contents.append(list)
            continue

    # 92 ~ 100 순위 까지 (마지막은 스크롤을 내릴 수 없어서 따로 for문 작성)
    for i in range(1, 10):
        n = 75 * (i - 1)
        gui.moveTo(490, 236 + int(n), 0.5)
        gui.dragTo(1173, 280 + int(n), 1, button='left')
        gui.hotkey('ctrl', 'c')
        a = pyperclip.paste()
        gui.click()
        list = a.split('\r')
        list = [i.strip('\n') for i in list]
        if len(list) == 3:
            list.insert(2, '없음')
            contents.append(list)
            continue
        elif list[-1] == '':
            del list[-1]
            list.insert(2, '없음')
            continue
        elif len(list) == 4:
            contents.append(list)
            continue

    # 드래그시 열의 마지막 str에서 긴 (Application) 의 경우 1~2문자의 누락가능성 확인 -> 조정하기위한 for문
    for content in contents:
        if content[-1][-1] == 'n':
            content[-1] = content[-1] + 's)'
        elif content[-1][-1] == 'o':
            content[-1] = content[-1] + 'ns)'
        elif content[-1][-1] == 's':
            if (content[-1] == 'Games') or (content[-1] == 'Kids'):
                break
            else:
                content[-1] = content[-1] + ')'

    for content in contents:
        if content[-1][-1] == 'n':
            content[-1] = content[-1] + 's)'

    for content in contents:
        if content[-1][-1] == 'o':
            content[-1] = content[-1] + 'ns)'

    df = pd.DataFrame(data=contents)
    df = df.drop(columns=[0])
    # 회사명 中 None 은 '없음' 으로 본다

    # 데이터에 맞는 이름으로 엑셀 생성 Ex. '시장_국가명_무료/유료'
    file = '.xls'
    name = loot + data1 + '_' + nation + file
    df.to_excel(name, header=None, index=False)
    return