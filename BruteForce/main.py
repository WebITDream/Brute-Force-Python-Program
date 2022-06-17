import time, os
sentence = "test that this program work"
current = ""
all_letts = " abcdefghijklmnopqrstuvwxyz"
while sentence != current:
    for x in sentence:
        for i in all_letts:
            if x == i:
                current = current + x
                time.sleep(0.05)
                os.system("cls")
                print(current)