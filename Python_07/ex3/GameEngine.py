from typing import Dict, Optional
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        hand = [
            self.factory.create_creature(),
            self.factory.create_creature('goblin'),
            self.factory.create_spell()
        ]
        self.cards_created = len(hand)
        result = self.strategy.execute_turn(hand, [])
        self.turns_simulated += 1
        self.total_damage += result['damage_dealt']
        return result

    def get_engine_status(self) -> Dict:
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
