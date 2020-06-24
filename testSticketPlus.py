import time, requests

url = '/overlay/sticker/16897/293948094/iPhone/sticker.png?text=%E6%88%91%E8%82%9A%E5%AD%90%E9%A4%93%E4%BA%86!233666ttt111&timestamp=' + str(int(time.time() * 1000))
headers = {
    'authority': 'store.line.me', #req
    'method': 'GET', #req
    'path': url, #req
    'scheme': 'https', #req
    'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-TW,zh;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://store.line.me/stickershop/product/16897/zh-Hant?ref=Chrome',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}


res = requests.get('https://store.line.me' + url, headers = headers)

print(res) #if status_code is 404 -> auth fail, 200 -> ok!