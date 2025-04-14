from abc import ABC, abstractmethod
from typing import Dict


class BalanceEditorInterfaceController(ABC):
    @abstractmethod
    def edit(self, user_id: int, new_balance: float) -> Dict:
        pass
