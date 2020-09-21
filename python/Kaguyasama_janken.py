
# Kaguyasama_janken
"""
1. janken
2. 3times win
3. class syuuchiin
4. personal habit
"""

import random

# janken head
print("ジャンケンだYO！")
print("最初はドーン！　ジャンケンッ　ホイッ！！:")
yournum = random.randint(1,3)

# define function
def trans_num():
    global myhand
    global mynum
    myhand = input(":")
    if myhand == "goo":
        mynum = 1
    elif myhand == "choki":
        mynum = 2
    elif myhand == "paa":
        mynum = 3
    else:
        print("真面目にやってください！")

def trans_hand():
    if yournum == 1:
        yourhand = "goo"
        print(yourhand)
    elif yournum == 2:
        yourhand = "choki"
        print(yourhand)
    elif yournum == 3:
        yourhand = "paa"
        print(yourhand)

def fight():
    i = 1
    while i ==1:
        result = (yournum - mynum) % 3
        if result == 0:
            print("あいこでしょ！")
            trans_num()
            trans_hand()
            fight()
        elif result == 1:
            print("負けました～")
            break
        elif result == 2:
            print("私の勝ちですねっ！")
            break

# execute function
trans_num()
trans_hand()
fight()



