
file = open("test.txt", "a")
print("\nAPPEND MODE:\n")
file.write("Hi i m Prateek Jain")
file.close()

file = open("test.txt", "r")
print(file.read())
