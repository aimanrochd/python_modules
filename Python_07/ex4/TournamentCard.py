from typing import Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, health: int, card_id: str,
                 rating: int = 1200) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.card_id = card_id
        self.wins = 0
        self.losses = 0
        self.rating = rating

    def play(self, game_state: Dict) -> Dict:
        mana = game_state.get('mana', 0)
        return {'card_played': self.name, 'mana_used': self.cost,
                'effect': 'Tournament card deployed',
                'mana_remaining': mana - self.cost}

    def attack(self, target: object) -> Dict:
        return {'attacker': self.name, 'target': str(target),
                'damage': self.attack_power, 'combat_type': 'melee'}

    def defend(self, incoming_damage: int) -> Dict:
        damage_taken = incoming_damage
        still_alive = self.health > damage_taken
        return {'defender': self.name, 'damage_taken': damage_taken,
                'still_alive': still_alive}

    def get_combat_stats(self) -> Dict:
        return {'name': self.name, 'attack_power': self.attack_power,
                'health': self.health}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16

    def get_rank_info(self) -> Dict:
        return {'rating': self.rating, 'wins': self.wins,
                'losses': self.losses}

    def get_tournament_stats(self) -> Dict:
        return {'name': self.name, 'card_id': self.card_id,
                'rating': self.rating, 'wins': self.wins,
                'losses': self.losses, 'attack_power': self.attack_power,
                'health': self.health}
