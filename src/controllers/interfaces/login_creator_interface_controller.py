from abc import ABC, abstractmethod
from typing import Dict


class LoginCreatorInterfaceController(ABC):
    @abstractmethod
    def create(self, username: str, password: str) -> Dict:
        pass
