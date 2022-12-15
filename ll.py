f = open("stocks.txt", "r")
def read(file):
    file_list=file.readlines()
    name = []
    for lines in file_list[1:]:
        split = lines.split(" ")
        if float(split[2]) > 100:
            name.append(split[0])
    return  name
def stocks(txt):
        f = open("new.txt","w")
        return f.writelines(txt)
print(stocks(read(f)))

    