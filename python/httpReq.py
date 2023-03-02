#request是一个三方库：pip3 install requests
import requests
reponse = requests.get("http://books.toscrape.com/")
with open("httpReq.txt", "w", encoding="UTF-8") as f:
    if reponse.ok:
        # print(reponse.text)
        f.write(reponse.text)
    else:
        # print("request failed.")
        f.write("request failed.\n")