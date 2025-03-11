import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Paste your new data here
data = [
    18.4,33.9,23.9,29.5,12.4,5.8,69.2,30.7,5.7,21,6.1,15.5,61.7,20.9,34,34.4,55.7,61.4,24.4,35,4.7,33.7,57.3,3.7,8.7,42.6,10.8,25.2,19.3,6.7,25.8,18.6,17.4,19.7,8.7,47.1,36.4,4.7,55.5,12.7,59.9,29.1,32.2,65.5,21.2,46,43.1,9.6,48,7.7,36.3,32.5,16.7,47.3,14.6,6.7,71.3,54.2,29.5,3.1,7.2,51.2,33.5,3.8,55.9,44.7,21.9,32.7,15,19.6,89.5,21.3,62.8,40.1,5,39,38.9,45.4,46.6,4.2,33.4,12.8,40.2,39.2,4.3,6.8,15.7,26.1,42.8,38.8,78.7,28.1,54.9,23.9,79.3,15,31.8,27.6,45.6,34.8,22.4,5.3,4.8,6,22.3,1.4,40.4,38.4,30.2,29.1,20.1,23.8,9.6,27.9,6.8,8.9,51,17.1,23.1,24.8,10.9,21.6,5.2,43.7,29.6,9.4,29.2,64.8,69.9,23.9,30.1,3.2,31.2,6.8,40.8,19.9,7.8,41.5,5.3,49.4,37.4,36.8,41.2,35.5,67.9,55.9,38.7,30,5.4,14.2,58.8,27.5,22.8,6.3,1.6,39.3,67.4,8.5,74.9,52.6,9.3,33.1,4.1,7.5,45.5,40.7,24.5,66.5,53.2,4.3,63.4,64.9,11.6,55,3.1,52.4,62.2,66.5,18.5,24.6,4.7,17.5,43.7,65.3,48,42.4,7.1,19,93.5,9.5,28.4,38,20.3,13.4,18,23.3,11.3,4.3,3.3,26.8,32.2,25.7,76,48.5,34,5.8,8.6,55.8,5.3,41,8.8,8.8,39.3,33.1,86.7,26.8,6,39.5,65.5,3.7,78.5,5.8,48.6,5.4,5.8,24.2,41.9,5.9,27.5,66.3,46.8,25.2,4.3,55.3,6.1,31.7,1,53.1,4.7,23.6,25.9,34.4,23.5,49.3,60.3,47.6,35.6,10.7,64.6,35.5,4.1,5,5.4,30.8,6.9,25.1,6,6,13.2,31.5,38.5,37.8,4.3,93.2,25,9.3,31.4,3.7,1.1,16,16.8,65.1,64.2,34.9,5.6,3.6,1.6,41,8.5,8.5,88.3,52.6,78.2,32.6,8.5,5.5,22.6,5.7,24,4,13.6,8.5,68.7,29.6,46.8,7.2,3.1,13.9,11.2,27.3,31.1,8.6,6.3,28.5,45.3,13.2,2,1.2,3.9,4.3,7.1,6,8.8,94.1,29,52.6,39.7,9.3,46.4,47,36.2,31.2,20.3,6.8,44.9,3.7,4.9,7.1,10.6,62.7,9.5,26.6,23.2,14.2,13.4,46,8,29.5,55.9,5.6,29.6,40.3,68.4,36.8,24,84.7,4.4,7.8,25.7,58.9,3.2,12.3,54.1,47.4,47.5,7.7,28,20.2,41.6,68.1,7.4,3.4,7.3,4,12.7
]

# Fit a lognormal distribution to the data
shape, loc, scale = stats.lognorm.fit(data, floc=0)

# Generate a range of values for plotting the PDF
x = np.linspace(min(data), max(data), 1000)
pdf_fitted = stats.lognorm.pdf(x, shape, loc, scale)

# Plot the histogram and fitted distribution
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Data Histogram')
plt.plot(x, pdf_fitted, 'r-', label=f'Fitted Lognormal\nShape: {shape:.2f}, Scale: {scale:.2f}')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Lognormal Fit to Data')
plt.legend()
plt.show()

# Print the parameters
print(f'Fitted Lognormal Parameters: Shape={shape:.2f}, Scale={scale:.2f}')
