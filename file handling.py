f=open("test.txt",'r+')
f.write("my first file\n")
f.write("This file\n\n")
f.write("contains three lines\n")

print(f.read(4))    # read the first 4 data
print(f.read(4))    # read the next 4 data
print(f.read())     # read in the rest till end of file
f.close()
