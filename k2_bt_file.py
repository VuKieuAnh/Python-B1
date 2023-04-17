# Tinh key cua 1 chuoi
def key_of_word(w):
    return ''.join(sorted(w));

def get_data(file_name):
    try:
        fin = open(file_name)
    except:
        print("Loi doc file")
    data = [];
    for line in fin:
        l = line.strip();
        data = data + l.split(" ");
    return data;

# print(get_data("demo1.txt"))
def print_similar_word(file_name):
    ws= get_data(file_name);
    d = {}
    for w in ws:
        s = key_of_word(w)
        if s not in d:
            d[s] = [w]
        else:
            d[s].append(w);
    return d;

print(print_similar_word("demo1.txt"))