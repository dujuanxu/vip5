# session关联接口
# 一般登录后，还会有其它的操作，如发帖，评论等，这时候如何保持会话呢
import requests

urlstr = 'https://www.wanandroid.com/user/login'
header = {'User-Agent':'Mozilla/6.0'}
payload = {'username':'moon_du', 'password':'dujuanxu'}

# r = requests.post(url=urlstr, data=payload, headers=header)
# print(r.text)
# print(r.headers)

s = requests.session()
r = s.post(url=urlstr, data=payload, headers=header)
r = s.post(url=urlstr, data=payload)


r2 = s.get('https://www.wanandroid.com/user/lg/index')

print("********", r2.text)
print(r2.encoding)
# print("**", r.ok)

