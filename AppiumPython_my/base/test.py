# from timefrom import tqdm
from tqdm import tqdm

import time
# from tqdm import tqdm
mylist = [1,2,3,4,5,6,7,8]
for i in tqdm(mylist):
    time.sleep(1)
print("执行完毕")