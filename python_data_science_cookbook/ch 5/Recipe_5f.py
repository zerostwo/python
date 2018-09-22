# Standard deviation
std = np.std(total_data)
mean = np.mean(total_data)
b = 3
outliers = []
outlier_index = []
lower_limt = mean-b*std
upper_limt = mean+b*std
print "Lower limit = %0.2f, Upper limit = %0.2f"%(lower_limit,upper_limit)
for i in range(len(total_data)):
    x = total_data[i]
    if x > upper_limit or x < lower_limt:
        print "Outlier %0.2f"%(total_data[i])
        outliers.append(total_data[i])
        outlier_index.append(i)


plt.figure(3)
plt.title("Outliers using std")
plt.scatter(range(len(total_data)),total_data,c='b')
plt.scatter(outlier_index,outliers,c='r')
plt.savefig("B04041 04 10.png")
plt.show()
