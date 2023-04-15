e2v = {'one': 'mot', 'two': 'hai'}
# chi so cua list là so,
# chi so cua dict
# print(e2v)
# print(e2v['one'])

# duyet
for i in e2v:
    print(e2v[i])
# kiem tra xem co nam trong key ko
# print('one' in e2v)
# print(e2v.values())

# Viet ham countCh(s) tra ve dict key la cac ky tu, value va so luan xua hien cua ky tu trong string s

def countCh(s):
    dict = {}
    for key in s:
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
    return dict

def countCh2(s):
    dict = {}
    for key in s:
        dict[key] = dict.get(key, 0) + 1;
    return dict

# print(countCh("abcàgajsgfjahsgfa"))
d=countCh("aabcàgajsgfjahsgfabc")
# Ham sort
# for k in sorted(d):
#     print(k, d[k])

#Tra cuu nguoc tu value sang key: tra ve key cua value v trong d
def getKey(d, value):
    for i in d:
        if value == d[i]:
            return i
    return None;
print(getKey(e2v, 'mot'))


b1 = True
def globalTest():
    b1 = False

globalTest()

d1={0:0, 1:1}
def globalTest2():
    d1[1]=2;

globalTest2()
print(d1)

# Bien toan cuc: neu dung bien tham chieu mutable thi cung tham chie
# Bien toan cuc: kieu immutable thi khac nhau, neu muon la cung 1 bien thi phai dung tu khoa globle

def globalTest3():
    global b1
    b1 = False




