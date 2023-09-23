from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import sys
import urllib.request
import time
import re
import urllib.parse
import pymysql
import random
import hashlib
import requests

def setting():
    ###파일 저장할 폴더 가 있는지 체크하고 없다면 생성
    file_folder = './imgs'
    if not os.path.isdir(file_folder):  # 없으면 새로 생성하는 조건문
        os.mkdir(file_folder)

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='assignment3', charset='utf8')  # db설정
    cur = conn.cursor()  # DB와 데이터 주고받는 통로

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=chrome_options)
    chrome_options.add_argument(
        "User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
    browser.implicitly_wait(2)  # seconds

    duplication_post = False

    # li = big카테고리  ,   dd = small카테고리
    li = 3
    dd = 2
    browser.get('https://www.yna.co.kr/')

    return browser

if __name__ == "__main__":
    setting()