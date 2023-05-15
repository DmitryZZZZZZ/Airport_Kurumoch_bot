from bs4 import BeautifulSoup
import requests
import time
import lxml


def arrived():
    base = 'https://www.kuf.aero/board/?type=arr&ready=yes'
    html = requests.get(base).content
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find('div', class_='table-flex__body').find_all('a')
    list_ = []
    for s in div:
        text = s.get_text(' ', strip=True)
        list_.append(text)
        result_arrived = '\n'.join(list_)
    return result_arrived


def not_arrived():
    base = 'https://www.kuf.aero/board/?type=arr'
    html = requests.get(base).content
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find('div', class_='table-flex__body').find_all('a')
    list_ = []
    for r in div:
        text = r.get_text(' ', strip=True)
        list_.append(text)
        result_not_arrived = '\n'.join(list_)
    return result_not_arrived


course()

