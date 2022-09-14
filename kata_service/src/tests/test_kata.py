import unittest

from resources.kata import KataWrapper

class TestKataWrapper(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.kata = KataWrapper()

    def test_kata_empty_string(self):
        # act
        result = self.kata._kata("", 5)
        # assert
        assert result == ""

    def test_kata_small_string(self):
        # act
        result = self.kata._kata("book", 7)
        # assert
        assert result == "book"
    
    def test_kata_single_breaking_string(self):
        # act
        result = self.kata._kata("bookshelf", 5)
        # assert
        assert result == "books\nhelf"
    
    def test_kata_multi_breaking_string(self):
        # act
        result = self.kata._kata("bookshelfwithbookstoberead", 5)
        # assert
        assert result == "books\nhelfw\nithbo\noksto\nberea\nd"
    
    def test_kata_break_with_starting_space_string(self):
        # act
        result = self.kata._kata("bookshelf behind a sofa", 10)
        # assert
        assert result == "bookshelf\nbehind a\nsofa"

    def test_kata_break_after_starting_space_string(self):
        # act
        result = self.kata._kata("bookshelf behind sofa", 11)
        # assert
        assert result == "bookshelf\nbehind sofa"
    
    def test_kata_break_inbetween_space_string(self):
        # act
        result = self.kata._kata("bookshelf behind sofa", 3)
        # assert
        assert result == "boo\nksh\nelf\nbeh\nind\nsof\na"
        