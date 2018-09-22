# Impute based on class label
missing_y = y[2]
x_missing = np.where(y==missing_y)[0]
y = data['target']
# Mean stragegy 
print np.mean(x[x_missing,:],axis=0)
# Median stragegy
print np.median(x[x_missing,:],axis=0)
