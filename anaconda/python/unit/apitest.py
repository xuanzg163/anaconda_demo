import unittest
import json
import traceback
import requests

# api请求地址
url = "http://localhost:8099/wx/get/reserveinfoAll"
# 拼接的请求参数
querystring = {"skey": "xxxx"}
# 请求头部信息
headers = {
    'cache-control': "no-cache",
}
data = dict
# 响应信息
response = requests.request("POST", url, headers=headers, params=querystring)
# 将结果转换json串
result = json.loads(response.text)
for i in result:
    print("车型++++++++", i['carName'])
    print(i)

