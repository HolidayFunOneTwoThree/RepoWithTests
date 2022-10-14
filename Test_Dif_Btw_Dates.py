# is leap year
def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# get number of days in month
def getNumberOfDaysInMonth(year, month):
    if month == 2 and isLeapYear(year):
        return 29
    else:
        listOfDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return listOfDays[month - 1]


# get number of days between 01 01 1890 and date
def getDaysFrom1890(day, month, year):
    days = day - 1

    for i in range(1, month):
        days += getNumberOfDaysInMonth(year, i)

    for i in range(1890, year):
        if isLeapYear(i):
            days += 366
        else:
            days += 365
    return days


# Function to compare results with datetime function
def compareResultWithLibFunction(year1, month1, day1, year2, month2, day2, yourResultDays):
    from datetime import datetime
    libResultDays = datetime(year2, month2, day2) - datetime(year1, month1, day1)
    if yourResultDays == libResultDays.days:
        print("Your result matches with datetime library function")
    else:
        print("Your result does not match with datetime library function")


# Check if the input date is correct
def isDateCorrect(day, month, year):
    if year < 1900:
        print("Year must be >= 1900")
        return False

    if year > 2010:
        print("Year must be <= 2010")
        return False

    if month < 1:
        print("Month must be >= 1")
        return False

    if month > 12:
        print("Month must be <= 12")
        return False

    if day < 1:
        print("Day must be >= 1")
        return False

    if day > getNumberOfDaysInMonth(year, month):
        print("Day must be <= number of days in month")
        return False

    return True


# Main function, includes input and calculation of days
def inputReading():
    keepReading = True
    while (keepReading):

        print("Enter two dates in format \"dd mm yyyy, dd mm yyyy\"")
        inputString = input()
        try:
            listOfDates = str(inputString).split(",")

            day1, month1, year1 = map(int, listOfDates[0].strip().split())
            if isDateCorrect(day1, month1, year1):
                day2, month2, year2 = map(int, listOfDates[1].strip().split())
                if isDateCorrect(day2, month2, year2):
                    daysBetween1890AndDate1 = getDaysFrom1890(day1, month1, year1)
                    daysBetween1890AndDate2 = getDaysFrom1890(day2, month2, year2)
                    daysBetweenDates = daysBetween1890AndDate2 - daysBetween1890AndDate1
                    if daysBetweenDates < 0:
                        day1, month1, year1, day2, month2, year2 = day2, month2, year2, day1, month1, year1
                        daysBetweenDates = -daysBetweenDates

                    print(
                        f"{day1:02d} {month1:02d} {year1:04d}, {day2:02d} {month2:02d} {year2:04d}, {daysBetweenDates}")

                    compareResultWithLibFunction(year1, month1, day1, year2, month2, day2, daysBetweenDates)
                    keepReading = False

        except:
            print("Input error, try again")


# Main function call
if __name__ == '__main__':
    inputReading()
