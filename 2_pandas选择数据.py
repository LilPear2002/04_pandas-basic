# 小黎专属python固定模板
# 开发时间：2024/8/21 22:36

import pandas as pd
import numpy as np

dates = pd.date_range('20240821', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
print('-------------------')
print(df['A'])
print('-------------------')
print(df[0:3])
print('-------------------')
print(df['20240822':'20240824'])
print('-------------------')
print(df.loc['20240821'])
print('-------------------')
print(df.loc[:, ['A', 'B']])
print('-------------------')
print(df.loc['20240825', ['C', 'D']])
print('-------------------')
print(df.iloc[3])
print('-------------------')
print(df.iloc[3:5, 1:3])
print('-------------------')
# print(df.ix[:3, ['A', 'C']])

