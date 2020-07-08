import urllib.request
import socket
import urllib.error
import parse_code
import json

def is_bad_proxy(pip):
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('http://www.example.com')
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        print("ERROR:", detail)
        return True
    return False

def main():
    socket.setdefaulttimeout(120)
    working_proxies = []
    for currentProxy in parse_code.parse():
        if is_bad_proxy(currentProxy):
            print("Bad Proxy %s" % (currentProxy))
        else:
            print("%s is working" % (currentProxy))
            working_proxies.append(currentProxy)
    save_checked_proxies({'working proxies':working_proxies})

def save_checked_proxies(proxies):
    with open('proxy_checked.json', 'w') as file:
        json.dump(proxies, file, indent=4)

if __name__ == '__main__':
    main()