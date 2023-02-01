import requests
sku = 'nintendo+switch'
url = f"https://www.amazon.fr/S?k={sku}&dataVersion=v0.1&cid=34e221e4bbc90f0b74ef485250396f3e1ff0d5600fb507ddededc9f16d2b7036&format=json"
headers = {
    "Host": "www.amazon.fr",
    "Cookie": "",
    "Cache-Control": "max-age=0",
    "Device-Memory": "8",
    "Sec-Ch-Device-Memory": "8",
    "Dpr": "1",
    "Sec-Ch-Dpr": "1",
    "Viewport-Width": "1920",
    "Sec-Ch-Viewport-Width": "1920",
    "Rtt": "100",
    "Downlink": "1.35",
    "Ect": "4g",
    "Sec-Ch-Ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers=headers)
print(response.text)