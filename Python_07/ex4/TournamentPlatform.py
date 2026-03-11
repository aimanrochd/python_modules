from typing import Dict, List
from ex4.TournamentCard import TournamentCard
import random


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.attack_power == card2.attack_power:
            winner, loser = random.choice([(card1, card2), (card2, card1)])
        elif card1.attack_power > card2.attack_power:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1

        return {'winner': winner.card_id, 'loser': loser.card_id,
                'winner_rating': winner.rating,
                'loser_rating': loser.rating}

    def get_leaderboard(self) -> List:
        sorted_cards = sorted(self.cards.values(),
                              key=lambda c: c.rating, reverse=True)
        leaderboard = []
        for i, card in enumerate(sorted_cards, 1):
            leaderboard.append(
                f'{i}. {card.name} - Rating: {card.rating} '
                f'({card.wins}-{card.losses})'
            )
        return leaderboard

    def generate_tournament_report(self) -> Dict:
        ratings = [c.rating for c in self.cards.values()]
        avg_rating = sum(ratings) // len(ratings) if ratings else 0
        return {'total_cards': len(self.cards),
                'matches_played': self.matches_played,
                'avg_rating': avg_rating,
                'platform_status': 'active'}
