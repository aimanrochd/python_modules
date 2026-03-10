from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def play(self, game_state: dict) -> dict:
        ...

    def attack(self, target) -> dict:
        ...

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        ...
