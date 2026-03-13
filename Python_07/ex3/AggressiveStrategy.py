from enum import Enum
from ex3.GameStrategy import GameStrategy
from typing import List, Dict


class TargetType(Enum):
    PLAYER = "Enemy Player"
    CREATURE = "Enemy Creature"


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        sorted_hand = sorted(hand, key=lambda card: card.cost)
        cards_played = []
        mana_used = 0

        MAX_MANA = 5
        for card in sorted_hand:
            if mana_used + card.cost <= MAX_MANA:
                cards_played.append(card.name)
                mana_used += card.cost

        damage_dealt = mana_used + len(cards_played) + 1

        available_targets = battlefield + [TargetType.PLAYER.value]

        targets = self.prioritize_targets(available_targets)

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets,
            'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: List) -> List:
        return available_targets
