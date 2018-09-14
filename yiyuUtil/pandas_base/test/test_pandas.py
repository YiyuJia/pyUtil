from unittest import TestCase

from yiyuUtil.pandas_base import clean

class TestClean(TestCase):
    def test_is_string(self):
        s = (clean)
        self.assertTrue(isinstance(s))