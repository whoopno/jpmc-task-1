import client
import unittest

class TestClientFile(unittest.TestCase):

    def test_getRatio(self):
        result = client.getRatio(8, 0)
        self.assertEqual(result, None)
        result = client.getRatio(20, 5)
        self.assertEqual(result, 4)
        result = client.getRatio(5, 2)
        self.assertEqual(result, 2.5)