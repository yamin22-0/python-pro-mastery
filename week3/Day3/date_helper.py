from datetime import datetime

def parse_date(text):

    text = text.strip()

    if not text:
        raise ValueError("Please enter a date.")

    try:
        return datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Please enter a valid date as YYYY-MM-DD.")

def days_until(due,today):

    return (due - today).days
