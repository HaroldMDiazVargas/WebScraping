

from abc import ABC, abstractmethod

class Requisites(ABC):
    def __init__(self, keyword, characters):
        self.keyword = keyword
        self.maxCharacters = characters
    
    @abstractmethod
    def checkRequisites(self, soup, browser):
        print(f"Checking {self.keyword} existence")
