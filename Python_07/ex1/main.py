from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print('=== DataDeck Deck Builder ===\n')

    print('Building deck with different card types...')
    deck = Deck()
    deck.add_card(SpellCard('Lightning Bolt', 3, 'Common', 'damage'))
    deck.add_card(ArtifactCard('Mana Crystal', 4, 'Rare', 5,
                               '+1 mana per turn'))
    deck.add_card(CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5))

    print(f'Deck stats: {deck.get_deck_stats()}')

    print('\nDrawing and playing cards:')
    game_state = {'mana': 10}
    for _ in range(3):
        card = deck.draw_card()
        card_type = type(card).__name__.replace('Card', '')
        print(f'\nDrew: {card.name} ({card_type})')
        print(f'Play result: {card.play(game_state)}')

    print('\nTesting spell one-time use:')
    bolt = SpellCard('Lightning Bolt', 3, 'Common', 'damage')
    print(f'First play: {bolt.play(game_state)}')
    print(f'Second play: {bolt.play(game_state)}')

    print('\nTesting artifact durability:')
    ring = ArtifactCard('Mana Ring', 2, 'Rare', 2, '+1 mana per turn')
    print(f'Activate 1: {ring.activate_ability()}')
    print(f'Activate 2: {ring.activate_ability()}')
    print(f'Activate 3 (destroyed): {ring.activate_ability()}')
    print(f'testing playing after destroy: {ring.play(game_state)}')

    print('\nPolymorphism in action: Same interface, '
          'different card behaviors!')


if __name__ == '__main__':
    main()
