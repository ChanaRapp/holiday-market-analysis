import matplotlib.pyplot as plt
import math
import numpy

xyArray = []
f = open("processed.txt")
line = f.readline()
while line:
    fields = line.split('|')
    try: ratio = float(fields[1]) / float(fields[2])
    except: ratio = 0
    year = int(fields[0][:4])
    if "Yom" in fields[3]:
        if ratio: xyArray.append([year, math.log(ratio), 'k'])
    if year != 2020:
        if "Sukkot" in fields[3] or "Pesach" in fields[3] or "Shavuot" in fields[3]:
            if ratio: xyArray.append([year, math.log(ratio), 'c']) 
    line = f.readline()

x1 = [xyArray[i][0] for i in range(len(xyArray)) if xyArray[i][2] == 'c']
y1 = [xyArray[i][1] for i in range(len(xyArray)) if xyArray[i][2] == 'c']

x2 = [xyArray[i][0] for i in range(len(xyArray)) if xyArray[i][2] == 'k']
y2 = [xyArray[i][1] for i in range(len(xyArray)) if xyArray[i][2] == 'k']

#prepare the figure
f = plt.figure()

#do both scatter plots
plt.scatter(x1, y1, c='c', s=50)
plt.scatter(x2, y2, c='k', s=50)

#set y height
plt.ylim(-.55, .55)

#Add lines of best fit
m, b = numpy.polyfit(x1, y1, 1)
plt.plot(x1, m*numpy.array(x1) + b, color = 'c', label='Pilgrimage Holidays')

m, b = numpy.polyfit(x2, y2, 1)
plt.plot(x2, m*numpy.array(x2) + b, color = 'k', label='Yom Kippur')

# specify the x and y axis labels
plt.xlabel("Year")
plt.ylabel("Ratio of volume on holiday/average volume\nof month preceding and following")
plt.title("Bloomberg Terminal Data")

#Add the legend to the plot
plt.legend()
# render the plot on the screen
plt.show()
#Save the plot as a pdf
f.savefig("scatterPlot.pdf")
