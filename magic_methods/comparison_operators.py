class Number:
    def __init__(self, number):
        self.number = number

    def __lt__(self, other):
        return self.number < other.number

    def __gt__(self, other):
        return self.number > other.number

    def __eq__(self, other):
        return self.number == other.number

    def __ne__(self, other):
        return self.number != other.number

    def __le__(self, other):
        return self.number <= other.number

    def __ge__(self, other):
        return self.number >= other.number
