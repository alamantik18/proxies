import requests
import json
from bs4 import BeautifulSoup
import cheker

URL = "https://hidemy.name/en/proxy-list/?country=CZFRDELUNLNOPLSEGBUS&type=hs&anon=234#list"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)', 'accept': '*/*'}
massiv_of_proxies = ['155.138.151.112:8080', '191.232.176.187:80', '95.217.34.209:3128', '150.95.178.87:3128', '207.148.19.52:8080']

def get_html(url, params=None):
    r = requests.get(url,
                     headers = HEADERS,
                     params=params,
                     proxies = {'https' : '207.148.19.52:8080'})
    return r

def pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('div', class_='pagination')[0]
    pagination_list = pagination.find_all('li')
    pagination_href_list = 0
    for i in range(0, len(pagination_list)-1):
        pagination_list = pagination.find_all('li')[i]
        pagination_href_list = int(pagination_list.find('a').get_text())
    if pagination_href_list:
        return pagination_href_list
    else:
        return 1

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tbody')[0]
    trs = items.find_all('tr')
    proxies = []
    for tr in trs:
        tds = tr.find_all('td')
        IP_Address = tds[0].text
        Port =  tds[1].text
        Country_City = tds[2].text
        Speed = tds[3].text
        Type = tds[4].text
        Anonymity = tds[5].text
        proxies.append({'IP Address': IP_Address,
                        'Port':  Port,
                        'Country, City': Country_City,
                        'Speed': Speed,
                        'Type': Type,
                        'Anonymity': Anonymity})
    return {'proxies':proxies}

def save_unchecked_proxies(massiv_of_proxies):
    with open('proxy_uncheck.json', 'w') as file:
        json.dump(massiv_of_proxies, file, indent=4)

def parse():
    html = get_html(URL)
    print(html.status_code)
    proxies = get_content(html.text)
    print(proxies)
    massiv_of_proxies_for_check = []
    for i in range(0, len(proxies.get('proxies'))):
        massiv_of_proxies_for_check.append(proxies.get('proxies')[i].get('IP Address') + ':' + proxies.get('proxies')[i].get('Port'))
    print(massiv_of_proxies_for_check)
    save_unchecked_proxies(proxies)
    return massiv_of_proxies_for_check

if __name__ == '__main__':
    cheker.main()
    parse()