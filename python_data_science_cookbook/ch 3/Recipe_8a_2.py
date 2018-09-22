# 2.	Randomly sample 10 records from the loaded dataset
no_records = 10
x_sample_indx = np.random.choice(range(x.shape[0]),no_records)
print x[x_sample_indx,:]