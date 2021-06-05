import fire
from termcolor import colored, cprint

# colored(TEXT, fg, bg, attrs=['reverse','blink','bold'])


def greet(name='Roman', age='23'):
    print('Hello {} you are {}'.format(name, age))
    cprint('You are at {}'.format(age), 'blue', 'on_white')

def saybye(name):
    print('Good bye {}'.format(name))


if __name__=='__main__':
    fire.Fire({'greet':greet, 'saybye':saybye})