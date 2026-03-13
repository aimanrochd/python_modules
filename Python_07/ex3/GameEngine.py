from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import List


class GameEngine:
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self, hand: List = None) -> dict:
        if hand is None:
            hand = [
                self.factory.create_creature(),
                self.factory.create_creature('goblin'),
                self.factory.create_spell()
            ]

        self.cards_created = len(hand)
        result = self.strategy.execute_turn(hand, [])

        self.turns_simulated += 1
        self.total_damage += result['damage_dealt']

        result['hand_used'] = hand
        return result

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
