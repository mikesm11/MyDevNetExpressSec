import requests

api_key = '516s9ltift83a61kdeu37k4ri2'

SHA256 = '3b0fa8068f11dc9abf3a4017920ec16303f99999e7276678f19c6b4eecf65287'

url = 'https://panacea.threatgrid.com/api/v2/samples?sha256={}&api_key={}'.format(SHA256, api_key)

r = requests.get(url)
print (r.json())
