
'''
A simple Gooey example. One required field, one optional.
'''
# 导入第三方库
import xml.etree.ElementTree as ET
from gooey import Gooey, GooeyParser
import datetime

def alterxmlbug(name_of_user,DC,FC):
    file_xml = FC
    parser = ET.XMLParser(encoding="utf-8")
    # print(file_xml)
    print("修改的文件：",file_xml, flush=True)
    tree = ET.parse(file_xml,parser)  # 类ElementTree
    root = tree.getroot()  # 类Element

    # user = root.find("voucher")
    user = root.find("voucher").find('voucher_head').find("pk_prepared")
    user.text = name_of_user
    user = root.find("voucher").find('voucher_head').find("pk_prepared").text
    # print(user)
    # print(root)
    # print(ET.tostring(root))
    details =  root.find("voucher").find('voucher_head').find("details")
    i= 0
    for item in details.iter('item'):
        for ass in item.iter('ass'):
            for ass_item in  ass.iter('item'):
                if ass_item.find('pk_Checktype').text == 'ZLZB1':
                    ass_item.find('pk_Checktype').text = 'ZLZB0001'
                if ass_item.find('pk_Checktype').text == 'ZLZB4':
                    ass_item.find('pk_Checktype').text = 'ZLZB0004'
    time = datetime.datetime.now()
    filename = '\\'+'xmlR'+name_of_user+str(time.year)+str(time.month)+str(time.day)+'.xml'

    tree=ET.ElementTree(root)
    tree.write(DC+filename)
    print("操作成功,文件位于："+ DC+filename, flush=True)
    # print(i)


@Gooey(program_name="易盛用友数据修正程序1.0",language='chinese', default_size=(610,600),encoding='cp936')
def main():

    name_of_user = ''


    parser = GooeyParser(description='选择下面参数')

    name = parser.add_argument_group('选择操作人名字', gooey_options={
        'show_border': True
    })
    verbosity = name.add_mutually_exclusive_group()
    # verbosity.add_argument(help='Duration (in seconds) of the program output')
    z = verbosity.add_argument('-a', '--22', dest='请点击原点选择',
                           action= "store_true",)
    a = verbosity.add_argument( '--c', dest='chenyanlin',
                           action="store_true",)
    b = verbosity.add_argument( '--vl', dest='vernalin',
                           action="store_true",)
    c = verbosity.add_argument('--sq', dest='XGIT',
                           action="store_true",)
    
    # file_help_msg = "Name of the file you want to process"

    file = parser.add_argument_group('选择要修改的文件，以及导出的文件位置', gooey_options={
        'show_border': True
    })
    file.add_argument("FileChooser",
        help="选择你要修改的文件",  widget="FileChooser")
    file.add_argument("DirectoryChooser",
         help="选择你要保存的文件位置", widget="DirChooser")


    args = parser.parse_args()
    FC= ''
    DC = ''
    message = vars(args)
    # print(message)
    for key in message:
        if message[key] == True:
            name_of_user = key
        if key == "FileChooser":
            FC = message[key]
        if key == "DirectoryChooser":
            DC = message[key]
    # print(name_of_user,DC,FC)
    # print(args)

    alterxmlbug(name_of_user,DC,FC)





if __name__ == '__main__':
    main()
    # alterxmlbug()
