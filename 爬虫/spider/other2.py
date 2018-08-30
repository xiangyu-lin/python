import spider
import printl
html = spider.getUrl('http://huaban.com/boards/41308552/')
html = html.read().decode('utf-8')




import re
'''
html = re.findall('/pins/\d*',html)
j = []
for i in html:
    j.append('http://huaban.com' + i)
print(j)
#http://huaban.com/pins/1511030148
#http://huaban.com/pins/1509969174
'''
html2 = spider.getUrl('http://huaban.com/pins/1509969174')
html2 = html2.read().decode('utf-8')
#print(html2)

html2 = re.findall('',html2)
#html2 = re.findall('<img src="//[^/]*/[^"]*"',html2)

#for i in html2:
    #print('http:' + i.split('"')[1])

printl.printL(html2)

#<img src="//img.hb.aicdn.com/a5a72d4bad411909a5dda05b86a40906c2cdfd4110ecdc-7sik4K_fw658" width="658"
