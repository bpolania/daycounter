from datetime import datetime, date

def calculate_year_stats():
    # Get current date
    current_date = date.today()
    current_year = current_date.year
    
    # Create date objects for start and end of year
    year_start = date(current_year, 1, 1)
    year_end = date(current_year, 12, 31)
    
    # Calculate total days in year (accounts for leap years)
    total_days = (year_end - year_start).days + 1
    
    # Calculate days passed and remaining
    days_passed = (current_date - year_start).days + 1
    days_remaining = total_days - days_passed
    
    # Calculate percentage passed
    percentage_passed = (days_passed / total_days) * 100
    
    return {
        'current_date': current_date,
        'total_days': total_days,
        'days_passed': days_passed,
        'days_remaining': days_remaining,
        'percentage_passed': round(percentage_passed, 2)
    }

# Run and display the results
if __name__ == "__main__":
    stats = calculate_year_stats()
    print(f"Current date: {stats['current_date'].strftime('%B %d, %Y')}")
    print(f"Total days in year: {stats['total_days']}")
    print(f"Days passed: {stats['days_passed']}")
    print(f"Days remaining: {stats['days_remaining']}")
    print(f"Percentage of year passed: {stats['percentage_passed']}%")