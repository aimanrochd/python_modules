from typing import Dict
from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.card_type = 'Artifact'

    def play(self, game_state: Dict) -> Dict:
        mana = game_state.get('mana', 0)
        return {'card_played': self.name, 'mana_used': self.cost,
                'effect': f'Permanent: {self.effect}',
                'mana_remaining': mana - self.cost}

    def activate_ability(self) -> Dict:
        if self.durability <= 0:
            return {'artifact': self.name,
                    'error': 'Artifact has been destroyed'}
        self.durability -= 1
        return {'artifact': self.name, 'effect': self.effect,
                'durability_remaining': self.durability}
