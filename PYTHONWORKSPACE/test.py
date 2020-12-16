# a = {}
# with open('a.txt') as f:
#     for line in f:
#         key = line.strip()
#         print(key)
    


# f = open("C:\\Users\\hyunjin\\Desktop\\studypython\\PYTHONWORKSPACE\\a.txt","r")
# line = f.readline()
# print(line)

# f.close()
a = {}

with open("C:\\Users\\hyunjin\\Desktop\\studypython\\PYTHONWORKSPACE\\a.txt") as f:
    count = 0
    for line in f:

        ++count
        if(count % 9 == 0):
            key = line.strip()
            print(key)
            


