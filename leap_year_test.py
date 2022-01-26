def check_year(year):
    if year % 100 == 0:
        return "Century Year"


def test_it_should_be_century_year_if_input_ends_with_00():
    assert check_year(2000) == "Century Year"

