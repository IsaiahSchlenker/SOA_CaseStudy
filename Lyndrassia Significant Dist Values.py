import numpy as np

data = [
    6.7,None,15.8,32.7,27.1,None,59.4,17.2,5.9,9,None,None,None,None,None,36,None,32.3,None,None,None,9.2,None,None,None,None,6,None,None,None,None,None,20.3,46.4,None,5.4,19,None,None,36,28.4,20.9,None,None,28.8,None,None,6.8,None,41.6,None,31.2,None,31.7,4.1,5.1,38.5,None,None,4,8.7,None,None,29.6,None,None,7.1,43,4.7,11.4,9.2,None,None,2.5,None,47.1,29,27,27.7,None,22.6,7.4,None,37.5,4.3,None,None,41.9,None,None,14.6,None,14.9,30.3,35.9,14,3.5,None,None,2.8,None,None,13.3,None,20.6,None,23.4,12.6,None,7,None,None,30.3,None,2.7,None,16.8,None,23.3,11.3,22.1,None,24.1,35,None,4.9,5.7,5.9,None,None,24.1,6.3,None,None,None,31.3,None,29.3,37.1,None,None,None,None,8.1,6.9,None,38.1,9.2,None,31.1,None,None,43.7,16.7,9.6,None,None,None,6.2,12.6,11.5,7.7,36.9,20.8,None,None,4.6,2.3,5.2,None,18.7,None,9.3,24,None,35.7,12.9,None,None,7.6,None,None,36.9,38.6,None,None,None,29.9,None,None,None,8.9,20.9,None,10.3,None,48.9,36.4,None,None,None,None,None,None,None,None,None,29.6,None,None,None,None,12.9,None,35.7,None,None,36.8,4.7,45.3,None,47.6,None,None,None,None,None,7.5,None,None,40.1,None,None,22,None,8.2,17,None,66.1,None,None,None,None,None,None,9.5,9.1,None,3.7,21.9,13.6,None,None,None,11,31.8,None,None,None,None,29.5,None,8.9,28.8,None,None,None,5.1,None,39.2,19.6,None,None,None,None,None,None,None,5.1,26.3,None,None,None,None,18.4,None,None,6.3,None,6.6,25.5,11.6,None,None,3.7,5.5,None,9.1,23.8,29.7,None,13.7,None,8.7,10.6,7.3,None,None,30.3,None,None,None,20,7.7,9.1,None,None,None,3,None,None,None,33.3,None,57.9,21,None,None,None,None,30.5,None,None,None,None,None,None,None,None,40.9,None,None,None,8.5,2,30.9,10,None,None,8.1,3.4,44.9,None,3.5,3.6,None,None,9.1,None,None,None,8.9,None,None,None,None,None,18,3.4,None,None,None,None,None,None,None,None,None,5.7,5.9,None
]

filtered_data = [x for x in data if x is not None]
average = np.mean(filtered_data)
variance = np.var(filtered_data)

shape = (average ** 2) / variance
scale = variance / average

num_missing = data.count(None)
gamma_samples = np.random.gamma(shape, scale, num_missing)
gamma_samples = np.round(gamma_samples, 1)

filled_data = []
gamma_index = 0
for x in data:
    if x is None:
        filled_data.append(gamma_samples[gamma_index])
        gamma_index += 1
    else:
        filled_data.append(x)

print("Updated Data Array:", filled_data)
