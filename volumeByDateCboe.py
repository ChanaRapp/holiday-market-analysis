def main():
    file = "cboeData.txt"
    f = open(file, "rt")
    line = f.readline()
    while line:
        fields = line.split(",")
        date = fields[0].split("-")
        print(f'{date[0] + date[1] + date[2]}|{fields[13].strip()}')
        line = f.readline()
        
main()

