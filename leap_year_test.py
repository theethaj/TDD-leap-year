def check_year(year):
    if year % 400 == 0:
        return "Leap Year"
    elif year % 100 == 0:
        return "Century Year"


def test_it_should_be_century_year_if_input_is_1900():
    assert check_year(1900) == "Century Year"


def test_it_should_be_leap_year_if_input_is_400():
    assert check_year(400) == "Leap Year"

