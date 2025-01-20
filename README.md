# Year Statistics Calculator

A simple Python script that calculates various statistics about the current year, including days passed, days remaining, and percentage of year completed.

## Features

- Displays current date in a readable format
- Calculates total days in the current year (handles leap years automatically)
- Shows number of days passed in the current year
- Shows remaining days in the year
- Calculates percentage of year completed
- All calculations include the current day

## Requirements

- Python 3.x
- No external packages required (uses only standard library)

## Installation

1. Clone this repository or download the `year_stats.py` file
2. No additional installation steps needed

## Usage

Simply run the script using Python:

```bash
python year_stats.py
```

### Example Output

```
Current date: January 19, 2025
Total days in year: 365
Days passed: 19
Days remaining: 346
Percentage of year passed: 5.21%
```

## Code Structure

The script contains a main function `calculate_year_stats()` that:
- Takes no parameters
- Returns a dictionary containing all calculated statistics
- Uses the `datetime` module for accurate date calculations

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - feel free to use it in your own projects.

## Author

Boris Polania

## Version History

- 1.0.0 (2025-01-19)
    - Initial release
    - Basic year statistics functionality
    - Current date display added