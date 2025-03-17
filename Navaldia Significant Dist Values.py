import numpy as np

data = [
        11.2,3.9,8,3.7,None,2.9,8.7,None,6,None,None,None,9.1,None,None,None,6,None,6.1,None,None,None,None,None,7.3,6.2,None,None,4.9,8.8,None,None,None,3.7,5,5.5,3,4.2,None,None,None,None,36.5,8.4,9.3,39.6,None,None,48,6.4,None,None,4.3,None,4.4,None,64.2,5.9,18.6,3,8.6,None,None,None,None,6.1,8.3,None,6.1,4.1,9.2,9.1,None,8.8,8.5,69.9,5.6,5.2,None,7.6,None,None,8.3,3.5,None,None,9.5,7.5,None,None,4,None,3.9,None,None,None,None,None,None,9.3,None,42.6,5.3,7.8,None,None,5.3,3.5,None,25.7,8.9,None,None,8.9,None,65.8,8.1,8.5,None,None,None,8,3.1,5.7,None,3.3,None,5.4,4.4,None,36.4,None,None,None,4.6,None,58.9,None,8.4,None,6.6,None,None,8.6,5.1,None,None,None,None,None,None,None,None,None,None,8.6,6.2,44.6,None,None,65.6,None,None,None,15,None,4.2,31.1,6.4,None,None,None,7.6,7.7,8.2,57.2,8.8,None,2.9,5.5,5.6,None,8.5,None,8.2,64.1,None,None,30.3,3,6.1,35.5,None,6.2,None,None,4,None,None,None,3.5,51.5,42.8,6.4,4.8,None,9.4,None,None,45,7.5,None,4.8,None,None,13.7,None,None,None,8.5,None,None,30,None,None,4.3,27.7,88.3,None,3.7,None,4.3,None,10.7,None,None,23,40.8,4.6,5.4,4.1,4.3,None,None,6.8,None,7.1,8.8,None,None,8.3,None,None,7.6,6.7,None,3.8,None,None,8.2,33.7,None,7.2,None,None,3.4,None,7.8,26,2.9,None,None,4.5,30.5,44.9,42.1,4.4,None,29.9,40.1,None,None,None,None,None,8,36,None,27.7,4.1,None,6.1,None,8.2,None,37.3,7.7,59.3,None,None,None,4,None,None,4.1,None,3.3,47.1,None,None,None,None,3.6,3.2,7.6,5.6,9.3,9.5,15.4,None,None,None,14.4,None,None,None,None,7.1,None,7.2,8.7,60.8,29,61.7,9.2,7.9,26.2,28.8,4.2,None,None,6.9,7.3,7.6,None,4.7,32.5,4.8,None,None,None,5.4,7,None,8.2,7.6,None,None,29.6,None,None,4.7,None,6.9,9.4,None,None,4.6,8.8,7.7,6.4,9.2,5.3,4.3,6,5.1,None,None,29.2,35.8,5.1,None,None,None,None,49.5,None,24.8,3.7,5.7,None,6.6,None,21,5.2,7,3.9,None,None,60.3,None,5.6,None,None,7.7,None,5.1,None,None,67,17.6,None,None,None,7.3,7.9,6.1,9.3,6,5.4,3.1,5.9,None,None,None,4.7,None,8.2,68.4,None,None,5.1,None,None,None,None,7.7,7.9,4.1,None,None,40.6,3.1,None,None,None,8.1,5.1,None,40.5,7.1,None,None,None,6.5,3.4,None,None,4.7,None,None,None,3,None,5,3.9,6.6,None,36.6,4,3.3,None,None,45,3.3,7.1,None,9.5,None,6.2,6.1,8.8,None,None,None,18.1,7.8,6.2,40.4,None,None,8.2,8,6.8,7.8,5.9,None,3.9,3.6,38.2,8.2,7.5,None,None,None,8.1,8.8,2.1,None,None,None,4.8,None,None,3.4,None,None,5.5,3.3,None,None,None,None,7.5,3.9,None,6.1,None,5.7,5.3,None,3,4.5,None,48.5,None,None,None,None,6.2,None,None,4.2,None,8.1,64,29.5,4.5,3.5,5.1,None,7.6,None,None,6.4,6.5,None,None,9.1,82.4,5.7,None,18.5,None,None,5.2,5.6,None,None,None,3,4.3,5.9,8,8.2,9.5,None,3.2,None,None,5.1,None,7.4,None,7.9,8.3,8.6,9.1,25.1,None,None,5.3,None,None,None,7,4.6,4.3,None,6.3,5.7,None,None,4.1,None,43.6,None,None,None,None,37.3,None,7.3,None,8.7,4.1,6.6,6.9,None,None,None,None,5.1,None,6,6.3,3.1,7.8,9,9,4.9,6.5,None,7.5,None,7.2,None,32.3,3.3,None,5.5,None,8.3,9.7,None,42.5,None,None,7,4.5,None,None,None,None,None,None,None,4.5,None,6.3,6.6,9.4,35,5.2,None,3.7,13,50.5,None,6.4,37.8,5.1,9.2,5.9,None,None,8.9,18.9,None,None,6.7,4.6,37.5,None,3.6,8.4,5.9,None,5.5,3.9,None,None,None,7.3,None,3.4,None,None,None,4,7.7,None,3.5,7.8,8.5,4.5,None,3,32,None,20.7,None,None,7.6,5.6,None,None,None,5.2,None,None,7.1,None,31.3,None,3.3,None,28.9,5.5,6.2,8.9,None,None,None,None,None,9.1,8.4,8.6,6.2,5,5.8,5.3,None,None,8,None,None,9,None,16.6,3.9,6.3,4,None,None,8.6,5.7,6.5,4.9,5.1,8.3,None,None,None,5.7,None,23.7,None,8.4,7.1,None,None,6.6,9.2,9.3,3.4,None,2.9,None,5.4,None,7,7.6,8.1,None,None,44,None,None,9,6.5,4.7,None,None,None,9.2,None,6.5,None,None,None,None,29,45.2,70.1,5,None,None,None,None,None,9.5,3.2,None,None,4,None,None,None,5.4,None,4.2,None,7.5,None,5.8,None,None,3.7,None,None,None,65.6,6,9.5,None,5.7,None,None,23.2,None,None,69.8,6.2,None,None,None,None,None,None,4.3,40.9,26.8,8.5,None,None,None,None,4.2,46,None,4.2,8.9,None,None,None,None,7.5,94.2,16.3,66.6,None
]

filtered_data = [x for x in data if x is not None]

lambda_ = 1 / np.mean(filtered_data)

num_missing = data.count(None)

exponential_samples = np.random.exponential(scale=1/lambda_, size=num_missing)

exponential_samples = np.round(exponential_samples, 1)

filled_data = []
exp_index = 0
for x in data:
    if x is None:
        filled_data.append(exponential_samples[exp_index])
        exp_index += 1
    else:
        filled_data.append(x)

print("Updated Data Array:", filled_data)
