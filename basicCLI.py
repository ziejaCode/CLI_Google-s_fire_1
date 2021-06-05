import fire 

def greet(name):
    print('hello {}'.format(name))

age = 34

def sayBye(name):
    print('bye {}'.format(name))

class Employer(object):
    """docstring for Employer """
    def __init__(self, arg):
        super(Employer, self).__init__()
        print('Employ ', arg)
        self.arg = arg
    
    def __repr__(self):
        print('this is employer {}'.format(self.arg))


if __name__=='__main__':
    # fire.Fire() # this expose everything to user
    # fire.Fire(greet) # in this way we expose only whatever 
                     # is passed as argument 
    # fire.Fire(Employer) # Esposes object
    fire.Fire({'greet':greet, 'sayBye':sayBye}) # this is the 
                                                # way to expose multiple methods
