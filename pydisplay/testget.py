import requests
import json
urlget="http://192.168.4.1"
# header_info={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'}
#
# resget = requests.get(url=urlget,headers=header_info,timeout=500)
# print(resget.text)
# print("获取吊臂信息成功！")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
    'ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'ACCEPT-ENCODING': 'gzip, deflate, br',
    'ACCEPT-LANGUAGE': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'REFERER': 'hushen'
}



for i in range(50):
    r = requests.get(urlget,headers=headers,timeout=100)

    print(str(i),r.text)


# url = 'http://quan.suning.com/getSysTime.do'
# for i in range(30):
#     # res=requests.get(url).text
#     # #print(res)
#     # j=json.loads(res)
#     # t2_date = j['sysTime2'].split()[0] #日期
#     # t2_time = j['sysTime2'].split()[1] #时间
#     # t_time=t2_date+' '+t2_time
#     # print (t_time)
#     print(i)