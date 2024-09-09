# Univariate_Normality_Testss
Many parametric tests in statistical software require normality as a crucial assumption. Here is the code for the Python environment to conduct normality tests, including measures of skewness and kurtosis, and the coefficient of variation for univariate normality tests.

## Contents
  `Shapiro-Wilk.py` Conducts the Shapiro-Wilk test for normality.
  
  `Skewness and Kurtosis.py` calculates the absolute skewness and kurtosis.
  
  `Histogram.py` Generates histograms for visualizing data distributions.
  
  `QQ-plot.py` Creates Q-Q plots to check the normality of data.
  
# Shapiro-Wilk Statistic (W) Calculator

`Shapiro-Wilk.py` calculates the Shapiro-Wilk statistic (W) for numeric columns in a given CSV file. As mentioned by Ostrowski and Menyhárt [1], The Shapiro-Wilk test for normality can be conducted using the `shapiro()` function from the `scipy.stats` library in Python (Ostrowski and Menyhárt, 2020).

## Usage

1. Place your CSV file in an accessible location.
2. Modify the `file_path` variable in the script to point to your CSV file and write the column name.
3. Run the script.

# Skewness and Kurtosis Calculator

`Skewness and Kurtosis.py` calculates the absolute skewness and kurtosis for all numeric columns in a given CSV file. The calculation of skewness and kurtosis, is created based on the formulas and information in a study conductd by Cain in 2017 [2].


## Usage

1. Place your CSV file in an accessible location.
2. Modify the `file_path` variable in the script to point to your CSV file.
3. Run the script.


# Histogram Generator
`Histogram.py` generates a histogram for the specified data column from a CSV file, helping visualize data distributions. The script is created based on the descriptions in an article conducted by Ostrowski and Menyhárt [1].
## Usage
1. Place your CSV file in an accessible location.
2. Modify the file_path variable in the script to point to your CSV file.
3. Specify the column name you want to visualize in the script.
4. Run the script to view the histogram.


# QQ-plot Generator
`QQ-plot.py` generates a Q-Q plot for a specified column from a CSV file, which helps to check if your data follows a normal distribution. The script is created based on the descriptions in an article conducted by Ostrowski and Menyhárt [1].

## Usage
1. Place your CSV file in an accessible location.
2. Modify the file_path variable in the script to point to your CSV file.
3. Specify the column name to analyze in the script.
4. Run the script to create and display the Q-Q plot.

# References
1. Ostrowski, J.G., Menyhárt, J., 2020, Statistical analysis of machinery variance by python. Acta Polytechnica Hungarica 17, 151–168 (https://acta.uni-obuda.hu/Ostrowski_Menyhart_102.pdf).
2. Cain, M.K., Zhang, Z., Yuan, K.H., 2017. Univariate and multivariate skewness and kurtosis for measuring nonnormality: Prevalence, influence
and estimation. Behavior Research Methods 49, 1716–1735. ([https://rdcu.be/dTqDt](https://doi.org/10.3758/s13428-016-0814-1)).

```bash
python Skewness and Kurtosis.py
python Shapiro-Wilk.py
python Histogram.py
python QQ-plot.py
