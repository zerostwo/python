# Look at the contribution of
# each eigen value towards the variance in data
print "Component, Eigen Value, % of Variance, Cummulative %"
cum_per = 0
per_var = 0
for i,e_val in enumerate(eig_val):
    per_var = round((e_val / len(eig_val)),3)
    cum_per+=per_var
    print ('%d, %0.2f, %0.2f, %0.2f')%(i+1, e_val, per_var*100,cum_per*100)