import requests
import urllib.request
from bs4 import BeautifulSoup

URL = "https://hidemy.name/en/proxy-list/?country=CZFRDELUNLNOPLSEGBUS&type=hs&anon=234&__cf_chl_jschl_tk__=5c8a41717ecad20339c2c82ddf9c3e6704ace14d-1593769559-0-ARZE2MDxss9iy3Ys2WruR4rGSqUoDoswr7sWEJ_SuYw8hFHCHs2c5122kJxPPkGPUrqSANTrxMrrlZ9fJSqTmDusvEN5xVFLIzyYsK-DNPMbbtVcW6VZ_rGR2MJcoHFi-2BMR3Bk6_sh4bqE4PYTU9Efi9jjfRHgP2yM0SE_BE-YYe2UdXqvntvcyPEHB-nWtHEOuOl8Xsf6uWajq6bJpZWj2bTnuO5jI0Ql2rioXrAha3BtYST06rzEZ6DpP5p6L4TAIdMFOS6LQDqGr7xb7eMq3cZeUew2g5qT6mcYqui94ODLFHSej73L3wL5IVmkmdo3e9Z6UmYjoXgZsa8nIllsrcAukrypE2FG2QLwyWnJ#list"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)', 'accept': '*/*'}
massiv = ['155.138.151.112:8080', '191.232.176.187:80', '95.217.34.209:3128', '150.95.178.87:3128']

def get_html(url, params=None):
    r = requests.get(url, headers = HEADERS, params=params, proxies = {'https' : '150.95.178.87:3128'})
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tbody')[0]
    trs = items.find_all('tr')
    print(len(trs))
    proxies = {}
    for tr in trs:
        tds = tr.find_all('td')
        IP_Address = tds[0].text
        Port =  tds[1].text
        Country_City = tds[2].text
        Speed = tds[3].text
        Type = tds[4].text
        Anonymity = tds[5].text
        proxies.update({
            'IP Address': IP_Address,
            'Port':  Port,
            'Country, City': Country_City,
            'Speed': Speed,
            'Type': Type,
            'Anonymity': Anonymity
        })
        continue
    return proxies

def parse():
    html = get_html(URL)
    print(html.status_code)
    print(get_content(html.text))

if __name__ == '__main__':
    parse()