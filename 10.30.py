#玩家抽牌
def num(total):
    ans = total[0] + float(deck.pop(0))
    total.insert(0,ans)
    total.pop(1)
    return total
#電腦抽牌
def num1(com):
    ans = com[0] + float(deck.pop(0))
    com.insert(0,ans)
    com.pop(1)
    com1 = com[0]
    return com
#電腦偵測是否要再一張牌
def rule(com1):
    shuffle(chance_big)
    shuffle(chance_mini)
    shuffle(chance_small)
    #總點數為 0.5 時抽牌
    if com[0] + 9 <= 10.5:
        num(com)
    #總點數 < 3時抽牌
    elif com[0] < 3:
        num(com)
    #總點數 3~6 時有90%的機率抽牌 否則結束回合
    elif com[0] > 3 and com[0] < 6:
        if chance_mini[0] == "a":
            num(com)
        else:
            finall.insert(0,"5")
    #總點數 6~7 時有20%的機率抽牌 否則結束回合
    elif com[0] > 6 and com[0] < 7:
        if chance_small[0] == "b":
            num(com)
        if chance_small[0] == "a":
            finall.insert(0,"5")
    #當總點數 > 7 時  不抽牌
    elif com[0] <= 10.5:
        print(float(com[0]),"點",",","結束這個回合")
    #判斷誰贏
        if total[0] > com[0]:
            com[0] = 0
            print("你贏了")
            lose_com.append(fiftwo-len(deck)-lose[-1])
            print("\n","我有",lose_com[-1],"張牌","\n")
        elif total[0] < com[0]:
            com[0] = 0
            print("你輸了")
            lose.append(fiftwo-len(deck)-lose_com[-1])
            print("\n","你有",lose[-1],"張牌","\n")
        elif total[0] == com[0]:
            com[0] = 0
            fiftwo - (max(lose[-1],lose_com[-1]) - len(deck))
            print("平手啦")
        finall.insert(0,"5")
    return com1


from random import shuffle
order = ["A","A","A","A", "2", "2", "2","2", "3", "3", "3","3", "4","4", "4", "4","5","5","5" ,"5","6","6","6", "6","7","7","7", "7","8","8","8", "8", "9", "9", "9","9","10","10","10", "10","j","j","j", "j","q","q","q", "q","k","k","k", "k"]
deck = []
number = []
total = [0]
finall = [0]
lose = [0]
lose_com = [0]
fiftwo = 52
#洗牌
for j in order:
    number.append(j)
    shuffle(number)
for i in range(0,52):
    deck.append(number[i])
for o in range(0,52):
    if deck[o] == "j" or deck[o] == "q" or deck[o] == "k":
        deck[o] = 0.5
    if deck[o] == "A":
        deck[o] = 1
while len(deck) > 0:
    next = "" 
    total = [0]
    finall = [0]
    print("你抽到",number.pop(0))
    print("目前是:",num(total),"點")
    while next != "否":
        next = input("是否要下一張(是/否):")
        while next != "否" and next != "是":
            print("輸錯")
            next = input("是否要下一張(是/否):")
        if len(deck) == 0:
            lose_com.append(fiftwo-len(deck)-lose[-1])
            print("\n","我有",lose_com[-1],"張牌","\n")
            break
        if next == "否":
            break
        print("你抽到",number.pop(0))
        print("目前是:",num(total),"點")
        if total[0] > 10.5:
            print("你爆了")
            total[0] = 0
            break


    if len(deck) == 0:
        print("\n","俺のターン","\0","ドロー!","\n","阿怎麼沒牌了!?","\n")
    else:
        print("\n","俺のターン","\0","ドロー!","\n")
    if len(deck) == 0:
        lose_com.append(fiftwo-len(deck)-lose[-1])
        print("\n","我有",lose_com[-1],"張牌","\n")
        break
    finall = [0]
    chance_big = ["a","a","b"]
    chance_small = ["a","a","a","a","b"]
    chance_mini = ["a","a","a","a","a","a","a","a","a","b"]
    com = [0]
    com1 = 0
    while finall[0] == 0:
        print("目前是:",rule(com[0]),"點","\n")
        if len(finall) == 1:
            print("我抽到",number.pop(0))
        if len(deck) == 0:
            lose_com.append(fiftwo-len(deck)-lose[-1])
            print("\n","我有",lose_com[-1],"張牌","\n")
            break
        if com[0] > 10.5:
            print("目前是:",com[0],"點")
            com[0] = 0
            print("我爆了")
            if total[0] == 0 and com[0] == 0:
                com[0] = 0
                print("看來,你也爆了呢")
                fiftwo - (max(lose[-1],lose_com[-1]) - len(deck))
            else:
                com[0] = 0
                print("你贏了")
                lose_com.append(fiftwo-len(deck)-lose[-1])
                print("\n","我有",lose_com[-1],"張牌","\n")
            break
    if com[0] != 0:
        if total[0] > com[0]:
            print("你贏了")
            lose_com.append(fiftwo-len(deck)-lose[-1])
            print("\n","我有",lose_com[-1],"張牌","\n")
        elif total[0] < com[0]:
            print("你輸了")
            lose.append(fiftwo-len(deck)-lose_com[-1])
            print("\n","你有",lose[-1],"張牌","\n")
        elif total[0] == com[0]:
            fiftwo - (max(lose[-1],lose_com[-1]) - len(deck))
            print("平手啦")
if lose[-1] > lose_com[-1]:
    print(lose[-1],"V.S",lose_com[-1])
    print("最終結果:YOU LOSE")
if lose[-1] < lose_com[-1]:
    print(lose[-1],"V.S",lose_com[-1])
    print("最終結果:YOU WIN")
if lose[-1] == lose_com[-1]:
    print(lose[-1],"V.S",lose_com[-1])
    print("DRAW")







