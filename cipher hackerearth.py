s = input()
k = int(input())
small = "abcdefghijklmnopqrstuvwxyz"
cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
char = "!@#$%^&*()_+-=`~,./<>?:;'{}[]|"
for i in s:
    if i in small:
        y = k % 26
        x = small.index(i) + 1
        alpha = 26 - x;
        if x + y > 26:
            b = y - alpha;
            print(small[b - 1], end="")
        else:
            print(small[x + y - 1], end="")
    if i in cap:
        y = k % 26
        x = cap.index(i) + 1
        alpha = 26 - x;
        if x + y > 26:
            b = y - alpha;
            print(cap[b - 1], end="")

        else:
            print(cap[x + y - 1], end="")
    if i in num:
        if i in num:
            y = k % 10
            x = num.index(i) + 1
            alpha = 10 - x;
            if x + y > 10:
                b = y - alpha;
                print(num[b - 1], end="")
            else:
                print(num[x + y - 1], end="")
    if i in char:
        print(i, end="")