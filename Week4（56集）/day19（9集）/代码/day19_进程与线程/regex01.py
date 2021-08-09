import re

# 默认是贪婪的,如果想将贪婪模式变成非贪婪模式
msg = 'abc123abc'

result = re.match(r'abc(\d+?)', msg)

print(result)

path = '<img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=30a7526a9282d158bb8259b9b00b19d5/704bde177f3e67092893917b35c79f3dfadc55f5.jpg" size="2227636" changedsize="true" width="560" height="840" style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;">'

result = re.match(r'<img class="BDE_Image" src="(.*?)"', path)
# print(result.group(1))
image_path = result.group(1)
import requests

response = requests.get(image_path)

with open('aa.jpg', 'wb') as wstream:
    wstream.write(response.content)
