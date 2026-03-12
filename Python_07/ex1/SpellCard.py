from typing import Dict, List
from ex0.Card import Card, Rarity


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.used = False

    def play(self, game_state: dict) -> dict:
        if self.used:
            return {'card_played': self.name,
                    'error': 'Spell already used'}
        if isinstance(game_state, dict):
            self.used = True
            effects = {
                'damage': f'Deal {self.cost} damage to target',
                'heal': f'Heal {self.cost} health',
                'buff': f'Buff target by {self.cost}',
                'debuff': f'Debuff target by {self.cost}'
            }
            return {'card_played': self.name, 'mana_used': self.cost,
                    'effect': effects.get(self.effect_type,
                                        'Spell effect applied')}

    def resolve_effect(self, targets: List) -> Dict:
        return {'spell': self.name, 'effect_type': self.effect_type,
                'targets': targets, 'resolved': True}
