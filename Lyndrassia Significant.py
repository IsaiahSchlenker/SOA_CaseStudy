import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Paste your new data here
data = [
    6.7,15.8,32.7,27.1,59.4,17.2,5.9,9,36,32.3,9.2,6,20.3,46.4,5.4,19,36,28.4,20.9,28.8,6.8,41.6,31.2,31.7,4.1,5.1,38.5,4,8.7,29.6,7.1,43,4.7,11.4,9.2,2.5,47.1,29,27,27.7,22.6,7.4,37.5,4.3,41.9,14.6,14.9,30.3,35.9,14,3.5,2.8,13.3,20.6,23.4,12.6,7,30.3,2.7,16.8,23.3,11.3,22.1,24.1,35,4.9,5.7,5.9,24.1,6.3,31.3,29.3,37.1,8.1,6.9,38.1,9.2,31.1,43.7,16.7,9.6,6.2,12.6,11.5,7.7,36.9,20.8,4.6,2.3,5.2,18.7,9.3,24,35.7,12.9,7.6,36.9,38.6,29.9,8.9,20.9,10.3,48.9,36.4,29.6,12.9,35.7,36.8,4.7,45.3,47.6,7.5,40.1,22,8.2,17,66.1,9.5,9.1,3.7,21.9,13.6,11,31.8,29.5,8.9,28.8,5.1,39.2,19.6,5.1,26.3,18.4,6.3,6.6,25.5,11.6,3.7,5.5,9.1,23.8,29.7,13.7,8.7,10.6,7.3,30.3,20,7.7,9.1,3,33.3,57.9,21,30.5,40.9,8.5,2,30.9,10,8.1,3.4,44.9,3.5,3.6,9.1,8.9,18,3.4,5.7,5.9
]

# Calculate mean and variance from data
mean_data = np.mean(data)
var_data = np.var(data)

# For Gamma distribution, we can use the fact that:
# shape = (mean^2) / variance
# scale = variance / mean
shape = (mean_data**2) / var_data
scale = var_data / mean_data

# Generate a range of values for plotting the PDF
x = np.linspace(min(data), max(data), 1000)
pdf_fitted = stats.gamma.pdf(x, a=shape, scale=scale)

# Plot the histogram and fitted distribution
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Data Histogram')
plt.plot(x, pdf_fitted, 'r-', label=f'Fitted Gamma\nShape: {shape:.2f}, Scale: {scale:.2f}')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Lyndrassia Significant')
plt.legend()
plt.show()

# Print the shape and scale parameters
print(f'Fitted Gamma Parameters: Shape={shape:.2f}, Scale={scale:.2f}')
