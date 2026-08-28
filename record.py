import os
import pandas as pd

folder_name='测试文件'

excel_name='正极材料汇总.xlsx'

data_path=r"C:\Users\35230\Desktop"
folder_path=os.path.join(data_path,folder_name)
excel_path=os.path.join(folder_path,excel_name)
#提取数据
data={
    '材料名称':[],
    '缺点':[],
    '优点':[],
    '相关性能参数':[],
    '成本':[],
    }
for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        txt_path=os.path.join(folder_path,file_name)
        f=open(txt_path,'r',encoding='utf-8')
        txt=f.read()
        txt_data=txt.split('\n')
        for line in txt_data:
            if line.startswith('材料名称'):
                line = line.replace('材料名称：', '')
                data['材料名称'].append(line)
            if line.startswith('缺点'):
                line = line.replace('缺点：', '')
                data['缺点'].append(line)
            if line.startswith('优点'):
                line = line.replace('优点：', '')
                data['优点'].append(line)
            if line.startswith('相关性能参数'):
                line = line.replace('相关性能参数：', '')
                data['相关性能参数'].append(line)
            if line.startswith('成本'):
                line.replace('成本：', '')
                data['成本'].append(line)
print(data)
df=pd.DataFrame(data)
df.to_excel(excel_path,index=False)
print('保存完毕')

        

