
import time
def consumer():
    r=""
    while True:
        n = yield r
        if not n:
            return

        print("[consumer] consumer %s..."%n)
        time.sleep(1)
        r="200 ok"

def product(c):

    c.send(None)
    n=0
    while n<5:
        n=n+1
        print("[product] product %s"%n)
        r=c.send(n)
        print("[product] consumer return %s"%r)

c=consumer()

product(c)