# imports - wrapped in try/except to handle missing dependencies
try:
    import pandas
except ImportError:
    pandas = None

try:
    import numpy
except ImportError:
    numpy = None

try:
    import requests
except ImportError:
    requests = None

try:
    import matplotlib
    import matplotlib.pyplot as plt
except ImportError:
    matplotlib = None
    plt = None


def check_dependencies() -> bool:
    # Track if all packages are available
    all_good = True

    print('Checking dependencies:')
    # Check each package and print its version if available
    if pandas is None:
        print('[MISSING] pandas - Run: pip install -r requirements.txt')
        all_good = False
    else:
        print(f'[OK] pandas ({pandas.__version__}) - Data manipulation ready')

    if requests is None:
        print('[MISSING] requests - Run: pip install -r requirements.txt')
        all_good = False
    else:
        print(f'[OK] requests ({requests.__version__}) - Network access ready')

    if matplotlib is None:
        print('[MISSING] matplotlib - Run: pip install -r requirements.txt')
        all_good = False
    else:
        print(f'[OK] matplotlib ({matplotlib.__version__}) '
              '- Visualization ready')

    return all_good


def analyze_data() -> None:
    print('\nAnalyzing Matrix data...')
    print('Processing 10 data points...')
    print('Generating visualization...')

    # Use numpy to generate random data points
    data = numpy.random.randn(10)
    # Put data into a pandas DataFrame for manipulation
    df = pandas.DataFrame(data, columns=['values'])
    # Plot the data as a line graph
    plt.plot(df['values'])
    # Save the plot to a file instead of displaying it
    plt.savefig('matrix_analysis.png')
    # Free memory after saving
    plt.close()

    print('\nAnalysis complete!')
    print('Results saved to: matrix_analysis.png')


def show_pip_poetry_diff() -> None:
    print('\n--- pip vs Poetry ---')
    print('pip:')
    print('  - Install: pip install -r requirements.txt')
    print('  - Only installs packages')
    print('  - No lock file by default')
    print('Poetry:')
    print('  - Install: poetry install')
    print('  - Manages packages AND virtual environment')
    print('  - Creates poetry.lock for exact versions')


def main() -> None:
    print('\nLOADING STATUS: Loading programs...\n')

    # Check dependencies first - only analyze if all packages are available
    all_good = check_dependencies()
    if all_good:
        analyze_data()
    # this function Shows the differences between
    # pip and Poetry through your program’s output
    show_pip_poetry_diff()


if __name__ == "__main__":
    main()
