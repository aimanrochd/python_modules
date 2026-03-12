from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def main() -> None:
    print('=== DataDeck Card Foundation ===\n')

    print('Testing Abstract Base Class Design:\n')

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print('CreatureCard Info:')
    print(dragon.get_card_info())
    print('\nPlaying Fire Dragon with 6 mana available:')
    print(f'Playable: {dragon.is_playable(6)}')
    print(f'Play result: {dragon.play({})}')

    print('\nFire Dragon attacks Goblin Warrior:')
    print(f'Attack result: {dragon.attack_target("Goblin Warrior")}')

    print('\nTesting insufficient mana (3 available):')
    print(f'Playable: {dragon.is_playable(3)}')

    print('\nAbstract pattern successfully demonstrated!')


if __name__ == "__main__":
    main()
