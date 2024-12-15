import requests

response = requests.post("https://playground.learnqa.ru/api/get_301", verify=False, allow_redirects=True)
first_response = response.history[0]
second_request = response

print(first_response.url)
print(second_request.url)
