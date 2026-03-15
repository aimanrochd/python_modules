import sys
import os
import site


def main() -> None:
    try:
        # If both are equal, we are in the global Python environment
        # (no venv active)
        if sys.base_prefix == sys.prefix:
            print("\nMATRIX STATUS: You're still plugged in\n")

            # sys.executable gives the path to the current Python interpreter
            print(f'Current Python: {sys.executable}')

            print('Virtual Environment: None detected\n')

            print("WARNING: You're in the global environment!")
            print('The machines can see everything you install.\n')

            # Instructions to create and activate a virtual environment
            print('To enter the construct, run:')
            print('python -m venv matrix_env')
            print('source matrix_env/bin/activate # On Unix')
            print('matrix_env\nScripts\nactivate    # On Windows')
            print('\nThen run this program again.')
        else:
            print('\nMATRIX STATUS: Welcome to the construct\n')

            print(f'Current Python: {sys.executable}')

            # VIRTUAL_ENV env variable is set automatically
            # when a venv is activated
            path = sys.prefix

            # os.path.basename extracts just the folder name from the full path
            print(f'Virtual Environment: {os.path.basename(path)}')
            print(f'Environment Path: {path}')

            print("\nSUCCESS: You're in an isolated environment!")
            print('Safe to install packages without affecting\nthe global system.')

            # site.getsitepackages()[0]
            # gives the main packages directory of the venv
            print('\nPackage installation path:')
            print(f'{site.getsitepackages()[0]}')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()
