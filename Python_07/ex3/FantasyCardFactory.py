from typing import Dict, List, Union
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: Union[str, int, None]
                        = None) -> Card:
        return CreatureCard(str(name_or_power), 5, 'Legendary', 7, 5)

    def create_spell(self, name_or_power: Union[str, int, None]
                     = None) -> Card:
        return SpellCard(str(name_or_power), 3, 'Rare', 'damage')

    def create_artifact(self, name_or_power: Union[str, int, None]
                        = None) -> Card:
        return ArtifactCard(str(name_or_power), 2, 'Epic', 3, 'Mana Boost')

    def create_themed_deck(self, size: int) -> Dict:
        cards: List[Card] = []
        for i in range(size):
            if i % 3 == 0:
                cards.append(self.create_creature())
            elif i % 3 == 1:
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())
        random.shuffle(cards)
        return {'cards': cards, 'size': len(cards),
                'theme': 'Fantasy'}

    def get_supported_types(self) -> Dict:
        return {'creatures': ['dragon', 'goblin'],
                'spells': ['fireball'],
                'artifacts': ['mana_ring']}
