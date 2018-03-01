# -*- coding: utf-8 -*-
import requests
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header

def SendEmail(fromAdd, toAdd, subject,  htmlText):
  strFrom = fromAdd
  strTo = toAdd
  msg =MIMEText(htmlText)
  msg['Content-Type'] = 'Text/HTML'
  msg['Subject'] = Header('成都今天天气状况','utf-8').encode()
  msg['To'] = strTo
  msg['From'] = strFrom
  smtp.sendmail(strFrom,strTo,msg.as_string())

url = "https://www.sojson.com/open/api/weather/json.shtml"

querystring = {"city":"%E6%88%90%E9%83%BD"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "2f01661a-9699-34a0-c733-e4e267c0d679"
    }

response = requests.request("GET", url, headers=headers, params=querystring).json()

a=response
s=''
s=s+'成都今天天氣狀況爲:<br>'
s=s+'日期:'+a['data']['forecast'][0]['date']+'<br>'
#print ('日期:%s'%a['date'])
s=s+'溫度:'+a['data']['wendu']+'<br>'
s=s+'易感人群情況:'+a['data']['ganmao']+'<br>'
s=s+'湿度:'+a['data']['shidu']+'<br>'
s=s+'PM25:'+str(a['data']['pm25'])+'<br>'
s=s+'PM10:'+str(a['data']['pm10'])+'<br>'
s=s+'空氣質量:'+a['data']['quality']+'<br>'
s=s+'最高温度:'+a['data']['forecast'][0]['high']+'<br>'
s=s+'最低温度:'+a['data']['forecast'][0]['low']+'<br>'
s=s+'风向:'+a['data']['forecast'][0]['fx']+'<br>'
s=s+'风级:'+a['data']['forecast'][0]['fl']+'<br>'
s=s+'天气状况:'+a['data']['forecast'][0]['type']+'<br>'
s=s+'日出时间:'+a['data']['forecast'][0]['sunrise']+'<br>'
s=s+'日落时间:'+a['data']['forecast'][0]['sunset']+'<br>'
s=s+'注意:'+a['data']['forecast'][0]['notice']+'<br>'
s=s+'成都明日天氣预测狀況爲:'+'<br>'
s=s+'日期:'+a['data']['forecast'][1]['date']+'<br>'
s=s+'最高温度:'+a['data']['forecast'][1]['high']+'<br>'
s=s+'最低温度:'+a['data']['forecast'][1]['low']+'<br>'
s=s+'风向:'+a['data']['forecast'][1]['fx']+'<br>'
s=s+'风级:'+a['data']['forecast'][1]['fl']+'<br>'
s=s+'天气状况:'+a['data']['forecast'][1]['type']+'<br>'
s=s+'日出时间:'+a['data']['forecast'][1]['sunrise']+'<br>'
s=s+'日落时间:'+a['data']['forecast'][1]['sunset']+'<br>'
s=s+'注意:'+a['data']['forecast'][1]['notice']
smtp = smtplib.SMTP_SSL('smtp.qq.com',465)
smtp.login('751405162@qq.com','wbuerwowedwdbfca')
with open('./user.txt') as file:
    for line in file.readlines():
        SendEmail('751405162@qq.com', line.replace('\n',''), 'subject', s)
    smtp.close
while (1):
    if time.strftime("%H:%M:%S",time.localtime(time.time()))=='07:50:00':
        smtp = smtplib.SMTP_SSL('smtp.qq.com',465)
        smtp.login('751405162@qq.com','wbuerwowedwdbfca')
        with open('./user.txt') as file:
            for line in file.readlines():
                SendEmail('751405162@qq.com', line.replace('\n',''), 'subject', s)
        smtp.close

#SendEmail('751405162@qq.com', '751405162@qq.com', 'subject', s)

