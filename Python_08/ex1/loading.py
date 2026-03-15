# Third party imports
# wrapped in try/except to handle missing dependencies gracefully
try:
    import pandas
except ImportError:
    pandas = None

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
    """Check if all required dependencies are installed."""
    # Track if all packages are available
    all_good = True

    print('Checking dependencies:')
    # Check each package and print its version if available
    if pandas is None:
        print('[MISSING] pandas - Run: pip install -r requirements.txt')
        print('   Or with Poetry: poetry install')
        all_good = False
    else:
        print(f'[OK] pandas ({pandas.__version__}) - Data manipulation ready')

    if requests is None:
        print('[MISSING] requests - Run: pip install -r requirements.txt')
        print('   Or with Poetry: poetry install')
        all_good = False
    else:
        print(f'[OK] requests ({requests.__version__}) - Network access ready')

    if matplotlib is None:
        print('[MISSING] matplotlib - Run: pip install -r requirements.txt')
        print('   Or with Poetry: poetry install')
        all_good = False
    else:
        print(f'[OK] matplotlib ({matplotlib.__version__}) '
              '- Visualization ready')

    return all_good


def analyze_data() -> None:
    # Create sample Matrix data for analysis
    print('\nAnalyzing Matrix data...')
    print('Processing 1000 data points...')
    print('Generating visualization...')

    # Sample data points to analyze
    data = [3, 7, 2, 9, 1, 8, 4, 6, 5, 10]
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


def main() -> None:
    print('\nLOADING STATUS: Loading programs...\n')

    # Check dependencies first - only analyze if all packages are available
    all_good = check_dependencies()
    if all_good:
        analyze_data()


if __name__ == "__main__":
    main()
