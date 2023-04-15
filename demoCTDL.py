# String
# String không cho gán các thành phần của chuỗi thành phần tử
# slice
s = 'Hello'
# print(s[1:4])
# Bỏ qua phần đầu thì mặc định là 0, bỏ qua phần sau thì mặc định là len

def countOf(w, l,n):
    count=0;
    i = n;
    while i <len(w):
        if(w[i] == l):
            count +=1;
        i+=1;
    return count;

# print(countOf("hello", "l", 0))

# Method
# Toan tu in
# print('he' in 'Hello')
# so sanh: so sanh tung ky tu: neu khac nhau thi dung lai luon
# w = 'hello';
# if s > 'hallo':
#     print('sau')
# else:
#     print('trc')

# Viet ham in_both(w1, w2) tra ve cac ky tu xuat hien trong ca w1 va w2
def in_both(w1, w2):
    arr = []
    i=0;
    while i < len(w1):
        if w1[i] in w2:
            arr.append(w1[i])
        i+=1;
    return arr

print(in_both("xin chao", "an xin"))







