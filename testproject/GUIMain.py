from gooey import Gooey, GooeyParser
import jinSpider
 

@Gooey(program_name="易盛用友数据修正程序",language='chinese')
def gui():
    parser = GooeyParser(description="",)
    parser.add_argument('选择日期', widget="DateChooser")          # 日期选择框
    parser.add_argument('选择导出路径', widget="DirChooser")      # 文件选择框

    args = parser.parse_args()                                 # 接收界面传递的参数
    # print(type(args))
    message = vars(args)
    path = message['选择导出路径']
    date = message['选择日期']
    jinSpider.jindata_doc(path,date)
    # print(date)
    # print(path)
    print("日报成功生成！")
    


if   __name__ == '__main__':
    gui() 