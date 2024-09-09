# Univariate_Normality_Testss
Many parametric tests in statistical software require normality as a crucial assumption. Here is the code for the Python environment to conduct normality tests, including measures of skewness and kurtosis, and the coefficient of variation for univariate normality tests.

## Contents
  Shapiro-Wilk.py: Conducts the Shapiro-Wilk test for normality.
  
  Skewness and Kurtosis.py: calculates the absolute skewness and kurtosis.
  
  Histogram.py: Generates histograms for visualizing data distributions.
  
  QQ-plot.py: Creates Q-Q plots to check the normality of data.
  
# CSV Shapiro-Wilk Statistic (W) Calculator

Shapiro-Wilk.py calculates the Shapiro-Wilk statistic (W) for numeric columns in a given CSV file. 

## Usage

1. Place your CSV file in an accessible location.
2. Modify the `file_path` variable in the script to point to your CSV file and write the column name.
3. Run the script.

# CSV Skewness and Kurtosis Calculator

Skewness and Kurtosis.py calculates the absolute skewness and kurtosis for all numeric columns in a given CSV file.


## Usage

1. Place your CSV file in an accessible location.
2. Modify the `file_path` variable in the script to point to your CSV file.
3. Run the script.


# CSV histogram Generator
Histogram.py generates a histogram for the specified data column from a CSV file, helping visualize data distributions.

## Usage
1. Place your CSV file in an accessible location.
2. Modify the file_path variable in the script to point to your CSV file.
3. Specify the column name you want to visualize in the script.
4. Run the script to view the histogram.


# CSV QQ-plot Generator
QQ-plot.py generates a Q-Q plot for a specified column from a CSV file, which helps to check if your data follows a normal distribution.

## Usage
1. Place your CSV file in an accessible location.
2. Modify the file_path variable in the script to point to your CSV file.
3. Specify the column name to analyze in the script.
4. Run the script to create and display the Q-Q plot.


```bash
python Skewness and Kurtosis.py
Shapiro-Wilk.py
Histogram.py
QQ-plot.py
