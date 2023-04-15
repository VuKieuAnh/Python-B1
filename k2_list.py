# Tạo list
l1 = [10, 101, "hfasf"]
l1[2] = 100
l2 = l1;
l2[2]= 0;
# Truy cập phần tử
# print(l1);

# print(10 in l1)
# print(l1 + l2)
# print(l1*2)

# duyet phan tu
# for e in l1:
#     print(e)

for i in range(len(l1)):
    # print(l1[i])

#   method
#     l1.append("jshfas");
    # l2.extend(l1)
    # print(l2)

#     sort
    print(l1.sort())
    print(l1)
#     Xoa
# l1.pop(1)
# print(l1)

l1.remove(101);
# print(l1)

# chuyen chuoi thanh list
t = list("hjahfjasf")
# print(t)

s = "hello world"
t2 = s.split();
# print(t2)

# print('--'.join(t2))

# object vaf value
s1 = 'h';
s2 = 'h';
print(s1 is s2);
demo1=['h'];
demo2=['h'];
print(demo1[0] is s1)

t3 = [1, 2, 3];
t3 = [1, 2, 3];
# Các method của list không trả về giá trị
# String chỉ trả về nhưng ko thay đổi
