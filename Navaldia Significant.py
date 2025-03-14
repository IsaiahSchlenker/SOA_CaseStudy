import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Paste your new data here
data = [
    11.2,3.9,8,3.7,2.9,8.7,6,9.1,6,6.1,7.3,6.2,4.9,8.8,3.7,5,5.5,3,4.2,36.5,8.4,9.3,39.6,48,6.4,4.3,4.4,64.2,5.9,18.6,3,8.6,6.1,8.3,6.1,4.1,9.2,9.1,8.8,8.5,69.9,5.6,5.2,7.6,8.3,3.5,9.5,7.5,4,3.9,9.3,42.6,5.3,7.8,5.3,3.5,25.7,8.9,8.9,65.8,8.1,8.5,8,3.1,5.7,3.3,5.4,4.4,36.4,4.6,58.9,8.4,6.6,8.6,5.1,8.6,6.2,44.6,65.6,15,4.2,31.1,6.4,7.6,7.7,8.2,57.2,8.8,2.9,5.5,5.6,8.5,8.2,64.1,30.3,3,6.1,35.5,6.2,4,3.5,51.5,42.8,6.4,4.8,9.4,45,7.5,4.8,13.7,8.5,30,4.3,27.7,88.3,3.7,4.3,10.7,23,40.8,4.6,5.4,4.1,4.3,6.8,7.1,8.8,8.3,7.6,6.7,3.8,8.2,33.7,7.2,3.4,7.8,26,2.9,4.5,30.5,44.9,42.1,4.4,29.9,40.1,8,36,27.7,4.1,6.1,8.2,37.3,7.7,59.3,4,4.1,3.3,47.1,3.6,3.2,7.6,5.6,9.3,9.5,15.4,14.4,7.1,7.2,8.7,60.8,29,61.7,9.2,7.9,26.2,28.8,4.2,6.9,7.3,7.6,4.7,32.5,4.8,5.4,7,8.2,7.6,29.6,4.7,6.9,9.4,4.6,8.8,7.7,6.4,9.2,5.3,4.3,6,5.1,29.2,35.8,5.1,49.5,24.8,3.7,5.7,6.6,21,5.2,7,3.9,60.3,5.6,7.7,5.1,67,17.6,7.3,7.9,6.1,9.3,6,5.4,3.1,5.9,4.7,8.2,68.4,5.1,7.7,7.9,4.1,40.6,3.1,8.1,5.1,40.5,7.1,6.5,3.4,4.7,3,5,3.9,6.6,36.6,4,3.3,45,3.3,7.1,9.5,6.2,6.1,8.8,18.1,7.8,6.2,40.4,8.2,8,6.8,7.8,5.9,3.9,3.6,38.2,8.2,7.5,8.1,8.8,2.1,4.8,3.4,5.5,3.3,7.5,3.9,6.1,5.7,5.3,3,4.5,48.5,6.2,4.2,8.1,64,29.5,4.5,3.5,5.1,7.6,6.4,6.5,9.1,82.4,5.7,18.5,5.2,5.6,3,4.3,5.9,8,8.2,9.5,3.2,5.1,7.4,7.9,8.3,8.6,9.1,25.1,5.3,7,4.6,4.3,6.3,5.7,4.1,43.6,37.3,7.3,8.7,4.1,6.6,6.9,5.1,6,6.3,3.1,7.8,9,9,4.9,6.5,7.5,7.2,32.3,3.3,5.5,8.3,9.7,42.5,7,4.5,4.5,6.3,6.6,9.4,35,5.2,3.7,13,50.5,6.4,37.8,5.1,9.2,5.9,8.9,18.9,6.7,4.6,37.5,3.6,8.4,5.9,5.5,3.9,7.3,3.4,4,7.7,3.5,7.8,8.5,4.5,3,32,20.7,7.6,5.6,5.2,7.1,31.3,3.3,28.9,5.5,6.2,8.9,9.1,8.4,8.6,6.2,5,5.8,5.3,8,9,16.6,3.9,6.3,4,8.6,5.7,6.5,4.9,5.1,8.3,5.7,23.7,8.4,7.1,6.6,9.2,9.3,3.4,2.9,5.4,7,7.6,8.1,44,9,6.5,4.7,9.2,6.5,29,45.2,70.1,5,9.5,3.2,4,5.4,4.2,7.5,5.8,3.7,65.6,6,9.5,5.7,23.2,69.8,6.2,4.3,40.9,26.8,8.5,4.2,46,4.2,8.9,7.5,94.2,16.3,66.6
]

# Given values for average and variance
average = 13.52613391
variance = 263.065874

# For Exponential distribution:
# mean = 1 / lambda
# variance = 1 / lambda^2
# Thus, lambda can be calculated as the inverse of the mean
lambda_ = 1 / average

# Generate a range of values for plotting the PDF
x = np.linspace(0, max(data), 1000)
pdf_fitted = stats.expon.pdf(x, scale=1/lambda_)

# Plot the histogram and fitted distribution
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Data Histogram')
plt.plot(x, pdf_fitted, 'r-', label=f'Fitted Exponential\nlambda: {lambda_:.2f}')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Navaldia Significant')
plt.legend()
plt.show()

# Print the lambda parameter
print(f'Fitted Exponential Parameter: lambda={lambda_:.2f}')
