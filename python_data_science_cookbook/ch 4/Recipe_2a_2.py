# Create  KernelPCA object in Scikit learn, specifying a type of kernel as a parameter.
kpca = KernelPCA(kernel="rbf",gamma=10)
# Perform KernelPCA
kpca.fit(x)
x_kpca = kpca.transform(x)


# Plot the first two components.
plt.figure(4)
plt.title("Kernel PCA")
plt.scatter(x_kpca[:,0],x_kpca[:,1],c=y)
plt.xlabel("$Component_1$")
plt.ylabel("$Component_2$")

plt.show()
