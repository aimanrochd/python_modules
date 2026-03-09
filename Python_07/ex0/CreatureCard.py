from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        return {'card_played': self.name, 'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'}

    def get_card_info(self) -> dict:
        return {'name': self.name, 'cost': self.cost,
                'rarity': self.rarity, 'type': 'Creature',
                'attack': self.attack, 'health': self.health}

    def attack_target(self, target: object) -> dict:
        return {'attacker': self.name, 'target': str(target),
                'damage_dealt': self.attack, 'combat_resolved': True}
