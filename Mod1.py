'''

check specialvariable__name__.py
'''


print("Coming from Mod1 ",__name__)


def data():
     print("Ruchir")


if(__name__ == '__main__'):            ##This will make sure that data fction will not be called while importing this module
    data()