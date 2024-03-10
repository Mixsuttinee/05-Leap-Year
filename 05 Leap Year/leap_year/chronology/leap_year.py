# leap_year.py

"""Leap Year utility"""

# Standard Library

# 3rd Party Library

# Project Library


#---------------------------------------------------------------------------------
def is_leap_year(year: int) -> bool:
    """Determine if year is a leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False

