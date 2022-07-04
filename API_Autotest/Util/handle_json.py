import os
import sys
import json

base_path = os.path.dirname(os.getcwd())
sys.path.append(base_path)


def read_json(file_name=None):
    if file_name == None:
        file_path = base_path+"/Config/user_data.json"
        # file_path = base_path + "/Mock/config.json"
    else:
        file_path = base_path+file_name

    with open(file_path,encoding="utf-8") as f:
        data = json.load(f)
    return data


def get_value(key,file_name=None):
    data = read_json(file_name)
    return data.get(key)
    # return data[key]  这样写，如果没有key值，会报错，使用get比较好

def wrire_value(data):
    data_value = json.dumps(data)
    with open(base_path+"/Config/cookie.json","w",encoding='utf-8') as f:
        f.write(data_value)


if __name__=="__main__":

    # wrire_value()
    print(get_value("register"))
