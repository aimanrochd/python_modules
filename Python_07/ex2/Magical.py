from abc import ABC, abstractmethod
from typing import Dict, List


class Magical(ABC):
    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        ...
    cast_spell = abstractmethod(cast_spell)

    def channel_mana(self, amount: int) -> Dict:
        ...
    channel_mana = abstractmethod(channel_mana)

    def get_magic_stats(self) -> Dict:
        ...
    get_magic_stats = abstractmethod(get_magic_stats)
