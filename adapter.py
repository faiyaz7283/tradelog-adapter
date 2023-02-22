from abc import ABC, abstractmethod
from typing import List, Dict
from validator import OrderScheme


class Adapter(ABC):
    @abstractmethod
    def get_all_filled_orders(self) -> List[OrderScheme]:
        pass

    @abstractmethod
    def get_order_details(self, order_id: str) -> OrderScheme:
        pass
