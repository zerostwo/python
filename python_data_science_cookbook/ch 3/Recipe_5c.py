# 4.	Data dispersion, variance and standard deviation
print "col_names,variance,std-dev"
for i,col_name in enumerate(col_names):
    print "%s,%0.2f,%0.2f"%(col_name,np.var(x[:,i]),np.std(x[:,i]))
print
    
# 5.	Mean absolute deviation calculation  
def mad(x,axis=None):
    mean = np.mean(x,axis=axis)
    return np.sum(np.abs(x-mean))/(1.0 * len(x))
        
print "col_names,mad"
for i,col_name in enumerate(col_names):
    print "%s,%0.2f"%(col_name,mad(x[:,i]))
print

# 6.	Median absolute deviation calculation
def mdad(x,axis=None):
    median = np.median(x,axis=axis)
    return np.median(np.abs(x-median))
       
print "col_names,median,median abs dev,inter quartile range"
for i,col_name in enumerate(col_names):
    iqr = np.percentile(x[:,i],75) - np.percentile(x[i,:],25)
    print "%s,%0.2f,%0.2f,%0.2f"%(col_name,np.median(x[:,i]), mdad(x[:,i]),iqr)
print
    