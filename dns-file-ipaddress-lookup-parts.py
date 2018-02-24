import requests as rq

resp = rq.get('http://ip-api.com/json/172.217.7.133')

print(resp.json())

js = resp.json()

print(js['status'])
print(js['org'])
print(js['isp'])
print(js['as'])
print(js['city'])
print(js['regionName'])
print(js['country'])
print(js['zip'])
