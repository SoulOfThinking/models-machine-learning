import requests    # 用于向目标网站发送请求
import json
import time
import re
from encryption.srun_md5 import *
from encryption.srun_sha1 import *
from encryption.srun_base64 import *
from encryption.srun_xencode import *

# -*- coding: utf-8 -*-

# url = 'http://172.20.5.18/cgi-bin/srun_portal?callback=jQuery11240333091354053173_1681908068298&action=login&username=L202300035&password=%7BMD5%7D0d49df31c4f84d40f59aadec80b9ef24&ac_id=9&ip=10.24.5.235&chksum=d3f13a4f53748f6f6240a59952fdbfa66c2fbbf5&info=%7BSRBX1%7DmHHxVojgxqwOyW6BX5y0zCrwMl1jjNOQrDM08RYvxJLMqONgCaVXQFxxzF6JPtd0GXvhH6%2F8GmsBsxmjjC%2FbbdMdmSGtG%2Bv0Ls5dQNBanrTkay0Cr0Qe%2F5bDikFE7WUnPwcJlroYSiLXc2DU&n=200&type=1&os=Windows+10&name=Windows&double_stack=0&_=1681908068301'    # 这行是你需要根据自己的情况修改的地方

# url1 = 'http://172.20.5.18/cgi-bin/get_challenge?callback=jQuery11240333091354053173_1681908068294&username=L202300035&ip=10.24.5.235&_=1681908068301'
# url2 = 'http://172.20.5.18/cgi-bin/srun_portal?callback=jQuery11240333091354053173_1681908068294&action=login&username=L202300035&password=%7BMD5%7D0d49df31c4f84d40f59aadec80b9ef24&ac_id=9&ip=10.24.5.235&chksum=d3f13a4f53748f6f6240a59952fdbfa66c2fbbf5&info=%7BSRBX1%7DmHHxVojgxqwOyW6BX5y0zCrwMl1jjNOQrDM08RYvxJLMqONgCaVXQFxxzF6JPtd0GXvhH6%2F8GmsBsxmjjC%2FbbdMdmSGtG%2Bv0Ls5dQNBanrTkay0Cr0Qe%2F5bDikFE7WUnPwcJlroYSiLXc2DU&n=200&type=1&os=Windows+10&name=Windows&double_stack=0&_=1681908068302'
# username = 'L202300035'
#
# back = 'jQuery11240333091354053173_1681908068294({"challenge":"e522f9f968e37ffbfe33cae5719ae26f8f7c0d0ef9512554c92c2034c1412481","client_ip":"10.24.5.235","ecode":0,"error":"ok","error_msg":"","expire":"38","online_ip":"10.24.5.235","res":"ok","srun_ver":"SRunCGIAuthIntfSvr V1.18 B20181113","st":1681956386})'
# u = url + username
# print(u)
# # x = requests.get(url)
# #print(x.text)
# #info = x.text
# #info = info[41:-1]
# back = back[41:-1]
# d = json.loads(back)
# print(d)
# print(d['challenge'])
# u = '5c237d6a4bc08aeb3121903254955f08f1f1a408ad80219f24be0d68fae743e2'
# e = '1075221d409e481052fa5d1762e7b15640626bea'
# print(len(u))


#print(type(x.text))
# response = requests.get(url).status_code  # 直接利用 GET 方式请求这个 URL 同时获取状态码
# print("状态码{}".format(response))  # 打印状态码





