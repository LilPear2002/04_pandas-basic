# 小黎专属python固定模板
# 开发时间：2024/8/22 14:53

import pandas as pd

data = pd.read_csv("D:\\pycharm_workspace\\04_pandas基础\\student.csv", encoding='gbk')
print(data)

data.to_pickle('student_pickle')