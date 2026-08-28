from my_api import ai_ask
import pandas as pd
import os
def material_select_ai(path):
    file_name, ext = os.path.splitext(path)
    ext = ext.lower()
    #csv
    if ext == '.csv':
        df=pd.read_csv(path,encoding='gbk')
        text=df.to_string(index=False)
        #设定系统角色与提示词
        system_info = "你是一名新能源储能材料工程师，根据提供的电极材料数据筛选合适的材料。"
        user_prompt = f"""
        以下是本次锂离子电池样品实验数据：
        {text}
        根据以上数据筛选出综合性能最佳的三个电极材料。
        """
        #调用
        print('正在生成中...')
        ai_ask(system_info,user_prompt)

    #excel
    elif ext in ['.xls','.xlsx']:
        df=pd.read_excel(path)
        text=df.to_string(index=False)
        system_info = "你是一名新能源储能材料工程师，根据提供的电极材料数据筛选合适的材料。"
        user_prompt = f"""
                以下是本次锂离子电池样品实验数据：
                {text}
                根据以上数据筛选出综合性能最佳的三个电极材料。
                """
        # 调用
        print('正在生成中...')
        ai_ask(system_info, user_prompt)

if __name__ == "__main__":
    # 运行入口，修改为你的excel路径
    EXCEL_FILE = "C:/Users/35230/Desktop/测试文件/电极材料相关.csv"
    material_select_ai(EXCEL_FILE)
