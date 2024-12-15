import requests

payload = {"name":"User"}
response = requests.get("https://playground.learnqa.ru/api/hello", verify=False, params=payload)

print(response.text)