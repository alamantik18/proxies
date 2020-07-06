#!/usr/bin/env python
# coding: utf-8
# Proxy parser
# XO490 | Telegram: https://t.me/XO490

import requests
from bs4 import BeautifulSoup

URL = "https://hidemy.name/en/proxy-list/?country=CZFRDELUNLNOPLSEGBUS&type=hs&anon=234#list"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)', 'accept': '*/*'}
massiv = ['155.138.151.112:8080', '191.232.176.187:80', '95.217.34.209:3128', '150.95.178.87:3128']


def get_html(url, params=None):
    r = requests.get(
        url=url,
        headers=HEADERS,
        params=params,
        proxies={'https': '191.232.176.187:80'})
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tbody')[0]
    trs = items.find_all('tr')
    print(len(trs))
    proxies = []
    for tr in trs:
        tds = tr.find_all('td')
        IP_Address = tds[0].text
        Port = tds[1].text
        Country_City = tds[2].text
        Speed = tds[3].text
        Type = tds[4].text
        Anonymity = tds[5].text
        proxies.append({
            'IP Address': IP_Address,
            'Port': Port,
            'Country, City': Country_City,
            'Speed': Speed,
            'Type': Type,
            'Anonymity': Anonymity
        })
    return {'proxies': proxies}


def parse():
    html = get_html(URL)
    print(html.status_code)
    print(get_content(html.text))


if __name__ == '__main__':
    parse()
