f = open("stocks.txt", "r")
def read(file):
    file_list=file.readlines()
    name = []
    for lines in file_list[1:]:
        split = lines.split(" ")
        if float(split[3]) > 100:
            name.append(split[0])
    return  name
print(read(f))
f.close()