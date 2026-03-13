from typing import Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
import random


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, health: int,
                 defense_power: int, mana: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.defense_power = defense_power
        self.mana = mana

    def play(self, game_state: Dict) -> Dict:
        mana = game_state.get('mana', 0)
        return {'card_played': self.name, 'mana_used': self.cost,
                'effect': 'Elite card deployed to battlefield',
                'mana_remaining': mana - self.cost}

    def attack(self, target: Card) -> Dict:
        return {'attacker': self.name, 'target': str(target),
                'damage': self.attack_power, 'combat_type': 'melee'}

    def defend(self, incoming_damage: int) -> Dict:
        damage_taken = max(0, incoming_damage - self.defense_power)
        damage_blocked = self.defense_power
        still_alive = self.health > damage_taken
        return {'defender': self.name, 'damage_taken': damage_taken,
                'damage_blocked': damage_blocked, 'still_alive': still_alive}

    def get_combat_stats(self) -> Dict:
        return {'name': self.name, 'attack_power': self.attack_power,
                'health': self.health, 'defense_power': self.defense_power}

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        mana_used = len(targets) + 2
        damage = random.randint(1, self.attack_power)
        return {'caster': self.name, 'spell': spell_name,
                'targets': targets, 'mana_used': mana_used,
                'damage': damage}

    def channel_mana(self, amount: int) -> Dict:
        self.mana += amount
        return {'channeled': amount, 'total_mana': self.mana}

    def get_magic_stats(self) -> Dict:
        return {'name': self.name, 'mana': self.mana}
