def main():
    file = "NASDAQandNYSE.txt"
    f = open(file, "rt")
    line = f.readline()
    while line:
        fields = line.split(",")
        date = fields[0].split("/")
        if fields[1] != "#N/A N/A":
            #format all dates as yyyymmdd
            if len(date[1]) == 2 and len(date[0]) == 2:
                print(f'{date[2] + date[0] + date[1]}|{fields[1].strip()}')
            elif len(date[1]) == 1 and len(date[0]) == 2:
                print(f'{date[2] + date[0] + "0" + date[1]}|{fields[1].strip()}')
            elif len(date[1]) == 2 and len(date[0]) == 1:
                print(f'{date[2] + "0" + date[0] + date[1]}|{fields[1].strip()}')
            elif len(date[1]) == 1 and len(date[0]) == 1:
                print(f'{date[2] + "0" + date[0] + "0" + date[1]}|{fields[1].strip()}')
        line = f.readline()
        
main()
