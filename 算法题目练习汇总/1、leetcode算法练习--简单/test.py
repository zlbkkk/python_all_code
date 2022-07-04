from gevent import monkey;monkey.patch_all()
from gevent import spawn
import time
#
# def heng():
#     print("哼")
#     time.sleep(2)
#     print("哼")
#
#
# def ha():
#     print("哼")
#     time.sleep(2)
#     print("哼")
#
#
# start_time = time.time()
# g1=spawn(heng)
# g2=spawn(ha)
#
# # 以下的.join()必须要加入，要不然函数没运行完就退出了，是固定写法
# g1.join()
# g2.join()
#
# print(time.time()-start_time)
url_dict={}

with open("c:\\1.txt") as f:
    data = f.readlines()
    print(data)
    for url in data:
        url_key=url.split()[0]
        if url_key not in url_dict:
            url_dict[url_key]=1
        else:
            url_dict[url_key]=url_dict.get(url_key)+1

    print(url_dict)

from collections import Iterator

import json
info=json.dumps({"name":"李小龙",'age':66,'love':"cat"})
fp=open('testdict1.txt','w+',encoding='utf-8')
fp.write(info,encoding="utf-8")