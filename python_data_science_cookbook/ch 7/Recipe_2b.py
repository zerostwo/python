from sklearn.datasets import load_boston
from sklearn.linear_model import Ridge,LinearRegression
import numpy as np

import matplotlib.pyplot as plt

def get_data():
    """
    Return boston dataset
    as x - predictor and
    y - response variable
    """
    data = load_boston()
    x    = data['data']
    y    = data['target']
    return x,y    



def build_model(x,y):
    """
    Build a Ridge and Linear regression model
    """
    model_linear = LinearRegression(normalize=True)
    model_linear.fit(x,y)    
    
    model_ridge = Ridge(normalize=True,alpha=100)
    model_ridge.fit(x,y)
    # Track the scores- Mean squared residual for plot
    return model_linear,model_ridge    

def view_model(model):
    """
    Look at model coeffiecients
    """
    print "\n Model coeffiecients"
    print "======================\n"
    for i,coef in enumerate(model.coef_):
        print "\tCoefficient %d  %0.3f"%(i+1,coef)
            
    print "\n\tIntercept %0.3f"%(model.intercept_)


def coeff_path(x,y):
    """
    Plot how the coeffiecients weights are penalized
    for increasing values of alpha
    """
    alpha_range = np.linspace(10,100.2,300)
    coeffs = []
    for alpha in alpha_range:
        model = Ridge(normalize=True,alpha=alpha)
        model.fit(x,y)
        coeffs.append(model.coef_)
    
    plt.close('all')
    plt.figure(1)
    plt.xlabel("alpha value")
    plt.ylabel("Coeff weights")
    plt.title("Coeff Weight path")
    plt.plot(alpha_range,coeffs)
    plt.show()
    
    

x,y = get_data()
lin_model,ridg_model = build_model(x,y)

# Add some noise to the dataset
noise = np.random.normal(0,1,(x.shape))
x = x + noise

lin_model_n,ridg_model_n = build_model(x,y)

print "\nLinear Regression Model Before Noise"
view_model(lin_model)

print "\nLinear Regression Model after Noise"
view_model(lin_model_n)

print "\nRidge Model  Before Noise"
view_model(ridg_model)


print "\nRidge Model after Noise"
view_model(ridg_model_n)

coeff_path(x,y)
