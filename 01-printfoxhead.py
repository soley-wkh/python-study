# -*- coding:utf-8 -*-
"""
    version: 
    author : wkh
    time   : 2019/7/2 17:56
    file   : 01-printfoxhead.py
    
"""
# for i in range(1, 8):
#     # 处理每一行中" "的个数
#     for k in range(0, 8 - i):
#         print(' ', end='')
#     # 处理每一行中的"*"个数
#     for j in range(1, 2 * i):
#         print('*', end='')
#     for k in range(0, 25 - 2 * i, 1):
#         print(' ', end='')
#     for j in range(1, 2 * i):
#         print('*', end='')
#     print()


for i in range(1, 8):
    print(' ' * (8 - i), '*' * (2 * i - 1), ' ' * (2 * (8 - i) + 13), '*' * (2 * i - 1))

for i in range(1, 7):
    print(' ' * (4 * (i - 1)), ',' * (3 * (6 - i) + 1), '*' * (2 * (6 - i) + 1), ',' * (3 * (6 - i) + 1))
