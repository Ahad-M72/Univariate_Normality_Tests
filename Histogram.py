import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the file path for the CSV file
file_path = 'path/to/your/file.csv'

# Load the CSV file into a DataFrame
data = pd.read_csv(file_path)

# Select the column from the DataFrame
data = data['data_column']

# Create the histogram
plt.figure(figsize=(8, 6))
sns.histplot(data, bins=30, color='blue')
plt.title('Histogram for data_column')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)

# Show the plot
plt.show()
