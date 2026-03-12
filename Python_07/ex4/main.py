from ex0.Card import Rarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print('=== DataDeck Tournament Platform ===\n')

    platform = TournamentPlatform()

    dragon = TournamentCard('Fire Dragon', 5, "Legendary", 7, 5,
                            'dragon_001')
    wizard = TournamentCard('Ice Wizard', 4, "Rare", 5, 6,
                            'wizard_001', 1150)

    print('Registering Tournament Cards...')
    platform.register_card(dragon)
    platform.register_card(wizard)

    print(f'\n{dragon.name} (ID: {dragon.card_id}):')
    print('- Interfaces: [Card, Combatable, Rankable]')
    print(f'- Rating: {dragon.rating}')
    print(f'- Record: {dragon.wins}-{dragon.losses}')

    print(f'\n{wizard.name} (ID: {wizard.card_id}):')
    print('- Interfaces: [Card, Combatable, Rankable]')
    print(f'- Rating: {wizard.rating}')
    print(f'- Record: {wizard.wins}-{wizard.losses}')

    print('\nCreating tournament match...')
    result = platform.create_match('dragon_001', 'wizard_001')
    print(f'Match result: {result}')

    print('\nTournament Leaderboard:')
    for entry in platform.get_leaderboard():
        print(entry)

    print('\nPlatform Report:')
    print(platform.generate_tournament_report())

    print('\n=== Tournament Platform Successfully Deployed! ===')
    print('All abstract patterns working together harmoniously!')


if __name__ == '__main__':
    main()
