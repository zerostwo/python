# Print the mean and standard deviation
# to confirm the normality of our input data.
mean = np.mean(normal_data,axis=0)
std = np.std(normal_data,axis=0)
print "Mean =(%0.2f) and Standard Deviation (%0.2f)"%(mean[0],std[0])
