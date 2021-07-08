import requests

rating_pages = []

# https://workey.codeit.kr/ratings/index?year=2011&month=4&weekIndex=2
# response = requests.get("https://workey.codeit.kr/ratings/index")
# rating_page = response.text

# print(rating_page)



for i in range(5),:
    url = "https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex={}".format(i)
    # print(url)
    response = requests.get(url)
    rating_page = response.text
    rating_pages.append(rating_page)

print(len(rating_pages))
print(rating_pages[0])