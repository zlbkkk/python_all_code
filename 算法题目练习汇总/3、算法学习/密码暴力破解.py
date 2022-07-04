import zipfile
# from unrar import rarfile
import threading

# 判断线程是否需要终止
flag = True


def extract(password, file):
    try:
        password = str(password)
        file.extractall(pwd=password.encode('utf-8'))  # zip解压缩
        # file.extractall(pwd=password)#rar解压缩
        print("压缩包的密码是：{}".format(password))
        global flag
        flag = False
    except Exception:
        print(f"第{index}行的{password}密码是错误的".format(index,password))





def main():
    file = zipfile.ZipFile("c:\\1.zip")  # 压缩文件
    # file = rarfile.RarFile("pwd.rar")

    with open("c:\\pwd.txt",encoding="utf-8") as f:
        date = f.readlines()
        # print(date)
        global index
        for index,line in enumerate(date):
            line = line.strip()

            index=index
            # print(line)

            if flag is True:
                # number = str(number).zfill(4)
                # print(number)
                t = threading.Thread(target=extract, args=(line, file))
                t.start()
                t.join()


if __name__ == '__main__':
    main()
