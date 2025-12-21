from datetime import date
def parse_date(date_string):
    """
    Converts a YYYY-MM-DD string into a date object.
    Assumes the format is correct.
    """
    year, month, day = map(int, date_string.split("-"))
    return date(year, month, day)
