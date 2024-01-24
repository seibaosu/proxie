import urllib.request , socket
socket.setdefaulttimeout(10)

def is_bad_proxy(proxy):
    try:

        text = proxy.split(':')

        proxy_handler = urllib.request.ProxyHandler({
            'http': proxy
        })

        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlopen('http://ip-api.com/json/' + text[0])

    except urllib.error.HTTPError as e:
        return e.code
    except Exception as detail:
        return 1
    return 0

proxie = open('proxy.txt', 'r').read().strip().split('\n')
for item in proxie:
    if is_bad_proxy(item):
        print(f'[DIED] {item}')
    else:
        print(f'[LIVE] {item}')