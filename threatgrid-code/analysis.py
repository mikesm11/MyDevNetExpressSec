import requests
import json
import sys

api_key = '516s9ltift83a61kdeu37k4ri2'

sample_id = 'a3ff96c23f6d8baaf47720b5c388f9b9'

url = 'https://panacea.threatgrid.com/api/v2/samples/{}/analysis.json?api_key={}'.format(sample_id, api_key)

try:
    r = requests.get(url)
    #(r.json())
    status_code = r.status_code
    resp = r.text
    if (status_code == 200):
        json_resp = json.loads(resp)
        resp2=json.dumps(json_resp,sort_keys=True,indent=4, separators=(',', ': '))
        print(resp2)
        fh = open("result-step5.txt", "w")
        fh.write(resp2)
        fh.close()
    else:
        r.raise_for_status()
        print("Error occured in GET --> "+resp)
except requests.exceptions.HTTPError as err:
    print("Error in connection --> "+str(err))
finally:
    if r : r.close()
