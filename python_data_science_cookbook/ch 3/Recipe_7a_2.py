# 3.	Now create an imputer object with strategy as mean, 
# i.e. fill the missing values with the mean value of the missing column.
imputer = Imputer(missing_values=0,strategy="mean")
x_imputed = imputer.fit_transform(x_t)


mask = np.zeros_like(x_t)
mask[2,:] = 1
x_t_m = ma.masked_array(x_t,mask)


print np.mean(x_t_m,axis=0)
print x_imputed[2,:]