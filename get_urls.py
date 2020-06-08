import urllib.request
import re

url = "http://www.cnii.com.cn/wlkb/rmydb/node_31032.htm"

pattern1 = '<.*?(href="*.*?").*?'

headers = {'User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read().decode('utf8')

content_href = re.findall(pattern1,data,re.I)


set1 = set(content_href)


file_new = "D:\\href.txt"
with open(file_new,'w') as f:
    for i in set1:
        f.write(i)
        f.write("\n")
# f.close()
