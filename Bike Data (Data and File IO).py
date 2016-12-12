""" bike.py
 David Liben-Nowell
 Anna Rafferty
 This program analyzes bike share data.
"""

#finds average duration of each ride in terms of minutes, rounded to the nearest
#minute
def averageMinutes(seconds):
    averageMinutes = seconds / 60
    print("The average duration of each ride is approximately", "%.0f" % round(averageMinutes, 0), "minutes")

def main():
    """ Reads a file of bike share data and calculates statistics
        about the data.
        
        Note that all of the loading/printing is going in one function.
        There are more modular ways we might want to structure the code
        if we were using the statistics elsewhere, but this is okay
        for just interpreting a single file.
    """
    # The block of code below attempts to open the file with the bike share
    # data. If an IOError (input/output error) occurs, it prints an error
    # message and exits the program, since the rest of the program needs
    # to be able to read the file. If you get an error, check that you
    # haven't changed the name of the file and make sure if appears in the
    # same directory as bike.py.
    try:
        file = open("2015MayBikeShareData.csv")
    except IOError:
        print("ERROR!  2015MayBikeShareData.csv doesn't appear in the current directory.")
        exit(1)
        
        
    # The code below provides an example of looping through the data and
    # counting the number of rides that were taken in this period.
    numRides = 0
    totalDuration = 0
    numSmithJeff = 0
    startCount = 0
    numEnter = 0
    
    for line in file:
        numRides = numRides + 1
    
        # Divide this line of the file into the above fields; we'll only care about
        # a few of them so we'll ignore the others.
        fields = line.split(",")
        # We haven't seen this syntax before, but you should be able to guess what it
        # does. Try experimenting with it in the interpreter to confirm your guess.
        # From here on out in the code, you can ignore the fields variable - everything
        # you need has been stored in the variables on the left hand side.
        duration, startStation, endStation = int(fields[0]), fields[2], fields[4]
    
        # You'll add additional code within this for loop to complete the assignment.
        # There is one iteration of the loop for each line of the file.
        
        #sum all the durations in each ride
        totalDuration = totalDuration + duration
 
        #finding total number of rides that start at Smithsonian / Jefferson Dr & 12th St SW
        if startStation == 'Smithsonian / Jefferson Dr & 12th St SW':
            numSmithJeff = numSmithJeff + 1
                    
        #finding total number of bikes that arrive at Smithsonian / Jefferson station
        if endStation == "Smithsonian / Jefferson Dr & 12th St SW":
            numEnter = numEnter + 1
            
    #find average duration of each ride and convert to seconds
    averageDuration = (totalDuration / numRides) / 1000  
    
    #sum the number of bikes that have entered and left the station over the course of the data
    totalChange = numEnter - numSmithJeff
        
    # Files should always be closed when you are done with them.
    file.close()
    
    # Add additional print statements here
    print("There were", numRides, "total rides.")
    print("The average duration of each ride is", averageDuration, "seconds")
    
    #gives average duration of each ride in minutes and prints the result in a statement
    averageMinutes(averageDuration)
    
    print("The number of rides that started at Smithsonian / Jefferson Dr & 12th St SW is", numSmithJeff)
    
    if totalChange > 0:
        print("The number of bikes at Smithsonian / Jefferson station over the course of the data had increased by", totalChange, "units")
    elif totalChange < 0:
        print("The number of bikes at Smithsonian / Jefferson station over the course of the data has decreased  by", totalChange, "units")
    elif totalChange == 0:
        print("The number of bikes at Smithsonian / Jefferson station over the course of the data has not changed")

main()
   
