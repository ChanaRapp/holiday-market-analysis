BEGIN{
    FS = " "
    OFS = "|"
    file = "jewishHolidays.txt"
    outputFile = "organizedHolidays.txt"
    #make array of all month names corresponding to their number
    months["January"] = "01"
    months["February"] = "02"
    months["March"] = "03"
    months["April"] = "04"
    months["May"] = "05"
    months["June"] = "06"
    months["July"] = "07"
    months["August"] = "08"
    months["September"] = "09"
    months["October"] = "10"
    months["November"] = "11"
    months["December"] = "12"
    while (getline < file){
	if($1 !~ /[0-9]/){ #if it has a day of the week
	    if($1 !~ /(Sat\.|Sun\.)/){ #don't include it if it's on the weekend
		if ($5 ~ /\*/){ #only include it if the holiday name is followed by * indicating a work prohibition 
		    #format the dates uniformly
		    if (length($2) == 2) 
			    print substr($5, 1, length($5) - 1), $4 ""  months[$3] "" $2 > outputFile
			else
			    print substr($5, 1, length($5) - 1), $4 ""  months[$3] "0" $2 > outputFile
		}
		if ($6 ~ /[K].+\*$/){ #if it's a 2 word holiday - Yom Kippur
		    if (length($2) == 2)
			print $5 " " substr($6, 1, length($6) - 1), $4 ""  months[$3] "" $2 > outputFile
		    else
			print $5 " " substr($6, 1, length($6) - 1), $4 ""  months[$3] "0" $2 > outputFile
		}
	    }
	} else {
	    if ($4 ~/\*/){ #Same as before, if there is no day of the week
	        if (length($1) == 2)
		    print substr($4, 1, length($4) - 1), $3 ""  months[$2] "" $1 > outputFile
                else
		    print substr($4, 1, length($4) - 1), $3 ""  months[$2] "0" $1 > outputFile
            }
            if ($5 ~ /[K].+\*$/){
		if (length($1) == 2)
		    print $4 " " substr($5, 1, length($5) - 1), $3 ""  months[$2] "" $1 > outputFile
                 else
		     print $4 " " substr($5, 1, length($5) - 1), $3 ""  months[$2] "0" $1 > outputFile
            }
       }
    }
}
