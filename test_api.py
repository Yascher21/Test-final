import requests

url = "https://gigachat.devices.sberbank.ru/api/v1/models"

payload={}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 037b865f-83cb-417e-93a2-291bcb62e965'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)