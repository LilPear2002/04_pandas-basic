# 小黎专属python固定模板
# 开发时间：2024/8/22 15:08

import pandas as pd
import numpy as np

# concatenating
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])
print(df1)
print(df2)
print(df3)
print('---------------------')
# 上下合并
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res)

# join,['inner','outer']
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
print(df1)
print(df2)
print('---------------------')
res = pd.concat([df1, df2], join='inner', ignore_index=True)
print(res)

print('---------------------')

