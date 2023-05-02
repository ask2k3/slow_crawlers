class Square:
    def __init__(self, side_length):
        """__init__ is the dunder method that INITialises the instance.

        To create a square, we need to know the length of its side,
        so that will be passed as an argument later, e.g. with Square(1).
        To make sure the instance knows its own side length,
        we save it with self.side_length = side_length.
        """
        print("Inside init!")
        self.side_length = side_length

sq = Square(3241)


print(sq.side_length)