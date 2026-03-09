from ex0.Card import Card
import random


class Deck:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        from ex0.CreatureCard import CreatureCard
        from ex1.SpellCard import SpellCard
        from ex1.ArtifactCard import ArtifactCard
        total = len(self.cards)
        creatures = sum(1 for c in self.cards if isinstance(c, CreatureCard))
        spells = sum(1 for c in self.cards if isinstance(c, SpellCard))
        artifacts = sum(1 for c in self.cards if isinstance(c, ArtifactCard))
        avg_cost = sum(c.cost for c in self.cards) / total if total > 0 else 0
        return {'total_cards': total, 'creatures': creatures,
                'spells': spells, 'artifacts': artifacts, 'avg_cost': avg_cost}
