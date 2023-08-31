from datetime import datetime


def format_date(date):
    """
    Get date and format it

    Args:
        date: date to format

    Returns:
        Formatted date
    """
    try:
        return datetime.strptime(date, "%Y/%m")
    except ValueError:
        raise f"Not a valid date: {date}"


def stringnify_date(date):
    """
    Get stringnify date

    Args:
        date: date to stringnify

    Returns:
        Stringnify date with format (Mon day)
    """
    return date.strftime("%b %d")
