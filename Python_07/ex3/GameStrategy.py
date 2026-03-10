from abc import ABC, abstractmethod
from typing import Dict, List


class GameStrategy(ABC):
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        ...
    execute_turn = abstractmethod(execute_turn)

    def get_strategy_name(self) -> str:
        ...
    get_strategy_name = abstractmethod(get_strategy_name)

    def prioritize_targets(self, available_targets: List) -> List:
        ...
    prioritize_targets = abstractmethod(prioritize_targets)
