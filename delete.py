import requests
url = 'https://superestet.ru/'
payload  = {'method': 'getQuote', 'format': 'json', 'lang': 'ru'}
res = requests.delete(url, params=payload)
print('url ',res.url)
print('Код состояния ',res.status_code)
print('Заголовки ответа ',res.headers)
print('Содержимое ответа ',res.text)
print('Содержимое ответа ',res.content)
