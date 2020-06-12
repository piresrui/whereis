import shutil
import unittest
import os
from whereis.finder import walk, create_pattern


class TestWalk(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.join(os.curdir, "test_dir")
        os.mkdir(self.path)
        os.mkdir(os.path.join(self.path, "sub1"))
        os.mkdir(os.path.join(self.path, "sub2"))
        f = open(os.path.join(self.path, "111.abc.123.txt"), "w+")
        f.close()
        f = open(os.path.join(self.path, "sub1", "abc_123_zxy.txt"), "w+")
        f.close()

    def tearDown(self) -> None:
        shutil.rmtree(self.path)

    def test_create(self):
        no_regex = create_pattern("one")
        regex = create_pattern("f.*2")

        test_str = "file2"
        test_str2 = "abcone123"
        test_str_fail = "abcabc"

        self.assertTrue(no_regex(test_str2), ["abc", "one", "123"])
        self.assertEqual(regex(test_str), ["", "file2", ""])
        self.assertIsNone(regex(test_str_fail))
        self.assertIsNone(no_regex(test_str_fail))

    def test_walk(self):

        total = []
        for value in walk(self.path, "abc"):
            total.append(value)
            print(value)

        self.assertEqual(len(total), 2)
