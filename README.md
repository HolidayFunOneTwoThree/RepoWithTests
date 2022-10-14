# RepoWithTests
This is a public repository for some tests demonstration.

1. Test_Dif_Btw_Dates.py demonstrates how to calculate number of days between two dates from std input without using additional libraries.

  It includes several functions:
  
    isLeapYear - is used to check how many days in a year and in february.
    
    getNumberOfDaysInMonth - distiguish how many days in a given month.
    
    getDaysFrom1890 - calculates number of days between given date and 01.01.1890, it simplifies the code compare to calculation of days between two given days directly.

    compareResultWithLibFunction - function specifically added for "unit" testing

    isDateCorrect - check boundaries of entered dates

    inputReading - is the main function

    if __name__ == '__main__': added to be able to use functions from this file withou unnecessary calls
