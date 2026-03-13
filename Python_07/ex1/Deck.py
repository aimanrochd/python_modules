from typing import Dict, List, Optional
import random
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

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

    def draw_card(self) -> Optional[Card]:
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict:
        total = len(self.cards)
        raw_avg = sum(c.cost for c in self.cards) / total if total > 0 else 0.0
        avg_cost = float(f"{raw_avg:.1f}")
        type_counts: Dict[str, int] = {}
        for card in self.cards:
            card_type = card.card_type.lower() + 's'
            type_counts[card_type] = type_counts.get(card_type, 0) + 1
        type_counts['total_cards'] = total
        type_counts['avg_cost'] = avg_cost
        return type_counts
