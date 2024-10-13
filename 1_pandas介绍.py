# 小黎专属python固定模板
# 开发时间：2024/8/21 22:21

import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)

dates = pd.date_range('20240821', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)

df2 = pd.DataFrame(np.arange(12).reshape(3, 4))
print(df2)

