import yagmail #要pip安装
import os

# print(os.listdir("F:\\API_Autotest\\report\\"))
base_path = os.path.dirname(os.getcwd())
print(base_path)


def get_report_file(report_path):
    '''获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda x: os.path.getmtime(os.path.join(report_path, x))) # 升序排序

    print (u'最新测试生成的报告： ' + lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file



def send():
    yag = yagmail.SMTP(user="1315392407@qq.com",password="vnkbafuryetvghbj",host="smtp.qq.com")  # 这个要这样写

    subject = "自动化测试报告"

    body = "测试邮件的内容部分在下方"

    h1 = "<h1>shoopee</h1>"

    link = '点击<a href="http//www.baidu.com">连接</a>,前往shoopee网站'

    #添加邮件的附件
    att1 = base_path+"\\report\\"  # 这里要是双斜杠\\才可以发的出去
    # att2 = "c:\\2.txt"  可以发送多个附件
    # att3 = "c:\\3.json"

    file = get_report_file(att1)

    contend = "测试报告"

    yag.send("18680674921@163.com",subject=subject,contents=[body,h1,link,file])
    print("报告发送完毕")

# send()