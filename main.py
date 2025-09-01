def is_leap_year(year):
    """Return True if the year is a leap year, else False."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def check_single_year():
    """Check if a single year is a leap year."""
    year = int(input("Enter a year to check: "))
    if is_leap_year(year):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is NOT a Leap Year")

def check_range():
    """Check all leap years in a given range."""
    start = int(input("Enter the starting year: "))
    end = int(input("Enter the ending year: "))
    print(f"\nLeap years between {start} and {end}:")
    for year in range(start, end + 1):
        if is_leap_year(year):
            print(year, end=" ")
    print()  # for newline

if __name__ == "__main__":
    print("Leap Year Checker")
    print("------------------")
    print("1. Check a single year")
    print("2. List leap years in a range")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        check_single_year()
    elif choice == 2:
        check_range()
    else:
        print("Invalid choice. Please restart the program.")