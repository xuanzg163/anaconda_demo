import pandas as pd
import json

targetFile = "D:/python_workspace/v7_api_check_list.xlsx"
data = pd.read_excel(targetFile, sheet_name='EVT')
# excel表头
head_list = list(data.columns)
# print(head_list)
# 将excel数据转换成列表放入list_dic
list_dic = []
# api地址list
apiList_dic = []
# 预期相应结果list
responseList_dict = []
for i in data.values:  # i 为每一行的value的列表
    a_line = dict(zip(head_list, i))
    list_dic.append(a_line)
print("data.value===========",data.values)
print("获取的excel数据======",list_dic)
# 定义行列值
df = pd.DataFrame({'Name': ['A', 'B', 'C', 'D'],
                   'Age': [10, 0, 30, 50]})
# df = pd.DataFrame()
# 使用XlsxWriter创建一个写引擎
writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
# 将dataframe转换成XlsxWriter对象
# df.to_excel(writer, sheet_name='Sheet1', index=False)
# writer.save()
# print("excel 处理完毕")

data.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()
print("new data is wirting done!!!")
