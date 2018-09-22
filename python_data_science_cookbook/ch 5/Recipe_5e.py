# Median Absolute Deviation
median = np.median(total_data)
b = 1.4826
mad = b * np.median(np.abs(total_data - median))
outliers = []
# Useful while plotting
outlier_index = []
print "Median absolute Deviation = %.2f"%(mad)
lower_limit = median - (3*mad)
upper_limit = median + (3*mad)
print "Lower limit = %0.2f, Upper limit = %0.2f"%(lower_limit,upper_limit)
for i in range(len(total_data)):
    if total_data[i] > upper_limit or total_data[i] < lower_limit:
        print "Outlier %0.2f"%(total_data[i])
        outliers.append(total_data[i])
        outlier_index.append(i)

plt.figure(2)
plt.title("Outliers using mad")
plt.scatter(range(len(total_data)),total_data,c='b')
plt.scatter(outlier_index,outliers,c='r')
plt.show()

