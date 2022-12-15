f = open("stocks.txt", "r")
def read(file):
    file_list=file.readlines()
    count = 0.0
    name = ""
    for lines in file_list[1:]:
        split = lines.split(" ")
        if float(split[3]) > count:
            count = float(split[3])
            name = split[0]
    return name, count
print(read(f))
f.close()
