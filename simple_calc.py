import fire


class Calc(object):
    """docstring"""
    def __init__(self, x, y):
        super(Calc, self).__init__()
        self.x = x
        self.y = y

    def add(self):
        print(self.x + self.y)# with google fire args are not only
                              # strings and can be manipulated

    def substract(self):
        print(self.x - self.y)

if __name__=='__main__':
    fire.Fire(Calc)