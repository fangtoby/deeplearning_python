"""
python3从chrome浏览器读取cookie
get cookie from chrome
2016年5月26日 19:50:38 codegay

参考资料：

python模拟发送动弹
http://www.oschina.net/code/snippet_209614_21944

用Python进行SQLite数据库操作
http://www.cnblogs.com/yuxc/archive/2011/08/18/2143606.html

encrypted_value解密脚本
http://www.ftium4.com/chrome-cookies-encrypted-value-python.html

利用cookie劫持微博私信
https://segmentfault.com/a/1190000002569850

你所不知道的HostOnly Cookie
https://imququ.com/post/host-only-cookie.html
"""
import os
import sqlite3
import requests
from win32.win32crypt import CryptUnprotectData

def getcookiefromchrome(host='.oschina.net'):
    cookiepath=os.environ['LOCALAPPDATA']+r"\Google\Chrome\User Data\Default\Cookies"
    sql="select host_key,name,encrypted_value from cookies where host_key='%s'" % host
    with sqlite3.connect(cookiepath) as conn:
        cu=conn.cursor()        
        cookies={name:CryptUnprotectData(encrypted_value)[1].decode() for host_key,name,encrypted_value in cu.execute(sql).fetchall()}
        print(cookies)
        return cookies

#运行环境windows 2012 server python3.4 x64 chrome 50
#以下是测试代码
#getcookiefromchrome()
#getcookiefromchrome('.baidu.com')

url='http://my.oschina.net/'

httphead={'User-Agent':'Safari/537.36',}

#设置allow_redirects为真，访问http://my.oschina.net/ 可以跟随跳转到个人空间
r=requests.get(url,headers=httphead,cookies=getcookiefromchrome('.oschina.net'),allow_redirects=1)
print(r.text)