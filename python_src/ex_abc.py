'''abc - abstract base class
'''
import abc

class Base(abc.ABC):
    @classmethod
    @abc.abstractclassmethod
    def factory(cls):
        return cls()

    @staticmethod
    @abc.abstractclassmethod
    def say_name():
        return 'I am base'

class Implement(Base):
    @classmethod
    def factory(cls, *args):
        obj = cls(*args)
        return obj

    @staticmethod
    def say_name():
        return 'I am Implement'


i = Implement()
print(i.say_name())  # hi from Implement



