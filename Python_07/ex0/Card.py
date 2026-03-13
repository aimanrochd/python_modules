from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = Rarity(rarity)
        self.card_type = 'Card'

    def play(self, game_state: Dict) -> Dict:
        ...
    play = abstractmethod(play)

    def get_card_info(self) -> Dict:
        return {'name': self.name, 'cost': self.cost,
                'rarity': self.rarity.value, 'type': 'Card'}

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
