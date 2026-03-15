import os
from dotenv import load_dotenv


def load_config() -> dict:
    load_dotenv()
    matrix_mode = os.environ.get('MATRIX_MODE')
    database_url = os.environ.get('DATABASE_URL')
    api_key = os.environ.get('API_KEY')
    log_level = os.environ.get('LOG_LEVEL')
    zion_endpoint = os.environ.get('ZION_ENDPOINT')
    return {'matrix_mode': matrix_mode, 'database_url': database_url,
            'api_key': api_key, 'log_level': log_level,
            'zion_endpoint': zion_endpoint}


def display_config(config: dict) -> None:
    print('\nORACLE STATUS: Reading the Matrix...\n')

    print('Configuration loaded:')
    print(f"Mode: {config['matrix_mode']}")
    print(f"Database: {config['database_url']}")
    print(f"API Access: {config['api_key']}")
    print(f"Log Level: {config['log_level']}")
    print(f"Zion Network: {config['zion_endpoint']}")


def security_check() -> None:
    print('\nEnvironment security check:')
    if os.path.exists('.env'):
        print('[OK] .env file properly configured')
    else:
        print('[MISSING] .env file not found')
    if os.path.exists('.gitignore'):
        with open('.gitignore', 'r') as f:
            content = f.read()
            if '.env' in content:
                print('[OK] .env is in .gitignore')


def main() -> None:
    config = load_config()
    display_config(config)
    security_check()


if __name__ == "__main__":
    main()
