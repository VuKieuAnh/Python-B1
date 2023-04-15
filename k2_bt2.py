def avoids(word, forbidden):
    i=0;
    while i < len(word):
        if(word[i] in forbidden):
            return False
        i+=1;
    return True

print(avoids("Vu thi kieu anh", "ajfhjas"))

def user_only(word, avaiable):
    i = 0;
    check = True;
    while i < len(word):
        if (not (word[i] in avaiable)):
            return False;
        i += 1;
    return check;

print(user_only("Vu thi kieu anh", "ajfhjas"))

def user_all(word, required):
    i = 0;
    check = False;
    while i < len(word):
        if (word[i] in required):
            check= True;
        i += 1;
    return False;

def user_all(word, required):
    return user_only(required, word)

s='Hello';
print(s[-1:-len(s)-1: -1])

