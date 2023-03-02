import requests
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
#reponse = requests.get("https://movie.douban.com/top250", headers=headers)
reponse = requests.get("https://leetcode.cn/robots.txt", headers=headers)
#返回一个相应实体
print(reponse)
print(reponse.status_code)
print(reponse.text)