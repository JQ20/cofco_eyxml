'''
A simple Gooey example. One required field, one optional.
'''

from gooey import Gooey, GooeyParser

def alterxmlbug():
    return


@Gooey(program_name="易盛用友数据修正程序",language='chinese')
def main():

    name_of_user = ''


    parser = GooeyParser(description='选择下面参数')

    name = parser.add_argument_group('选择用友表名', gooey_options={
        'show_border': True
    })
    verbosity = name.add_mutually_exclusive_group()
    # verbosity.add_argument(help='Duration (in seconds) of the program output')
    a = verbosity.add_argument('--t', '--verbozze', dest='chenyanlin',
                           action="store_true",help='请点击圆点，不要点击文字！')
    b = verbosity.add_argument('--q', '--quiet', dest='vernalin',
                           action="store_true",help='请点击圆点，不要点击文字！')
    
    args = parser.parse_args()

    message = vars(args)
    print(message)
    for key in message:
        if message[key] == True:
            name_of_user = key
    print(name_of_user)




if __name__ == '__main__':
    main()
