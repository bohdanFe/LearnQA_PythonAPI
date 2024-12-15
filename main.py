import requests

response = requests.post("https://playground.learnqa.ru/api/check_type", verify=False, data={"params1":"value1"})
print(response.text)