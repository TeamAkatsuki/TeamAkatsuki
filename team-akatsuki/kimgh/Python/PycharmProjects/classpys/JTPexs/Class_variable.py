class Family:
    lastname = '김'
    def __init__(self, name):
        self.firstname = name

father = Family("근근")
mother = Family("선선")
son = Family("봉봉")

print(Family.lastname)
