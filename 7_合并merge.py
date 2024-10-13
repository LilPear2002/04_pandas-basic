# 小黎专属python固定模板
# 开发时间：2024/8/22 15:24

import pandas as pd
import numpy as np

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)

res = pd.merge(left, right, on='key')
print(res)
print('--------------------')

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
res = pd.merge(left, right, on=['key1', 'key2'], how='inner')
print(res)
print('------------------------')
res = pd.merge(left, right, on=['key1', 'key2'], how='outer', indicator=True)
print(res)
print('--------------------------')
res = pd.merge(left, right, on=['key1', 'key2'], how='right')
print(res)
print('--------------------------')
res = pd.merge(left, right, on=['key1', 'key2'], how='left')
print(res)
print('--------------------------')