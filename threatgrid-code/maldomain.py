import requests

api_key = '516s9ltift83a61kdeu37k4ri2'

url = 'https://panacea.threatgrid.com/api/v2/iocs/feeds/domains?domain=lamp.troublerifle.bid&api_key={}'.format(api_key)

r = requests.get(url)

print (r.json())
