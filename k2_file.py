# ghi
import dbm

fout = open('words.txt', 'w');
fout.write("l1 \n");
fout.write("l2 \n");
fout.write(str(42));
# toan tu fomart
fout.write("test %d" %40);
fout.write("test %d - %d %d" %(40, 2022, 30));
fout.close();


# Doc
try:
    fin = open("words1.txt")
    print((fin.read()))
except:
    print("gi")


#     doc ghi file kieu key, value
db = dbm.open("dbkv", "c");

db["nguyen"] = "1";
db["tran"] = "2";
# db.close();


print(db['nguyen'])