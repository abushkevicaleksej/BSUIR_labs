from abc import ABC, abstractmethod
import pickle


class FileRepository(ABC):

    @staticmethod
    @abstractmethod
    def save_state(entity):
        pass

    @staticmethod
    @abstractmethod
    def load_state():
        pass