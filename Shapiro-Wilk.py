import pandas as pd
from scipy.stats import shapiro

# Set the file path for the CSV file
file_path = 'path/to/your/file.csv'

# Load the CSV file into a DataFrame
data = pd.read_csv(file_path)

# Select the column from the DataFrame
data = data['Column_name']

# Perform the Shapiro-Wilk normality test
shapiro_test = shapiro(data)

# Print the results of the Shapiro-Wilk test
print("Shapiro-Wilk Test Statistic:", shapiro_test.statistic)
print("p-value:", shapiro_test.pvalue)





