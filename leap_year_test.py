def check_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return "Leap Year"
        else:
            return "Century Year"
    else:
        if year % 4 == 0:
            return "Leap Year"
        else:
            return "Neither century year nor leap year"


def test_it_should_be_century_year_if_input_is_1900():
    assert check_year(1900) == "Century Year"


def test_it_should_be_leap_year_if_input_is_400():
    assert check_year(400) == "Leap Year"


def test_it_should_not_be_century_year_and_leap_year_if_input_is_1999():
    assert check_year(1999) == "Neither century year nor leap year"


def test_it_should_be_leap_year_if_input_divided_by_4():
    assert check_year(2004) == "Leap Year"


def test_it_should_not_be_leap_year_if_input_cannot_be_divided_by_400_and_4():
    assert check_year(2003) == "Neither century year nor leap year"
