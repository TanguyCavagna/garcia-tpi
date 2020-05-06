# Necessaire pour définir une classe abstraite
from abc import ABC, abstractmethod

class Migration(ABC):

    @abstractmethod
    def setup(self):
        pass

    def seed():
        return None