def analyze_data(data):
    """Calculate multiple statistics for a list of numbers.
    
    Args:
        data (list): List of numbers.
    
    Returns:
        tuple: Mean, minimum, and maximum of the list.
    """
    mean = sum(data) / len(data)
    minimum = min(data)
    maximum = max(data)
    return mean, minimum, maximum

# Usage
numbers = [1, 5, 3, 8, 2]
avg, min_val, max_val = analyze_data(numbers)
print(f"Mean: {avg}, Min: {min_val}, Max: {max_val}")  # Output: Mean: 3.8, Min: 1, Max: 8