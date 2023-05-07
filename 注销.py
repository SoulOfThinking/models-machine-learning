import requests

url = "http://10.10.10.253/cgi-bin/srun_portal?callback=jQuery666&action=logout&ac_id=1&ip=10.0.9.14&username=180170415&_=1607515717022"


header = {
    "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "lang=zh-CN; PHPSESSID_8800=8makdq9tccnueje9vsu32955p4; _csrf=ed0a2843dadf0d23f9246acc18d9686ac112b6f16df897ca9c87fe35b20ee844a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22w19qaDNPEdhlz_6Uf8nijWYQSFFBkQff%22%3B%7D",
    "Host": "10.10.10.253",
    "Referer": "http://10.10.10.253/srun_portal_success?ac_id=1&theme=basic1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52",
    "X-Requested-With": "XMLHttpRequest"
}

response2 = requests.get(url,  headers=header).status_code;
print(format(response2))
