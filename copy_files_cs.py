"""
批量复制文件并改名
@author: ChenXing
@email:  onechenxing@163.com
@date:   2015/4/2

"""

import os
import os.path as path
import shutil as sh



sourceDir = "csv"
targetDir = "../../Assets/Scripts/Data/Info"
#要查找的文件后缀
suffixList = [".cs"]
#要添加的新后缀
addSuffix = ""

def checkSuffix(fileName):
    for suffix in suffixList:
        if fileName.endswith(suffix):
            return True
    return False

try:
    for file in os.listdir(sourceDir):
        sourceFile = path.join(sourceDir, file)
        targetFile = path.join(targetDir, file + addSuffix)             
        if path.isfile(sourceFile) and checkSuffix(sourceFile):
            sh.copy(sourceFile,targetFile)
except IOError:
                print("copy file error")
print("copy_files_cs ok.")
#input()

