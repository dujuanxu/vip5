import requests
urlstr = 'https://account.cnblogs.com/signin'
r = requests.get(url=urlstr)
# print(r.text)
# print(r.status_code)
help(r)

urlmsg = 'https://msg.cnblogs.com/'

r = requests.get(url=urlmsg)
print(r.text)