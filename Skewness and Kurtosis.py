import csv

def read_csv(file_path):
    """
    Read a CSV file and extract data for all numeric columns.
    
    :param file_path: Path to the CSV file
    :return: Dictionary with column names as keys and lists of floats as values
    """
    data = {}
    numeric_columns = []
    
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            headers = reader.fieldnames
            
            for header in headers:
                data[header] = []
            
            for row in reader:
                for header in headers:
                    try:
                        value = float(row[header])
                        data[header].append(value)
                        if header not in numeric_columns:
                            numeric_columns.append(header)
                    except ValueError:
                        continue
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None, None
    
    return data, numeric_columns

def central_moment(values, order):
    """
    Calculate the central moment of a list of values.
    
    :param values: List of numerical values
    :param order: Order of the central moment
    :return: Central moment of the specified order
    """
    mean = sum(values) / len(values)
    return sum((x - mean) ** order for x in values) / len(values)

def sample_standard_deviation(values):
    """
    Calculate the sample standard deviation of a list of values.
    
    :param values: List of numerical values
    :return: Sample standard deviation of the values
    """
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    return variance ** 0.5

def calculate_skewness_kurtosis(data, numeric_columns):
    """
    Calculate skewness and kurtosis for specified columns.
    
    :param data: Dictionary with column names as keys and lists of floats as values
    :param numeric_columns: List of numeric columns to calculate skewness and kurtosis for
    :return: List of dictionaries with skewness and kurtosis results for each column
    """
    results = []

    for column in numeric_columns:
        x = data[column]  # List of floats
        n = len(x)
        
        if n < 3:  # Skewness and kurtosis require at least 3 data points
            continue

        m2 = central_moment(x, 2)
        m3 = central_moment(x, 3)
        m4 = central_moment(x, 4)
        
        s = sample_standard_deviation(x)
        
        G1 = (n * (n - 1)) ** 0.5 / (n - 2) * (m3 / m2**1.5)
        
        G2 = ((n - 1) / ((n - 2) * (n - 3))) * ((n + 1) * ((m4 / ((m2) * (m2))) - 3) + 6)
        
        EG2 = G2 - 3
        
        absolute_skewness = abs(G1) <= 2
        absolute_kurtosis = abs(EG2) <= 4
        
        results.append({
            'Column': column,
            'Absolute Skewness': abs(G1),
            'Absolute Kurtosis (Excess)': abs(EG2),
            'Absolute Skewness (<=2)': absolute_skewness,
            'Absolute Kurtosis (<=4)': absolute_kurtosis
        })

    return results

def main(file_path):
    """
    Main function to read CSV file and calculate skewness and kurtosis for all numeric columns.
    
    :param file_path: Path to the CSV file
    """
    data, numeric_columns = read_csv(file_path)
    
    if data is None or numeric_columns is None:
        print("No valid numeric data found.")
        return

    results = calculate_skewness_kurtosis(data, numeric_columns)

    # Print results
    print("Skewness and Kurtosis")
    for result in results:
        print(result)

if __name__ == "__main__":
    # Example usage
    file_path = 'Path\to\your\file.csv'
    main(file_path)
