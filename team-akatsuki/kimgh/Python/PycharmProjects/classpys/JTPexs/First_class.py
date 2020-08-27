class FourCal:

    def __init__(self, first, second):
        self.second = second
        self.first = first

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def min(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result


a = MoreFourCal(4, 2)
b = MoreFourCal(3, 8)
c = MoreFourCal(9, 4)

print(a.pow())
print(b.add())
print(c.mul())
