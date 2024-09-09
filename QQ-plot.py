import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Set the file path for the CSV file
file_path = 'path/to/your/file.csv'

# Load the CSV file into a DataFrame
data = pd.read_csv(file_path)

# Select the column from the DataFrame
subj_uqol_data = data['column_name']

# Create a QQ plot with a line fitted to the sample quantiles
fig = sm.qqplot(subj_uqol_data, line='s')
plt.title('QQ Plot for indicator_name')
plt.show()
