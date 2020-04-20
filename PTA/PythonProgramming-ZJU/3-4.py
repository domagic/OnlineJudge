pattern = input()
string = input()
index = string.rfind(pattern)
if index == -1:
    print("Not Found")
else:
    print("index = {}".format(index))
