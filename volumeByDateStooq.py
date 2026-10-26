def makeDict(data):
    f = open(data)
    line = f.readline()
    myDict = {}
    while line:
        fields = line.split(",")
        if fields[2] in myDict:
            try: myDict[fields[2]] += int(fields[8])
            except: myDict[fields[2]] += 0
        else:
            try: myDict[fields[2]] = int(fields[8])
            except: myDict[fields[2]] = 0
        line = f.readline()
    f.close()
    return myDict

def main():
    file = "allStocksStooq.txt"
    allDates = makeDict(file)
    for date in allDates:
        print(f'{date}|{allDates[date]}')
        
main()

