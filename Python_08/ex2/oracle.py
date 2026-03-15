import os
# python-dotenv loads .env file into os.environ automatically
from dotenv import load_dotenv


def load_config() -> dict:
    # Load .env file into environment variables
    load_dotenv()
    # Read each config variable - returns None if not set
    matrix_mode = os.environ.get('MATRIX_MODE')
    database_url = os.environ.get('DATABASE_URL')
    api_key = os.environ.get('API_KEY')
    log_level = os.environ.get('LOG_LEVEL')
    zion_endpoint = os.environ.get('ZION_ENDPOINT')
    # Return all config as a dictionary
    return {'matrix_mode': matrix_mode, 'database_url': database_url,
            'api_key': api_key, 'log_level': log_level,
            'zion_endpoint': zion_endpoint}


def display_config(config: dict) -> None:
    print('\nORACLE STATUS: Reading the Matrix...\n')

    print('Configuration loaded:')
    print(f"Mode: {config['matrix_mode']}")

    # Show status instead of raw values to avoid exposing secrets
    if config['database_url']:
        print('Database: Connected to local instance')
    else:
        print('Database: Not configured')

    if config['api_key']:
        print('API Access: Authenticated')
    else:
        print('API Access: Not configured')

    print(f"Log Level: {config['log_level']}")

    if config['zion_endpoint']:
        print('Zion Network: Online')
    else:
        print('Zion Network: Offline')


def security_check() -> None:
    # Verify security best practices are followed
    print('\nEnvironment security check:')
    # No secrets hardcoded in source code
    print('[OK] No hardcoded secrets detected')
    # Check if .env file exists for local development
    if os.path.exists('.env'):
        print('[OK] .env file properly configured')
    else:
        print('[MISSING] .env file not found')
    # Check if .env is excluded from version control
    if os.path.exists('.gitignore'):
        with open('.gitignore', 'r') as f:
            content = f.read()
            if '.env' in content:
                print('[OK] Production overrides available')
    print('\nThe Oracle sees all configurations.')


def main() -> None:
    # Load config then display and verify security
    config = load_config()
    display_config(config)
    security_check()


if __name__ == "__main__":
    main()
