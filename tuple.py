# (1)
t = ('a', 'b', 'c');
# Mot phan tu phai co dau phay
t2 = ('a',);
t3 = ();
print()

# Truy cap
# Cac gia tri khong thay doi duoc
t = ('a', 'b', 'c', 'd', 'e')
# t[0]='a'; => loi
t2 = ('b',) + t[1:]

print(t[1:3]);
# So sanh
t3=('1',)
t4=('2',)

# Doi cho khac 1 chut
t3, t4 = t4, t3

# cac cach gan trong tuple
# t1, t2 = 'a@gmail.com'.split('@')
# t1, t2 = 'ab';
# t1, t2 = [1, 2];

# ham dung nhieu tham so
def sum2(*x):
    s=0
    for i in x:
        s += i
    return s

print(sum2(1, 2))
print(sum2(1, 2, 3))

# tuple, list
a='abc'
l = [0, 1, 2]

for t in zip(a, l):
    # moi 1 phan tu la 1 tuple
    print(t)

# dict, tuple
d = {'a':0, 'b':1, 'c':2}
for k, v in d.items():
    print(k, v)

t = [('a', 1), ('b', 2), ('c', 3)];
d = dict(t)
print(d)