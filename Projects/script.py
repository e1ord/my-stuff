# Gamertag Autoclaimer

import requests
import lxml.html

# Session Saves Cookies

s = requests.session()

# Payload Is Used For Login

payload = {
    'login': 'ldrew.email@gmail.com',
    'passwd': 'snapcap85',
}

# Post Payload To Website

response = s.post('https://login.live.com/ppsecure/post.srf?wa=wsignin1.0&rpsnv=13&rver=7.3.6963.0&wp=MBI_SSL&wreply=https:%2f%2faccount.xbox.com%2fen-us%2faccountcreation%3freturnUrl%3dhttps%253a%252f%252fwww.xbox.com%253a443%252fen-US%252f%26ru%3dhttps%253a%252f%252fwww.xbox.com%252fen-US%252f%26rtc%3d1%26csrf%3dGCJwcBlYP51Iq1AE2Qnoq4XroB1sLZucKJcB30cl9ZeddXAKEbiwb7Q6vrM0gPLcM1vAVxD8QRjzDGsGaR8xwYf9AlE1&lc=1033&id=292543&aadredir=1&contextid=C29BCBB0694AC9EA&bk=1607973459&uaid=8fff75d0e7b341c1962ec7193e5cdb3c&pid=0', data=payload)

# HTTP Status Codes
# 1XX = Informational
# 2XX = Success
# 3XX = Redirection
# 4XX = Client Error
# 5XX = Server Error

if response.status_code == 100:
    print('\033[0;32mStatus Code = Informational') 
if response.status_code == 200:
    print('\033[1;33mStatus Code = Success')     
if response.status_code == 300:
    print('\033[0;31mStatus Code = Redirection')  
if response.status_code == 400:
    print('\033[0;34mStatus Code = Client Error')   
if response.status_code == 500:
    print('\033[0;35mStatus Code = Server Error')          

#

r = s.get('https://social.xbox.com/changegamertag')
lxlml = lxml.html.fromstring(r.content)

print(lxml.xpath('''//*[@id="root"]/div[2]/div/div[2]/div[3]/span/p/text()'''))