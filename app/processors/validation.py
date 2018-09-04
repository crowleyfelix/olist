"""Module with validators."""


def phone_number(text):
    """Validate phone number."""
    text = str(text)
    return text.isnumeric() and (10 <= len(text) <= 11)
