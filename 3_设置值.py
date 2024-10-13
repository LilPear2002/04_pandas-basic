# 小黎专属python固定模板
# 开发时间：2024/8/22 14:14

import pandas as pd
import numpy as np

dates = pd.date_range('20240821', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
print('-------------------')
df.iloc[2, 2] = 111
print(df)
print('-------------------')
df.loc['20240822', 'B'] = 222
print(df)
print('-------------------')
df['F'] = np.nan
print(df)
print('-------------------')
df['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20240821',periods=6))
print(df)
print('-------------------')
