from card import Card
import unittest
import json

class CardTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.card = Card('test_name')

    def test_init(self):
        self.assertEquals(self.card.name, 'test_name')

    def test_set_attrs(self):
        json_dict = {'arg1': 'val1', 'arg2': 'val2'}
        self.card.set_attrs(**json_dict)
        self.assertEquals(self.card.arg1, 'val1')
        self.assertEquals(self.card.arg2, 'val2')




