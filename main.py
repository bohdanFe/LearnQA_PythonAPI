from json.decoder import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text", verify=False)
print(response.text)
try:
    parsed_response_text = response.json()
    print(parsed_response_text)

except JSONDecodeError:
    print("Response is not a JSOn format")