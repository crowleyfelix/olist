from unittest import TestCase
from app.processors import validation


class TestValidation(TestCase):
    def test_validation(self):
        self.assertTrue(validation.phone_number("0123456789"))
        self.assertTrue(validation.phone_number("01234567890"))
        self.assertFalse(validation.phone_number("012345678901"))
        self.assertFalse(validation.phone_number("01234567890x"))

    def test_year_month(self):
        self.assertTrue(validation.year_month("2018-09"))
        self.assertFalse(validation.year_month("201809"))
        self.assertFalse(validation.year_month("2018-22"))
