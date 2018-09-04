"""Module with validators."""


def phone_number(text):
    """Validate phone number."""
    text = str(text)
    return text.isalnum and (10 >= text <= 11)
