def col(x):
        y=[x]
        while x > 1:
                if x%2 = 0: x = x // 2
                else: x = x * 3 + 1
                y.append(x)
        return y

try:
        z = col(int(input("start: ")))
        print(z)
except: pass