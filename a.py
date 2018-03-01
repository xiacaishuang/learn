# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
#def LoginEmail(fromAdd, toAdd, subject,  htmlText):
smtp = smtplib.SMTP_SSL('smtp.qq.com',465)
smtp.login('751405162@qq.com','wbuerwowedwdbfca')
def SendEmail(fromAdd, toAdd, subject,  htmlText):
  strFrom = fromAdd
  strTo = toAdd
  msg =MIMEText(htmlText)
  msg['Content-Type'] = 'Text/HTML'
  msg['Subject'] = Header(subject,'gb2312')
  msg['To'] = strTo
  msg['From'] = strFrom
  smtp.sendmail(strFrom,strTo,msg.as_string())

a={"date":"20180227","message":"Success !","status":200,"city":"成都","count":1190,"data":{"shidu":"76%","pm25":67.0,"pm10":98.0,"quality":"良","wendu":"11","ganmao":"极少数敏感人群应减少户外活动","yesterday":{"date":"26日星期一","sunrise":"07:35","high":"高温 14.0℃","low":"低温 9.0℃","sunset":"19:00","aqi":92.0,"fx":"无持续风向","fl":"<3级","type":"小雨","notice":"雨虽小，注意保暖别感冒"},"forecast":[{"date":"27日星期二","sunrise":"07:34","high":"高温 17.0℃","low":"低温 9.0℃","sunset":"19:00","aqi":99.0,"fx":"无持续风向","fl":"<3级","type":"多云","notice":"阴晴之间，谨防紫外线侵扰"},{"date":"28日星期三","sunrise":"07:33","high":"高温 18.0℃","low":"低温 9.0℃","sunset":"19:01","aqi":104.0,"fx":"无持续风向","fl":"<3级","type":"多云","notice":"阴晴之间，谨防紫外线侵扰"},{"date":"01日星期四","sunrise":"07:32","high":"高温 22.0℃","low":"低温 11.0℃","sunset":"19:02","aqi":89.0,"fx":"无持续风向","fl":"<3级","type":"多云","notice":"阴晴之间，谨防紫外线侵扰"},{"date":"02日星期五","sunrise":"07:31","high":"高温 22.0℃","low":"低温 11.0℃","sunset":"19:03","aqi":75.0,"fx":"无持续风向","fl":"<3级","type":"多云","notice":"阴晴之间，谨防紫外线侵扰"},{"date":"03日星期六","sunrise":"07:30","high":"高温 20.0℃","low":"低温 13.0℃","sunset":"19:03","aqi":99.0,"fx":"无持续风向","fl":"<3级","type":"阴","notice":"不要被阴云遮挡住好心情"}]}}
print ('%s今天天氣狀況爲:'%a['city'])
print ('日期:%s'%a['date'])
print ('溫度:%s'%a['data']['wendu'])
print ('易感人羣情況:%s'%a['data']['ganmao'])
print ('溼度:%s'%a['data']['shidu'])
print ('PM25:%s'%a['data']['pm25'])
print ('PM10:%s'%a['data']['pm10'])
print ('空氣質量:%s'%a['data']['quality'])
print ('\n明日天氣预测狀況爲:')
print ('日期:%s'%a['data']['forecast'][0]['date'])
print ('最高温度:%s'%a['data']['forecast'][0]['high'])
print ('最低温度:%s'%a['data']['forecast'][0]['low'])
print ('风向:%s'%a['data']['forecast'][0]['fx'])
print ('风级:%s'%a['data']['forecast'][0]['fl'])
print ('天气状况:%s'%a['data']['forecast'][0]['type'])
print ('日出时间:%s'%a['data']['forecast'][0]['sunrise'])
print ('日落时间:%s'%a['data']['forecast'][0]['sunset'])
print ('注意:%s'%a['data']['forecast'][0]['notice'])
SendEmail('751405162@qq.com', '751405162@qq.com', 'subject', 'test<br>test2')
smtp.quit()





