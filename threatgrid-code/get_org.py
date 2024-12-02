import requests

api_key = '516s9ltift83a61kdeu37k4ri2'

url = 'https://panacea.threatgrid.com/api/v2/search/submissions?term=behavior&q=Process Modified a File in a System Directory&before=2018-08-07T12:30:00Z&after=2018-08-07T12:15:00Z&api_key={}'.format(api_key)

r = requests.get(url)
print (r.json())
