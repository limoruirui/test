from requests import get, post
from time import sleep, time
from random import uniform
from json import dumps
def timestamp():
    return int(round(time()*1000))
def tgpush(content):
    bot_token = '2099344461:AAEdpKluee3ljwJdwPRCOQxDMTeZSX7lJ1o'
    user_id = '657034974'
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'chat_id': str(user_id), 'text': content, 'disable_web_page_preview': 'true'}
    try:
        req = post(url, headers=headers, data=data)
    except:
        print('推送失败')
def getId(ck):
    url = 'https://m.client.10010.com/welfare-mall-front-activity/super/five/get619Activity/v1?whetherFriday=&from=955000006&acId=AC20211104165159'
    headers = {
      'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148  unicom{version:iphone_c@8.0900}{systemVersion:dis}{yw_code:}',
      'Referer': 'https://img.client.10010.com/',
       'Cookie': ck
    }
    data = post(url, headers=headers).json()['resdata']['tabList'][0]['goodsList']
    goodsNameList = {'星巴克30元代金券': '', '盒马鲜生30元电子券': '', '奈雪的茶30元代金券': '', '爱奇艺黄金月卡': '', '腾讯视频会员月卡': ''}
    for i in range(len(data)):
        if data[i]['goodsName'] in goodsNameList:
            goodsNameList[data[i]['goodsName']] = data[i]['goodsId']
    return goodsNameList
def buy(ck):
    goodsNameList = getId(ck)
    for goodsName in goodsNameList:
        goodsId = goodsNameList[goodsName]
        print(goodsId)
        url = 'https://m.client.10010.com/welfare-mall-front/mobile/api/bj2402/v1'
        headers = {
      'Cookie': ck,
      'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148  unicom{version:iphone_c@8.0900}{systemVersion:dis}{yw_code:}',
'Referer': f'https://img.client.10010.com/jifenshangcheng/goodsorder?goodsId={goodsId}&type=C&pip=192',
          'Content-Type': 'application/x-www-form-urlencoded'
    }
        data = {
          'reqsn': '4eddd450-e8c6-90dc-7762-abc19d18f8ab',
          'reqtime': timestamp(),
          'cliver': '',
          'reqdata': {"goodsId":goodsId,"payWay":"01","amount":"4.90","saleTypes":"C","points":0,"beginTime":1636077600000,"imei":"054bdfb98e2eb748385471df74e0d41be5a6fd3c41f39588a271cd749d659038","sourceChannel":"955000006","proFlag":"","scene":"","promoterCode":"","sign":"","oneid":"","twoid":"","threeid":"","maxcash":"","floortype":"undefined","FLSC_PREFECTURE":"SUPER_FRIDAY","launchId":"","platAcId":"AC20211104165159"}
        }
        print(post(url, headers=headers, data=dumps(data)).json())
if __name__ == '__main__':
    ck = 'ecs_token=eyJkYXRhIjoiNWVjMzc1MzNjZDhiYmJhZTEwYWQ1NDMzYjIyNDJkODc2M2Q4ZWU2M2U4ZjAxYTk5OGEzNTQ2NDcwMDFmNzI3NDEwNDYzZmE3MWFhM2M0YjM0MzUyMDAyMDQyZWM1MDcyZWU1OTRhYTQ2M2JkMzFiOTZmOTk1ODBjODFmNzhlZTkyM2IxMDcwMzRiMTQwMTAwMTVmNGYxMDJlMDRhNDM1MGQxNzdiYjUxOGY4ZTVlOTg0N2M3MWNkMmM1MGUwMDE4IiwidmVyc2lvbiI6IjAwIn0=;'
    buy(ck)
