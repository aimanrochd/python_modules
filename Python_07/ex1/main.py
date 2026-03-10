from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print('=== DataDeck Deck Builder ===\n')

    print('Building deck with different card types...')
    deck = Deck()
    deck.add_card(SpellCard('Lightning Bolt', 3, Rarity.COMMON, 'damage'))
    deck.add_card(ArtifactCard('Mana Crystal', 4, Rarity.RARE, 5,
                               '+1 mana per turn'))
    deck.add_card(CreatureCard('Fire Dragon', 5, Rarity.LEGENDARY, 7, 5))

    print(f'Deck stats: {deck.get_deck_stats()}')

    print('\nDrawing and playing cards:')
    for _ in range(3):
        card = deck.draw_card()
        card_type = type(card).__name__.replace('Card', '')
        print(f'\nDrew: {card.name} ({card_type})')
        print(f'Play result: {card.play({})}')

    print('\nPolymorphism in action: Same interface,'
          'different card behaviors!')


if __name__ == '__main__':
    main()
