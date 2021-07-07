import requests

response = requests.get("https://workey.codeit.kr/ratings/index")
print(response.text)