import csv

def mean(values):
    """
    Calculate the mean of a list of values.
    
    :param values: List of numerical values
    :return: Mean of the values
    """
    return sum(values) / len(values)

def sample_standard_deviation(values):
    """
    Calculate the sample standard deviation of a list of values.
    
    :param values: List of numerical values
    :return: Sample standard deviation of the values
    """
    mean_value = mean(values)
    variance = sum((x - mean_value) ** 2 for x in values) / (len(values) - 1)
    return variance ** 0.5

def coefficient_of_variation(values):
    """
    Calculate the coefficient of variation (CV) for a list of values.
    
    :param values: List of numerical values
    :return: CV of the values as a percentage
    """
    mean_value = mean(values)
    sample_standard_deviation_value = sample_standard_deviation(values)
    cv = (sample_standard_deviation_value / mean_value) * 100
    return cv

def read_csv(file_path):
    """
    Read a CSV file and return data as a dictionary of columns.
    
    :param file_path: Path to the CSV file
    :return: Dictionary containing column data and list of numeric columns
    """
    data = {}
    numeric_columns = []
    
    with open(file_path, newline='') as csvfile:
        datareader = csv.reader(csvfile)
        headers = next(datareader)
        
        for header in headers:
            data[header] = []
        
        for row in datareader:
            for header, value in zip(headers, row):
                try:
                    data[header].append(float(value))
                    if header not in numeric_columns:
                        numeric_columns.append(header)
                except ValueError:
                    data[header].append(value)
                    
    return data, numeric_columns

def calculate_cv_for_numeric_columns(file_path):
    """
    Calculate the coefficient of variation for each numeric column in a CSV file.
    
    :param file_path: Path to the CSV file
    :return: Dictionary with column names as keys and their CV as values
    """
    data, numeric_columns = read_csv(file_path)
    cv_results = {column: coefficient_of_variation(data[column]) for column in numeric_columns}
    return cv_results

if __name__ == "__main__":
    # Example usage
    file_path = 'path/to/your/file/name.csv'
    cv_results = calculate_cv_for_numeric_columns(file_path)
    print(cv_results)
