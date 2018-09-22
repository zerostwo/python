#3.Calculate percentile values (25th, 50th,75th) for the data to understand data distribution
perc_25 = np.percentile(y,25)
perc_50 = np.percentile(y,50)
perc_75 = np.percentile(y,75)
print
print "25th Percentile    = %0.2f"%(perc_25)
print "50th Percentile    = %0.2f"%(perc_50)
print "75th Percentile    = %0.2f"%(perc_75)
print
#4.Plot these percentile values as reference in the plot we generated in the previous step.
# Draw horizontal lines at 25,50 and 75th percentile
plt.axhline(perc_25,label='25th perc',c='r')
plt.axhline(perc_50,label='50th perc',c='g')
plt.axhline(perc_75,label='75th perc',c='m')
plt.legend(loc='best')
