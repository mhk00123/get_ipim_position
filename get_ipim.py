from requests_html import HTMLSession
import requests
import time

url = 'https://m.ipim.gov.mo/zh-hant/recruitment/recruitment-notice/'

# Request to ipim
session = HTMLSession()
rs = session.get(url)

# Get 2&3 item
text = rs.html.find('.recruitment-item')
text1 = text[1].text
text2 = text[2].text

print(text1 + '\n' + text2)
ptime = time.strftime("%H:%M")
print("-------------  "+time.strftime("%H:%M")+"  ---------------\n")    

# URL request to Wechat
url2 = 'https://sc.ftqq.com/SCU52896T17559e439d325e78cd0f71bfa5b877945cf68de25a16b.send?text=貿促局更新左啦'

rs.close()

# Loop per 30min
while 1 :
    time.sleep(1800)
    rss = session.get(url)
    text_loop = rss.html.find('.recruitment-item')
    loop1 = text_loop[1].text
    loop2 = text_loop[2].text

    print(loop1 + '\n' + loop2)
    print("-------------  "+time.strftime("%H:%M")+"  ---------------\n")    

    # Compare with the First scrapy
    if((loop1 != text1) or (loop2 != text2)):
        print("Change!")
        requests.get(url2)
        rss.close()
        break
    rss.close()