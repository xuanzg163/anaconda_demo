import pandas as pd
import json
import traceback
import requests

# 目标文件位置
file = "D:/python_workspace/station_agent_check_list.xlsx"
targetFile = "D:/python_workspace/v7_api_check_list.xlsx"
# IP地址
ipUrl = "192.168.3.42"
# 端口
portUrl = "8099"
# 拼接的请求参数
querystring = {"skey": "xxxx"}
# 请求头部信息
headers = {
    'cache-control': "no-cache",
}

# 发起测试请求
def apitest(type, url, querystring, headers):
    # 响应信息
    response = requests.request(type, url, headers=headers, params=querystring)
    # 将结果转换json串
    return json.loads(response.text)


# 读取excel信息
# data = pd.read_excel(file, sheet_name='EVT', keep_default_na=False)
data = pd.read_excel(targetFile, sheet_name='EVT', keep_default_na=False)
# excel表头
head_list = list(data.columns)
print(head_list)
# 将excel数据转换成列表放入list_dic
list_dic = []
# api地址list
apiList_dic = []
# 预期相应结果list
responseList_dict = []
for i in data.values:  # i 为每一行的value的列表
    a_line = dict(zip(head_list, i))
    list_dic.append(a_line)
# 遍历excel值
for i in list_dic:
    # print(i)
    # 分析数据，拆分出api地址，请求参数，目标结果
    apiList_dic.append(i['测试方法'].replace(" ", ""))
    # print("预期结果============", i['预期结果'])
    responseList_dict.append(i['预期结果'])
    totalResult= json.loads(i['预期结果'])
print("需要测试的接口地址============", apiList_dic)
# print(responseList_dict)
# 遍历apilist集合，拼接完整的请求url，调用requests.request
for i in apiList_dic:
    print(i)
    # 获取请求协议 http\https
    paramRequestStr = i.split(':')
    paramRequestProtocol = paramRequestStr[0]
    # 获取请求方式 put\get\post\delete
    paramRequestType = (paramRequestStr[1].split("/"))[0]
    # 获取请求url
    if (paramRequestType == "GET"):
        requestUrl = (paramRequestStr[1].split("GET"))[1]
    #     拼接请求地址 协议+ip+接口路径
    elif (paramRequestType == "PUT"):
        requestUrl = (paramRequestStr[1].split("PUT"))[1]
    elif (paramRequestType == "POST"):
        requestUrl = (paramRequestStr[1].split("POST"))[1]
        print("api========url", requestUrl)
        print("api========协议", paramRequestProtocol)
        print("api========请求方式", paramRequestType)
        apiUrl = paramRequestProtocol.lower() + "://" + ipUrl + ":" + portUrl + requestUrl
        # 发起测试请求-接受结果
        result = apitest(paramRequestType, apiUrl, querystring, headers)
        print("api请求获取结果======",result)
        print("预期结果============",totalResult)
        # 请求结果处理。回写入api测试文件，显示测试统计结果
        for i in result:
            print("预约用户姓名： ", i['realName'])

    # print("api type========",paramRequestProtocol)
    # print("api type========",paramRequestType)
