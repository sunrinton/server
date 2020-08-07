import requests
url="https://stdict.korean.go.kr/api/search.do"
api_key='E6D5AAE591392D05D77F18CE05B339EA'
parameters={'key':api_key,'q':'안녕'}
re=requests.get(url,parameters)
print(re.text)