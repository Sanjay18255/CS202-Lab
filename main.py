def isLeapYear(year):
    if(year % 400 == 0):
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def CheckSingleYear():
    year = int(input("Enter a year to check: "))
    if isLeapYear(year):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is NOT a Leap Year")


def checkRange():
    start = int(input("Enter the starting year: "))
    end = int(input("Enter the ending year: "))
    print("Leap years between", start, "and", end, ":")
    for yr in range(start, end+1):
        if isLeapYear(yr):
            print(yr, end=" ")


print("Leap Year Checker")
print("------------------")
print("1. Check a single year")
print("2. List leap years in a range")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    CheckSingleYear()
elif choice == 2:
    checkRange()
else:
    print("Invalid choice. Please restart the program.")
