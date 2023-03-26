# coding=utf-8
import json

import requests
import pycorrector

# s = requests.Session()
# login_data = {'username': 'teacher', 'password': 'teacher'}
# 方法1
# resp1 = s.post('http://192.168.2.132/login/', data=login_data)
# r = s.get('http://192.168.2.132/personal_live/')

# 方法2
# resp1 = requests.post('http://192.168.2.132/login/', data=login_data)
# print('cookie:' + str(resp1.cookies))
# r = requests.get('http://192.168.2.132/personal_live/', cookies=resp1.cookies)

# 方法3
# c = {'sessionid': '3ps7ouyox1l43alcb7rafxg9dtfnurcb'}
# r = requests.get('http://192.168.2.132/personal_live/', cookies=c)
from bs4 import BeautifulSoup

from service.shortNews import *
from service.shortNews2 import get_summary, get_key_words
from pycorrector import Corrector

c = {
    '.CNBlogsCookie': 'D020D...07',
    '.Cnblogs.AspNetCore.Cookies': 'CfDJ...WA',
    'SyntaxHighlighter': 'java',
    'SERVERID': '560...34'

}


def get_corrected_sent(text):
    pycorrector.set_log_level('error')
    model = Corrector(language_model_path="/Users/huan/Documents/zh_giga.no_cna_cmn.prune01244.klm")
    corrected_sent, detail = model.correct(text)
    return corrected_sent


def getDocByUrl(url):
    r = requests.get(url)
    resp = r.text
    return resp


# author_type=1 大V  author_type=3 机构
def generateShortNews(author_type, title_perf):
    resp = getDocByUrl(
        'https://www.yicai.com/api/ajax/getauthorlist?keys=authorsbyType&type=' + author_type.__str__() + '&pagesize=10&page=1')
    respArr = json.loads(resp)
    sizeofList = len(respArr)
    for i in range(sizeofList):
        item = respArr[i]
        # print(item['url'])
        if item['url'].find("news") == -1:
            continue
        print("财经提要：" + (i + 1).__str__())
        print("\r\n")
        print(item['NewsTitle'])
        print("\r\n")

        sub_url = 'https://www.yicai.com' + item['url']
        sub_resp = getDocByUrl(sub_url)
        # 解析 HTML
        soup = BeautifulSoup(sub_resp, "html.parser")

        # 提取文本内容
        filtered_text = soup.text
        if len(filtered_text) < 800:
            continue
        # summary=generate_summary(filtered_text,3)
        # summary=get_key_words(filtered_text,3)
        sp = 2
        summary = get_summary(filtered_text, sp)
        for sp_i in range(sp):
            corrected_sent = get_corrected_sent(summary[sp_i])
            print(corrected_sent)
        print("\r\n")


print("\r\n")
print("\r\n")
generateShortNews(1, "大V")
print("\r\n")
print("\r\n")
