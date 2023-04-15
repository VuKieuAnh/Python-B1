# (1)
l1 = [2, 3, 4, 5, 6];
def remove1(list):
    list.pop(0);
    list.pop(len(list) -1);
    return list;

# remove1(l1);
# print(l1)
def remove2(list):
    list.pop(0);
    list.pop(len(list) - 1);
    return None;

# print(remove2(l1));
# print(l1)

def has_dup(list):
    for i in range(len(list)):
        count = 0;
        for j in range(len(list)):
            if (j!=i and list[j]==list[i]):
                    return True;
    return False;


# print(has_dup([2, 3, 4, 5, 7]))
# def countCh2(s):
# dict = {}
#     for key in s:
#         if key in dict:
#             dict[key] += 1
#         else:
#             dict[key] = 1
#     return dict

def idict(d):
    dict = {}
    for key in d:
        value = d[key];
        if(value in dict):
            dict[value].append(key);
        else:
            dict[value] = [key];

    return dict

# print(idict({"h":1, "e":1, "l":2, "o": 1}));
# (5)
def has_duplicate(d):
    for key in d:
        for key2 in d:
            count = 0;
            if (d[key] == d[key2]):
                count+=1;
                if count==2:
                    return True;
    return False;

print(has_duplicate({"h":1, "e":1, "l":2, "o": 4}))






