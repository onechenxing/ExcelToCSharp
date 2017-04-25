"""
批量执行操作
@author: ChenXing
@email:  onechenxing@163.com
@date:   2017/4/5

"""

import os

pyList = ["excel_to_csv.py",
          "csv_to_csharp.py",
          "copy_files_csv.py",
          "copy_files_cs.py"
          ]

for py in pyList:
    os.system(py)

print("all_do ok.")
input()

