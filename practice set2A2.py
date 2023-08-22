def leap_year(year) -> bool:
    """
    Determine if a given year is a leap year.

    Args:
        year : The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Test cases
years_check = [2003, 1995, 2000, 2023]

for year in years_check:
    if leap_year(year):
        print( year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
