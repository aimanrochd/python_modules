from typing import Dict
from ex0.Card import Card, Rarity


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        return {'card_played': self.name, 'mana_used': self.cost,
                'effect': f'Permanent: {self.effect}'}

    def activate_ability(self) -> Dict:
        return {'artifact': self.name, 'effect': self.effect,
                'durability_remaining': self.durability}
