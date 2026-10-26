#The final product is a pdf of a scatter plot showing the correlation in the data
all: scatterPlot.pdf scatterPlotCboe.pdf scatterPlotStooq.pdf

#Clears all intermediate files
clean:
	rm NASDAQandNYSE.txt volumeByDate.txt processed.txt volumeByDateCboe.txt organizedHolidays.txt processedCboe.txt scatterPlot.pdf scatterPlotCboe.pdf volumeByDateStooq.txt processedStooq.txt scatterPlotStooq.pdf
	echo 'All clean'

#Combine the csv files for both stock markets into one text file
NASDAQandNYSE.txt: NASDAQ_DATA.csv NYSE_DATA.csv
	find ~/SemesterProject -type f -name '*.csv' -exec cat {} + > NASDAQandNYSE.txt

#Organize the volume data into a column of dates with the total volume on that date - both markets added
volumeByDate.txt: NASDAQandNYSE.txt volumeByDate.py
	python3 volumeByDate.py > volumeByDate.txt

#Organize the messy jewishHolidays data into a column of holidays - Yom Kippur or one of the 3 Pilgrimage Holidays followed by the date
organizedHolidays.txt: jewishHolidays.txt organizeDates.awk
	gawk -f organizeDates.awk

#Make a file of each holiday date followed by the volume on the date, the average of the average volumes the preceding and following months, and the holiday name
processed.txt: organizedHolidays.txt volumeByDate.txt compare.py
	python3 compare.py > processed.txt

#Make a scatter plot of the data with lines of best fit and save it to a pdf
scatterPlot.pdf: processed.txt scatterPlot.py
	python3 scatterPlot.py

#Repeat with Cboe data
volumeByDateCboe.txt: cboeData.txt volumeByDateCboe.py
	python3 volumeByDateCboe.py > volumeByDateCboe.txt

processedCboe.txt: organizedHolidays.txt volumeByDateCboe.txt compareCboe.py
	python3 compareCboe.py > processedCboe.txt

scatterPlotCboe.pdf: processedCboe.txt scatterPlotCboe.py
	python3 scatterPlotCboe.py

#Repeat with Stooq stock data
volumeByDateStooq.txt: allStocksStooq.txt volumeByDateStooq.py
	python3 volumeByDateStooq.py > volumeByDateStooq.txt

processedStooq.txt: organizedHolidays.txt volumeByDateStooq.txt compareStooq.py
	python3 compareStooq.py > processedStooq.txt

scatterPlotStooq.pdf: processedStooq.txt scatterPlotStooq.py
	python3 scatterPlotStooq.py
