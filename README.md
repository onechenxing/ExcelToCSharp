注意：Python3以上版本，需要用pip安装xlrd包


1.模版配置:
修改copy_files各代码里面的目标路径targetDir即可实现自动生成文件到指定目录

2.执行生成：
把待生成的Excel表放入csv文件夹
点击all_do.py生成

3.Excel规则，请参考csv目录的Enemy.xlsx
第一行为注释,[]里面为数据类型，支持：int,float
第二行为变量名
后面行为具体的数值行

4.游戏内代码使用：

确保游戏已经加载好了csv文件

动态解析csv代码范例：（如果vs导入了快捷代码模版输入csv+两次tab键）

	/// <summary>
        /// 技能静态表
        /// </summary>
        private Dictionary<int, SkillInfo> _skillInfoDic;
        /// <summary>
        /// npc静态表
        /// </summary>
        public Dictionary<int, SkillInfo> skillInfoDic
        {
            get
            {
                //解析
                if (_skillInfoDic == null)
                {
                    _skillInfoDic = CsvTool.CsvToDictionary<int, SkillInfo>("csv_skill", "id");
                }
                return _skillInfoDic;
            }
        }
