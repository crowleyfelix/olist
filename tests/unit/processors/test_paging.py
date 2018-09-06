from unittest import TestCase
from unittest.mock import patch, Mock
from app.processors import paging


class TestPaging(TestCase):
    def test_process(self):
        with self.subTest("when is in first page"):
            self.assertEqual(
                paging.process(1, 10, 21),
                {
                    "current": 1,
                    "size":    10,
                    "max_size": 10,
                    "next": 2
                })

        with self.subTest("when is in middle page"):
            self.assertEqual(
                paging.process(2, 10, 21),
                {
                    "current": 2,
                    "size":    10,
                    "max_size": 10,
                    "previous": 1,
                    "next": 3
                })

        with self.subTest("when is in last page"):
            self.assertEqual(
                paging.process(3, 10, 21),
                {
                    "current": 3,
                    "size":    1,
                    "max_size": 10,
                    "previous": 2,
                })

        with self.subTest("when is over page"):
            self.assertEqual(
                paging.process(4, 10, 21),
                {
                    "current": 4,
                    "size":    0,
                    "max_size": 10,
                    "previous": 3,
                })

        with self.subTest("when max size is less than all count"):
            self.assertEqual(
                paging.process(1, 10, 6),
                {
                    "current": 1,
                    "size":    6,
                    "max_size": 10,
                })

    def test_filter(self):
        items = list(range(0, 10))
        page = 4
        size = 2

        self.assertEqual(paging.filter(items, page, size), [6, 7])
