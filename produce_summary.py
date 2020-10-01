reports = ["um-deliveries-20140519.txt", "um-deliveries-20140520.txt", "um-deliveries-20140521.txt"]    #creates a list of the report file names

for day in range(len(reports)):                                                                         #starts the loop to iterate through the different reports
    print(f"Day {day + 1}")                                                                             #prints the day for the report shown
    the_file = open(reports[day])                                                                       #opens the file specified
    for line in the_file:                                                                               #starts the loop to perform the bulk of the work
        line = line.rstrip()                                                                            #turns a line of the file into a string
        words = line.split('|')                                                                         #turns the string into a list

        melon = words[0]                                                                                #defines variable 'melon' from the first item in the list
        count = words[1]                                                                                #defines variable 'count' from the second item in the list
        amount = words[2]                                                                               #defines variable 'amount' from the third item in the list

        print("Delivered {} {}s for total of ${}".format(                                               #print the line in the new format
            count, melon, amount))
    the_file.close()                                                                                    #close the file
