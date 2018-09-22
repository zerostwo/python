# Load Libraries
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load Iris dataset
data = load_iris()
x = data['data']
plt.close('all')