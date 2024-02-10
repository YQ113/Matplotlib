#爬蟲抓取 PTT 電影版的網頁原始碼(HTML)
import urllib.request as req

url="https://www.ptt.cc/bbs/movie/index.html"
#建立一個Request物件,附加 Request Header 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
})    

with req.urlopen(request) as respons:
    data=respons.read().decode("utf-8")
print(data)