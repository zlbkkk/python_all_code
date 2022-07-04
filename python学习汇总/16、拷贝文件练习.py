import os


def copy(old_floder, new_floder,filename):
    # print("文件{},从{}复制到{}".format(filename,old_floder,new_floder))

    with open(old_floder+"\\"+filename,"rb") as f1:
        data = f1.read()

    with open(new_floder+"\\"+filename,"wb") as f2:
        f2.write(data)

    print("文件{},从{}复制到{}已完成！！！".format(filename, old_floder, new_floder))


def main(a):
    old_floder = "c:\\222"
    new_floder = old_floder+"副本"


    try:
        os.mkdir(new_floder)
    except:
        pass

    filenames = [ filename for filename in  os.listdir(old_floder) if os.path.isfile(old_floder+"\\"+filename)]
    for filename in filenames:

        copy(old_floder,new_floder,filename)





