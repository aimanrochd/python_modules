from ex2.EliteCard import EliteCard


def main() -> None:
    print('=== DataDeck Ability System ===\n')

    warrior = EliteCard('Arcane Warrior', 6, 'Legendary', 5, 10, 3, 4)

    print('EliteCard capabilities:')
    caps = warrior.get_capabilities()
    for interface, methods in caps.items():
        print(f"- {interface}: {methods}")

    print('\nPlaying Arcane Warrior (Elite Card):')
    game_state = {'mana': 10}
    print(f'Play result: {warrior.play(game_state)}')

    print('\nCombat phase:')
    print(f'Attack result: {warrior.attack("Enemy")}')
    print(f'Defense result: {warrior.defend(5)}')

    print('\nMagic phase:')
    print(f'Spell cast: '
          f'{warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])}')
    print(f'Mana channel: {warrior.channel_mana(3)}')

    print('\nMultiple interface implementation successful!')


if __name__ == '__main__':
    main()
