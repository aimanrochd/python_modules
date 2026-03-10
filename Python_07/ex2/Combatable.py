from abc import ABC, abstractmethod
from typing import Dict


class Combatable(ABC):
    def attack(self, target: object) -> Dict:
        ...
    attack = abstractmethod(attack)

    def defend(self, incoming_damage: int) -> Dict:
        ...
    defend = abstractmethod(defend)

    def get_combat_stats(self) -> Dict:
        ...
    get_combat_stats = abstractmethod(get_combat_stats)
