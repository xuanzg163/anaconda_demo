import pandas as pd
# 目标文件位置
file = "D:/python_workspace/station_agent_check_list.xlsx"
data = pd.read_excel(file, sheet_name='EVT',keep_default_na=False)
# 表头
head_list = list(data.columns)
print(head_list)
# 将excel数据转换成列表放入list_dic
list_dic = []
# api地址list
apiList_dic=[]
#预期相应结果list
responseList_dict=[]
for i in data.values:  # i 为每一行的value的列表
    a_line = dict(zip(head_list, i))
    list_dic.append(a_line)
# 遍历excel值
for i in list_dic:
    # print(i)
    # 分析数据，拆分出api地址，请求参数，目标结果
    apiList_dic.append(i['测试方法'].replace(" ",""))
    print("============",i['预期结果'])
    responseList_dict.append(i['预期结果'])

print(responseList_dict)