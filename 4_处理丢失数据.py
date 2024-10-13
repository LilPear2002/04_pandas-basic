# 小黎专属python固定模板
# 开发时间：2024/8/22 14:41

import pandas as pd
import numpy as np

dates = pd.date_range('20240821', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)
print('-------------------')

# 处理行 若有NaN则丢失整行
print(df.dropna(axis=0, how='any'))
# 全部为NaN才丢失
# print(df.dropna(axis=0, how='all'))
# 处理列
# print(df.dropna(axis=1, how='any'))
print('-------------------')

df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
# 填充为0
print(df.fillna(value=0))
print('-------------------')
print(np.any(df.isnull()))
