import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/"

querystring = {"count":"6"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "e9101501-439f-7cc7-75f7-5538884ea29c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
deck = response.json()
deck_id = deck['deck_id']
print(deck_id)
