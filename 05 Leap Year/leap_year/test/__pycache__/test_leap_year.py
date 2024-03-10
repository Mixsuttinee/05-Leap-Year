# test_leap_year.py

"""Test cases for leap year."""


# Standard Library

# 3rd Party Library
import pytest

# Project Library
from chronology.leap_year import is_leap_year


#-------------------------------------------------------
@pytest.mark.parametrize(
        "year",
        [
            2001, 2002, 2003, 2005, 2006, 2007,
        ]
)
def test_year_is_not_divisible_by_4(year: int):
    """Return false if year is not a leap year."""
    # Arrange
    expected_result = False

    # Act
    result = is_leap_year(year)

    # Assert
    assert result == expected_result

#-------------------------------------------------------
@pytest.mark.parametrize(
        "year",
        [
            1700, 1800, 1900, 2100, 2200,
        ]
)
def test_year_is_divisible_by_100_but_not_400(year: int): 
    """Return false if year is not a leap year."""
    # Arrange
    expected_result = False

    # Act
    result = is_leap_year(year)

    # Assert
    assert result == expected_result 

#-------------------------------------------------------
@pytest.mark.parametrize(
        "year",
        [
            2024, 2020, 2000,
        ]
)
def test_year_is_divisible_by_4_but_not_100(year: int): 
    """Return true if year is a leap year."""
    # Arrange
    expected_result = True

    # Act
    result = is_leap_year(year)

    # Assert
    assert result == expected_result 
