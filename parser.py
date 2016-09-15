#!/bin/python3
import urllib.request
import json
import threading

url = "https://tproger.ru/wp-content/plugins/citation-widget/getQuotes.php"

req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

data = []


def get_from_server():
    threading.Timer(1.0, get_from_server).start()
    f = urllib.request.urlopen(req)
    string = f.read().decode('utf-8')
    if string not in data:
        data.append(string)
        with open('quotes.json', 'w', encoding='utf8') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=True, ensure_ascii=False)


get_from_server()
