import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Paste your new data here
data = [
    3.5,3.2,38.9,3.4,3.4,46,14.3,7.4,9.4,40.7,7.2,10.3,1.5,17.6,6.3,6.1,83.1,37,4.1,5.9,7.2,9.3,8.1,65.2,5.2,1.7,3.9,42.2,5.5,32.1,21.5,4,7.4,40.3,9.2,38.6,28.4,45,3.2,3.5,9.3,3.1,78.6,25.1,3.4,3.1,8.2,40.2,3.3,3.4,11,6.3,22.5,9.3,6.1,3.3,3.5,11.9,4,5.3,5,5.8,5.3,9.5,4.2,82.5,3.6,7,3,8.9,38.8,5.5,23.5,4.2,5.5,8.7,7.2,4,4.8,15.4,5.1,27,7,8.1,8.5,3.9,3.4,5,7.8,7,25.2,3.6,8.2,8.4,5.1,6.5,6.3,2.9,7.5,27.9,8.6,7.9,39.7,37.6,5.7,44.2,4.9,57.3,6.6,30.6,7.4,3.9,5.6,3.3,31.7,20.3,7.6,6,34.3,3.4,57.3,5.3,11,6.1,7.1,9.5,5.9,4.4,7.5,3.9,5.4,12.9,7.8,4.8,3.5,7.7,7.5,4.7,7.2,1.2,9,38.4,8.5,5.8,23,3.3,41.5,2.8,3.7,6,5.4,43.9,6.7,9.2,5.4,35.1,35.1,39.4,29.3,8.8,5,3.7,3.5,8.1,4.6,3.2,5.9,6.9,4.6,30.1,2.9,7.8,6,3.9,28.5,7.4,2.9,6.6,7.9,4.7,3.9,66.4,41.4,3.3,67.2,1.8,83.5,27.6,17.5,8.1,33.2,5.2,4.8,7.2,6.4,31.2,8.5,7.8,5.6,8.4,9.5,26.7,8.3,7.3,7.9,6.9,46.9,5.7,39.9,5.2,6.4,8.6,4.6,4.2,25.9,16.9,3.1,6.2,11.6,15.6,50.1,3.7,8,3.5,7.6,59.7,3.9,4.3,3.3,8.8,3.7,4.7,8.5,9.3,7.2,6.5,7.5,5.9,5.2,5.9,6.6,9,33.9,62.2,59.7,9.4,5.1,17.1,7.1,7.6,9.2,7.4,5.7,6.7,8.2,4,8.6,62.9,15.8,35.9,78.7,7.1,26.4,42,6,9,3.9,5.4,2.9,72.1,4.7,88.8,6.1,63.3,8.7,3.6,3.9,31.9,4.6,7.1,3.9,7.2,6.8,6.6,4,9.4,4.1,9,3.8,54.7,3.3,5.7,7.4,5.2,8.7,3.7,3.9,33,6.6,6.5,5.7,7.7,4.8,7.7,5.9,5.7,3.8,3.8,4.3,7.4,29.8,5.4,5.5,19.2,4.7,8.5,6.2,9.4,25.6,8,9.2,9.3,4.5,13.4,3.3,16.8,32.9,27.2,5.6,3.5,7.9,13.7,4.8,6.3,7.6,44.5,6.9,7.6,6,4.1,6.2,3.4,7.5,4.1,3.3,38.2,5.2,4.7,3.5,4.1,8.9,8,8.9,49.3,6.9,3.1,33.8,1.3,26.2,6.9,6.6,16,4.8,19.3,9.5,8.9,5,34.6,4.7,7.4,7.6,30.5,15.8,6.9,5.4,6.7,4.5,8.3,9.1,2.9,82.2,9.4,6.3,9.2,60.5,7.8,6.7,8.9,6.5,8.1,3.7,7.5,5.6,3.7,6.1,5.3,8.2,7.8,7.2,47.4,19.7,6.3,5.6,4.2,4.3,8.7,8.5,3.8,7.6,6,8,3,5,6.8,4.8,4.1,8.5,7.9,7.6,24.1,9.3,3.8,3,9.5,6.5,4.1,14.3,8.6,4.9,8.6,5,9.5,4,6.5,7.1,2.9,5.3,32.3,3.6,3.7,8.4,3.1,7.9,3.6,8.5,7.2,9.5,7.8,8.3,4.5,12.4,6.7,9,4.7,9.1,7.9,19.8,9.5,4.4,4.2,5.3,3.4,4.3,6.1,5.6,3.5,9.4,6.6,7.1,3.3,4.2,3.6,6.3,9.2,4.3,26.3,3.2,4.4,8.5,5.9,23.1,6.5,53.4,8.1,3.4,3.2,4.4,8,29.3,3.7,71.2,5.7,4.5,8.5,26.2,8.2,7,7.8,8,11.8,8.8,6.4,4.8,8.7,1.2,5.1,9.1,4.3,6.7,6.3,39.1,6.5,5.7,3.1,6.3,6.4,6.8,7.2,12.7,3.6,4.8,4.7,9.1,29,9.5,6.2,3.3,3.6,8.5,6,4.3,4.3,3.1,47.1,43.6,3.2,3.1,7.8,34.1,5.1,86.6,3.3,3,4.3,10.3,3.9,8.8,8.8,4.3,3.6,48.7,6.1,7.6,3.8,3.9,5.4,28.8,7.1,4.9,9.3,8.4,7,5.8,3,5.9,6.1,80.4,6.2,6.1,6.4,9.1,16,2.9,33.4,9.2,4,7.5,3,8.2,8.8,5.1,7.1,33.6,5.7,3.8,7.8,3.2,6.2,6.9,9.2,4.1,7.5,5,3.5,5.8,7.9,5.4,7,44.7,4.7,4.4,5.8,38,5.8,4.1,4.3,8.3,9.1,3,8,6.9,5,2,4.9,7.2,3.4,5.5,4.3,6.9,4.6,28.8,11.3,3.9,6.2,5.7,3.3,3.7,9.2,4.8,5.9,47.3,19.9,38.4,40.4,3.3,3.6,7.3,5.6,44.4,8.5,4.6,3.9,4,71.2,5.9,7.1,7.1,7.1,7.2,3.7,4.8,4.5,7,34.7,8.1,13.6,8.6,6.4,7.5,2.9,8.3,7,3.4,46.9,3.4,6,6.6,5.2,11.4,2.9,9.3,41.1,6.7,6.1,34.7,3.6,52.4,4.8,8.9,7.1,4.9,3.3,6.6,9,7.9,18.3,8.4,3.1,9.5,4.4,8.7,7.5,3.8,8.1,3.2,8.5,7.4,40.8,7.3,7.3,3.4,7.3,7.6,49.8,3.3,45.3,12.6,45.1,4.5,9.2,7.1,6.5,9.1,8.1,43.1,8.3,5,5,20.8,6,45.6,55.8,2.9,5,7.3,6.5,4.3,8.6,4.8,7.3,4.5,9.4,6.9,8.4,22.8,38.6,8.3,6.6,25.9,8.1,4.7,16.5,4.7,5.6,5.9,7.5,3.1,7.9,36.4,5.9,7.1,13,18.5,4.1,1.8,3,4.8,39.8,2.9,3,49.5,7.6,3.9,5.4,7.8,33.7,31.6,4.8,28.5,7,3,5.5,37.2,5.5,3.9,7,6.6,8.2,9.3,6.5,5.9,5.9,39.8,21,8.4,5.2,6.3,3.8,29.9,9,23.9,3.2,37,6.4,6.1,7.3,5.5,7.2,41.8,6.6,6.7,4.9,8.8,37.2,8.3,19.6,3,4.2,8.2,2.9,8,3.3,9.5,6.3,8.5,5.2,4,6.6,6.7,6.6,5.7,5.1,4.3,7.2,4,7.7,4.9,6.5,6.1,8.2,3.5,3.9,8.9,45.9,33.3,2.9,2.9,4.6,8.2,4.8,7.5,4.6,9,25.5,9.2,5.4,7.6,7.8,4.1,9,4.3,5.7,9.4,22.2,5.2,7.2,3.2,6.5,7.9,3.1,3.4,3.1,3.1,9.4,4.1,5.2,4.3,3.6,39.2,4.7,5.2,44.9,8.3,8.1,4.8,95.1,4.8,4.5,6.9,6.4,4.2,8.4,9.2,8.4,9.1,8.4,8.4,6.3,8.1,3.1,6.3,25.7,17.5,24,7.6,3.9,9.3,3.9,5.8,6,43.3,7.9,4.8,6.1,8.3,35.1,5.5,5.2,8.3,6,8.1,6.7,9.5,20.5,8.9,8.1,8.6,2.9,3,9.9,9.3,3.5,5.9,3.1,5.7,4.4,9.3,9.4,19.1,6.2,3.6,4.2,5.7,6.2,4.4,7.8,2.9,7,8.9,6.9,32.9,8.3,8.6,5,6.3,5,8.7,9,44.2,8.5,68.7,42.8,6.4,5.7,3.6,31.7,3.5,7.7,5,3.9,31.8,5.5,3.9,5.6,80.1,10,3.6,5.7,7.8,8.4,5.4,31.4,9.3,4.6,7.5,3.3,8,7,8.7,4.2,9.1,8,6.4,6.7,8.3,5.2,5.3,7.3,3.4,16.4,60.8,4.6,4.8,8.4,8.5,9.3,3.2,6.4,7.8,3.1,3.3,5.5,4.8,7.3,6.9,7.1,6.3,7.8,9.3,3.5,8.4,4.7,3.7,8,71.3,6.9,5.2,3.3,66.7,3.3,24.8,7.8,7.8,7.3,5,4.5,8.5,89.1,14.3,66.6,46.5,7.4,8.9,4.7,6.9,8.2,3.3,8.6,8.2,7.7,40.5,4.8,6.9,4.3,8.2,1.9,8.8,44.7,4.3,31.7,7,6.9,8.7,4.1,12,3.7,6.4,16.8,5.1,9,5.8,3.7,5.9,7.5,8.7,6,3.4,8,3.3,8.8,3.8,6.2,7.3,8,5.3,8,5.5,4.8,5.1,58.5,7.7,3.3,4.7,6.3,6.7,22.7,37.1,8.9,6.9,37.2,4.3,8.6,52,6.3,3.3,45.2,5,3.7,4.1,8.8,12.5,3.6,9.4,8.7,4.9,6,3.5,7.2,8.5,26,4.5,3.4,6.7,6.6,8.7,5.5,7.8,15.6,7.4,3.4,7.1,3.6,6.3,8,7.2,8.4,44.5,8.4,7.3,7.2,4.6,36.2,21.9,1.9,4.7,7.1,5.2,3.7,5.5,45.2,5.3,5.2,6.6,7.1,9.5,5.5,3.7,5.1,48.1,9.4,8.3,4.3,3.4,41.8,4.1,3.3,3.1,8.2,22.3,7.5,7.4,9.2,3.8,6.8,4.5,5.2,4.9,5.7,5.9,8.7,3.1,9.2,5.2,7.9,3.4,7.2,6.7,5.7,9.5,43.6,8.1,6.5,4.7,1.5,8.1,3.2,7.6
]

# Fit an Exponential distribution to the data
mean_data = np.mean(data)
var_data = np.var(data)

# For Exponential distribution, the rate (λ) is the inverse of the mean
rate = 1 / mean_data

# Generate a range of values for plotting the PDF
x = np.linspace(min(data), max(data), 1000)
pdf_fitted = stats.expon.pdf(x, scale=1/rate)

# Plot the histogram and fitted distribution
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Data Histogram')
plt.plot(x, pdf_fitted, 'r-', label=f'Fitted Exponential\nRate: {rate:.2f}')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Lyndrassia High')
plt.legend()
plt.show()

# Print the rate (λ) parameter
print(f'Fitted Exponential Parameter: Rate={rate:.2f}')
