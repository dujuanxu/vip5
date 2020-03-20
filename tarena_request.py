import requests

urlstr = 'http://guess2.win007.com/users/login.aspx'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
          'Cookie': 'ASP.NET_SessionId=heizwwiolphdma0ajg3v42k2',
          'Origin': 'http://users.win007.com'}

payload = {"g":0, "UserName":"moon_du", "Password":"dujuan1234"}

r = requests.post(url=urlstr, data=payload, headers=header)
r.encoding = "utf-8"
# html = r.text.encode('iso-8859-1').decode('utf-8')
print(r.text)
