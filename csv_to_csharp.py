"""
csv转换成C#代码工具
@author: ChenXing
@email:  onechenxing@163.com
@date:   2015/1/17

"""

import glob

def buildCode(filePath):
        #类模版
        classTemplate = """
using System;

namespace Data
{
    /// <summary>
    /// 静态表数据类
    /// </summary>
    [Serializable]
    public class $className
    {
	$paramFied

		public $className Clone()
		{
			return ($className) this.MemberwiseClone();
		}
    }
}
"""
        #属性模版
        paramTemplate = """
        /// <summary>
        /// $paramNote
        /// </summary>
        public $paramType $paramName;"""
        
        className = filePath.split("\\")[-1].split(".")[0] + "Info"    
        code = "";
        try:
                with open(filePath, encoding = "utf-8") as dataFile:
                        notes = dataFile.readline().strip('\n').split(",")
                        params = dataFile.readline().strip('\n').split(",")
                        for i,paramName in enumerate(params):
                                try:
                                        paramNote = notes[i]
                                        #默认类型string
                                        paramType = "string"
                                        #查找和判断类型
                                        findIndex = 0;
                                        findIndex = paramNote.rfind("[int]")                                     
                                        if(findIndex != -1):
                                           paramType = "int"
                                           paramNote = paramNote[0:findIndex]
                                        findIndex = paramNote.rfind("[float]")
                                        if(findIndex != -1):
                                           paramType = "float"
                                           paramNote = paramNote[0:findIndex]               
                                        #生成属性
                                        code += paramTemplate.replace("$paramNote", paramNote).replace("$paramName", paramName).replace("$paramType",paramType)
                                except ValueError:
                                        pass
                        #生成类
                        code = classTemplate.replace("$className", className).replace("$paramFied", code)
        except IOError as err:
                print("The data file is missing:" + str(err))
        try:
                with open("csv\\" + className + ".cs", "w", encoding = "utf-8") as outFile:
                        print(code, end="", file = outFile)
        except IOError:
                print("write file error")


#导出csv目录下所有文件
csvFiles = glob.glob("csv\\*.csv")
for eachFile in csvFiles:
	buildCode(eachFile)
print("csv_to_csharp ok.")
#input()





