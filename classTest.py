class Student(object):

    def __init__(self, cur_date=None):
        self.date = cur_date
        print("I'm init")
        self.score

    @property
    def sys(self):
        b = 3
        print("I'm @property 3")
        return b

    @property
    def score(self):
        a = 1
        print("I'm @property 1")
        return a



    @score.setter
    def score(self, value):
        # 1
        pass


if __name__ == "__main__":
    a = Student(1)
    a.sys
    print(a.score)
