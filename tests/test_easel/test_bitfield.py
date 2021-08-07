import pickle
import unittest

from pyhmmer import easel


class TestBitfield(unittest.TestCase):

    def test_index_error(self):
        bitfield = easel.Bitfield(8)
        with self.assertRaises(IndexError):
            bitfield[9] = 1
        with self.assertRaises(IndexError):
            bitfield[-9] = 1

    def test_eq(self):
        b1 = easel.Bitfield(8)
        self.assertNotEqual(b1, object())

        b2 = easel.Bitfield(8)
        self.assertEqual(b1, b2)

        b3 = easel.Bitfield(7)
        self.assertNotEqual(b1, b3)

        b1.toggle(0)
        self.assertNotEqual(b1, b2)
        b2.toggle(0)
        self.assertEqual(b1, b2)

    def test_pickle(self):
        b1 = easel.Bitfield(8)
        b1[2] = b1[4] = True

        b2 = pickle.loads(pickle.dumps(b1))
        self.assertEqual(b1, b2)

        b3 = easel.Bitfield(8)
        self.assertNotEqual(b2, b3)
