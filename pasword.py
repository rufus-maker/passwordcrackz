import sys

import random
import datetime

print(" welcome to нΛㄈҚƐ尺 101 ㄈ尺ΛㄈҚƐ尺 ")
print(" you have 4 options")
print("1 : Normal pasword (words ) ")
print("2 : words and numbers ")
print("3 : passcode ")
print("4 :strong combination ")
x = input(" enter your choice : ")
x = int(x)
if x == 1:

    d = input(" enter the pasword  : ")
    l = "qwertyuiopasdfghjklzxcvbnm"
    s = " mnbvcxzasdfghjklpoiuytrewq "
    dx = len(d)
    e = l + s

    ti = datetime.datetime.now()
    print(" started cracking at ", ti)
    print("-" * 40)
    print("-" * 50)
    print("-" * 60)
    while True:
        pasword = "".join(random.sample(e, dx))
        de = datetime.datetime.now()
        lo = de - ti
        print(pasword)
        if pasword == d:
            print(" successfully cracked ")
            print(" it took ", lo)
            print(" you pasword is ", pasword)
            sys.exit()
elif (x == 2):
    v = input(" enter pasword : ")
    # numbers and words
    r = "qwertyuiopasdfghjklzxcvbnm"
    yi = "1234567890"
    lq = len(v)
    j = r + yi
    p = datetime.datetime.now()
    print(" started cracking at ", p)
    print("-" * 40)
    print("-" * 50)
    passs = "".join(random.sample(j, lq))
    while True:
        passs = "".join(random.sample(j, lq))
        print(passs)
        if passs == v:
            print(" succefully cracked pasword ")
            print(" your pasword is ", passs)
            sys.exit()
elif (x == 3):
    k = input(" enter pascode : ")
    f = " 1234567890"
    i = "0987654321"
    dw = k + i
    wr = len(k)
    print("-" * 40)
    print("-" * 50)
    print(" started cracking ")
    while True:
        po = "".join(random.sample(dw, wr))
        print(po)
        if po == k:
            print(" your pasword is ", po)
            sys.exit()
elif (x == 4):
    c = input(" enter strong pasword ")
    lu = "qwertyuiopasdfghjklzxcvbnm"
    so = " mnbvcxzasdfghjklpoiuytrewq "
    tx = " 1234567890 "
    sh = "!@#$%^&*()-_=+`~;:'[]{}\|<,>./?"
    sa = len(c)
    print("-" * 40)
    print("-" * 50)
    ll = lu + so + tx + sh
    while True:
        ty = "".join(random.sample(ll, sa))
        print(ty)
        if ty == c:
            print(" your pasword is ", ty)
            sys.exit()



