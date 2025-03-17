import numpy as np

data = [
        8.7,16.5,67.1,56.6,12,12.8,50.5,7.7,64.7,72,23,None,69.8,12.2,None,51.2,24.5,78.4,12.3,6.8,66.9,13.4,None,16.2,47.7,None,60.6,None,54.4,5.2,72.5,None,16.8,15.2,None,41.2,31,48,8.8,64.1,77.2,23.4,71,None,5.4,72.1,43.9,32.3,31.8,68.9,6.5,7,51.1,8.4,32.7,32.2,49.1,17.5,71,3.1,None,75.5,None,11.8,59.3,4.7,71.8,None,23.2,4,3,12.2,22.6,37.5,40.3,84.5,42.3,None,56.5,66.1,12.5,None,33.1,None,5.9,None,63.6,43,68.8,None,None,None,92.8,None,None,17.1,None,47.7,21.2,4.4,22.1,67.6,12.4,54.5,47.7,None,None,14.8,19.8,None,11,65.2,33.3,84.5,35,41.2,70.5,14.8,72.4,None,92.2,50,44.3,24.9,13.5,19.6,34.5,None,5.3,35.1,9.2,65.7,89,75.4,34.2,91.4,37,None,None,None,79.3,32.2,None,None,None,68.7,None,None,32.6,4,33.1,None,None,46.7,20.8,22.9,3.6,61.1,33.7,76.7,79.2,67.2,11,None,5.3,42.3,72.7,8.8,37.8,55.4,30.5,None,46,79.4,9.3,83.8,92.1,39.1,37.8,24.7,91.2,21.8,None,19.4,35.1,None,None,45.8,None,69,None,61.6,63.5,None,25.5,41.6,59.3,67.2,None,37.1,None,15.5,35.5,83.4,18.9,31.8,49,None,32.7,7.4,80.2,3.6,39,None,62.6,26.9,None,None,None,None,13.7,19.7,41.4,None,19,42.8,38,6.4,1.6,58.6,32.9,None,35.4,39.2,None,9.7,47.4,42.1,44.7,5.7,11.7,76.9,64.3,21.4,48.5,None,35.3,41.8,15.8,None,None,12,36.9,73.5,58,76.5,None,15,34.7,7.1,None,51.8,23.6,45.1,45.1,26.1,37.2,None,8.7,None,55.1,77.8,20.1,16.6,31.3,None,2.1,4.9,None,6.3,59.5,28.2,8.2,None,None,42.3,56.5,None,79.1,42.2,12.2,None,11.7,86.5,4.8,68.5,33.8,22.2,18.9,None,None,62.8,24.6,7.1,30.7,78,49.1,88.7,50.4,4.3,None,45.7,25.5,None,3.7,90.8,None,4.9,33.1,18.1,20.7,16.6,19.8,55.8,32.2,30.1,None,92.4,None,4.2,87.3,47.2,None,77.9,73.6,43,41.2,66.7,36.6,18.5,94.7,60.4,22,13.9,22,86,18.6,9.2,None,None,55.2,61.5,42.1,60.3,44.1,87.4,27.6,12.8,65.2,None,54.9,12.1,27.1,71.9,69.7,29.5,None,67.2,34.1,32.9,44.1,48.6,8,49.4,None,None,23,2.1,30.3,None,None,None,None,4.1,53.4,None,33.9,20.8,None,34.1,None,56.2,None,83,None,5.6,None,23,None,5.9,39.7,23.2,77.1,3,9.6,64.7,94.4,None,38.1,58.2,71.9,None,None,55.1,47,42.6,33.7,52,None,None,63.9,15.5,12.5,38.8,46.7,72.4,None,79.4,None,None,16.3,15.3,62.3,39,None,39.3,None,22.4,None,None,21.7,76.7,60.6,18.3,15.6,None,52.3,4.4,38.8,31.7,67.9,7.6,79,71.2,None,None,7.1,12,5.6,68.1,19.3,68.4,72.5,None,88.9,None,44.7,7.2,73.1,17.7,30.1,33.2,12.3,None,42.4,55.4,None,34.7,3,76.5,58.6,69.5,44.1,11.1,62.7,26.6,18.3,None,None,47.1,34.6,37.8,20.1,55.7,6,None,46.2,26.6,None,85,86.5,11.8,3.5,64.3,10.7,49.2,45.8,81.9,33.1,32.2,63.3,None,89.7,None,40.9,None,92.4,34.8,5.6,10.1,21.2,50.5,22.8,57.4,8,3.2,59.7,13.5,4,None,26.1,21,64,66.3,49.9,10.2,43.8,54.2,68.6,9.2,8.4,39.4,43.8,25.1,88.9,None,35.8,51.7,43.9,31.7,26.6,None,25.8,5.3,90.8,5.5,None,94.4,22.5,61.8,58.8,74.1,45.3,12.3,26.1,23.8,9.7,21.7,58.3,88.1,18.7,42.5,24.1,25.2,78.3,70.2,93.5,None,None,None,94.1,4.2,34.3,6.7,None,41.4,63.5,None,None,13.1,49,25.4,76.1,9.4,11.1,16.1,42.8,80.5,None,None,72.2,None,15.1,39.1,None,None,43.2,40.9,6.9,34.1,20.4,6.4,None,16.1,9.7,None,None,68.2,61.8,8.5,None,77.5,36.8,None,None,None,46.4,None,15.6,86.4,91.6,49.4,39.8,None,23.5,8.4,80.2,None,None,4.7,41.2,32.2,46.3,5.7,None,78.5,35,None,20.9,60.1,None,45.4,43.1,40.6,36,7.9,95.4,52.2,22.6,15.4,None,29.2,8.7,9.8,None,23.8,None,54,35,48.7,61.7,None,None,None,44.7,29.1,41.3,7.5,None,61.7,None,27,None,21.5,None,47,58.9,None,12.6,None,63.8,93.9,None,13.3,48.5,21.1,49,None,None,None,38.6,73.5,82.8,3.9,27.9,70.6,18.2,34.6,31.3,13.7,9,69.5,24.1,None,17,None,None,None,31.5,93.7,None,16.8,81.1,43.5,None,5.3,32.1,83.9,None,17.4,21,None,74.5,70,88.4,84.5,None,71,None,None,19.9,58.3,51.8,None,18.8,30.6,37.7,None,None,None,93.8,3.3,45.2,42.3,66.1,93.2,45.9,None,15.9,4.3,None,88.3,50.6,32.2,31.9,26.6,21.3,89.9,88.2,60.5,23.5,67.6,68.4,6.7,None,67.4,None,None,50.3,None,18.4,42.6,65.6,88.3,55.5,None,None,None,71.5,None,50.9,9.2,4.7,82.6,21.7,31.4,51.7,77.1,28.7,None,None,None,None,77.8,35.6,61.5,25,71.8,11.5,25.3,None,61.1,27.6,46.2,None,26.4,48.1,10.3,39.8,8.5,57.6,16,12,None,77,16.9,14,2.8,None,None,27.1,10.6,52.6,17.1,26.2,46.3,22.9,66.3,None,None,None,None,37.5,29.3,10.7,50.1,51.3,54.6,15.6,None,26.6,26.4,45.2,25.7,42.5,None,None,27.7,6.1,53,None,24.1,67.4,None,72.6,32.1,75.9,None,37.5,7,10.7,9.8,9.7,66.6,27.1,None,None,None,None,44.1,None,None,7.9,18.4,29.8,None,None,None,21,33.9,21.8,62.8,None,15.9,46.2,31.7,66.5,64.9,None,15.3,None,42,35.2,9,62,9.3,None,13.9,None,21.9,None,12,None,None,None,None,None,None,52.2,None,47.8,None,None,None,7.1,47.6,33.5,None,31.1,None,7.9,16.7,30.6,66.2,None,48.2,None,None,40,None,None,15.9,77.5,36.8,None,40.9,86.5,15,None,None,37.8,None,6.4,None,None,None,None,10.5,None,None,55.9,54.3,21,28.3,57.7,56.5,92.7,None,29.3,56.7,27.1,10.5,None,None,None,52.8,31.1,53,None,51.1,5.3,61.6,11.5,None,9.7,2.8,None,68.7,25.3,12.9,65.6,42.9,31,None,9.3,11.8,27.9,None,37.3,30.9,22.6,None,None,None,None,42.4,62.7,None,83.3,None,None,None,50.2,None,19.6,6.5,64.1,20.5,28.1,61.2,10.7,4.4,24,42.7,None,64.7,None,31.8,92.6,9.4,None,36.5,None,None,59.1,7.9,55.9,None,55.7,None,41.8,15.1,57.2,90.3,56.7,61.7,None,34,None,None,62.6,63.8,None,None,34.4,None,None,34.4,None,None,6.2,84.8,10.5,None,31.1,25.7,54,None,None,45.4,21.4,14,None,48.1,5.8,44.7,None,None,13.9,None,40.9,28.3,5.9,31.9,None,23.5,None,None,None,35.5,25.7,36.1,4.1,None,None,72.2,62.5,23,29.4,33.1,48.6,59.6,59.2,12.2,7.5,None,48.8,94.3,81.9,52.5,None,47.4,8,None,None,57,25.5,66.3,52.4,None,5.3,51,18,61.6,None,61.5,None,36,13.7,None,75.9,25.7,30.7,36.1,None,8.6,None,None,None,82.4,45.4,None,14.1,None,72.4,26.7,24,28.6,7.1,None,None,63.8,48.4,19.3,8.9,None,None,54.2,8.9,21.9,33.5,None,46.9,46,63.7,None,85,9.1,46.7,None,None,68.9,32.7,76.7,None,47.2,46.8,None,8.3,None,None,38.7,21.7,50,None,None,22.5,52.7,23.5,33.2,None,15.6,15.3,38.7,None,None,14,30.2,None,89.8,32.9,None,28,None,38.5,None,None,None,None,20.8,16.4,38,20.4,8.7,42.8,49.3,None,None,32.9,28.4,88.3,14.2,71.3,62,16.7,None,65.1,19.4,13.5,None,68.2,13.4,13.9,None,None,8,42.5,None,66.5,50.2,74.3,85.3,None,None,None,13.9,14.5,48,None,18.5,42.4,19.9,26.6,None,33.7,None,52.4,29.5,None,None,None,None,None,None,None,70.1,38.3,63.3,None,21.5,5,21.7,48.3,None,None,37.4,9.2,None,67,7.8,42.2,None,28.3,2.2,11.7,None,56.2,26.8,None,9,10.4,41.4,None,None,42.2,44.8,None,18.8,63.5,30.4,9.6,None,56.2,62.5,71,38.1,7.9,None,26.9,None,None,14.8,26,None,64.2,None,None,11.7,20.2,7.6,None,None,63.7,57.8,None,None,17.1,48.2,47.9,40.4,None,None,11.5,68.7,33.7,35.8,20.1,45.9,71.6,46.2,70.7,None,95.4,31.3,None,None,None,66.7
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
