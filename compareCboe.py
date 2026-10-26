#Make dictionary with 1st value as key, 2nd as data added up
def makeDict(data):
    f = open(data)
    line = f.readline()
    myDict = {}
    while line:
        fields = line.split("|")
        if fields[0] in myDict:
            try: myDict[fields[0]] += int(fields[1])
            except: myDict[fields[0]] += 0
        else:
            try: myDict[fields[0]] = int(fields[1])
            except: myDict[fields[0]] = 0
        line = f.readline()
    f.close()
    return myDict

def main():
    allDates = makeDict("./volumeByDateCboe.txt") #Make dictionary with key=date:data=summed volumes from that day
    g = open("organizedHolidays.txt")
    line = g.readline()
    while line: #loop through all the lines - each containing holiday|date
        fields = line.split("|") #Split the line into an array of [holiday, date]
        date = fields[1].strip()
        totalVolumeBefore = 0
        totalDaysBefore = 0
        totalVolumeAfter = 0
        totalDaysAfter = 0
        #Loop through all the dates in the dictionary to find the average volume from the months before and after our date
        for d in allDates:
            if d[:4] == date[:4]: #If it's in the same year as the holiday
                if int(d[4:6]) == int(date[4:6]) - 1: #If it's in the month before
                    totalDaysBefore += 1
                    totalVolumeBefore += allDates[d]
                if int(d[4:6]) == int(date[4:6]) + 1: #If it's in the month after
                    totalDaysAfter += 1
                    totalVolumeAfter += allDates[d]
        #Calculate average volume month before and after, except if total days before is 0, set it to 0
        try: averageBefore = totalVolumeBefore / totalDaysBefore
        except: averageBefore = 0
        try: averageAfter = totalVolumeAfter / totalDaysAfter
        except: averageAfter = 0
        #If we have the volume for that date and the average for the months before and after
        if date in allDates and averageBefore and averageAfter:
            # print the date|the volume on that day|the average of the volume the month before and after|the holiday
            print(f"{date}|{allDates[date]}|{(averageBefore + averageAfter) / 2}|{fields[0]}")
        line = g.readline()
    g.close()
main()
