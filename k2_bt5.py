s = "hello hello";
def countCh(s):
    dict = {}
    for key in s:
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
    return dict

def tanso(s):
    d = countCh(s);
    return (sorted(d, key=d.get, reverse=True))


print(tanso(s))
# bai cua Quang Anh
def tanso2(s:str)->list:
    f=[0 for _ in range(255)]
    for c in s:
        f[ord(c)] += 1
    g=[(f[i], i) for i in range(len(f)) if f[i] > 0]
    g.sort()
    g.reverse()
    return [chr(i[1]) for i in g]

print(tanso2(s))