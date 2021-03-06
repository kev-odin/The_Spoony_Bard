# Kevin's Time Tracker: 0.5 hour

import abc

class Potion(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def action(self):
        pass

    @abc.abstractmethod
    def _potion_effect(self):
        pass

    @property
    @abc.abstractmethod
    def name(self):
        pass
