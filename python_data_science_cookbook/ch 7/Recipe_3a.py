# Load libraries
from sklearn.datasets import load_boston
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import Lasso, LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

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


   

def build_models(x,y):
    """
    Build a Ridge regression model
    """
    # Alpha values uniformly
    # spaced between 0.01 and 0.02
    alpha_range = np.linspace(0,0.5,200)
    model = Lasso(normalize=True)
    coeffiecients = []
    # Fit a model for each alpha value
    for alpha in alpha_range:
        model.set_params(alpha=alpha)
        model.fit(x,y)
        # Track the coeffiecients for plot
        coeffiecients.append(model.coef_)
    # Plot coeffients weight decay vs alpha value
    # Plot model RMSE vs alpha value
    coeff_path(alpha_range,coeffiecients)
    # View coeffiecient value
    #view_model(model)

def view_model(model):
    """
    Look at model coeffiecients
    """
    print "\n Model coeffiecients"
    print "======================\n"
    for i,coef in enumerate(model.coef_):
        print "\tCoefficient %d  %0.3f"%(i+1,coef)
            
    print "\n\tIntercept %0.3f"%(model.intercept_)

def model_worth(true_y,predicted_y):
    """
    Evaluate the model
    """
    print "\t Mean squared error = %0.2f\n"%(mean_squared_error(true_y,predicted_y))


def coeff_path(alpha_range,coeffiecients):
    """
    Plot residuals
    """
    plt.close('all')
    plt.cla()

    plt.figure(1)
    plt.xlabel("Alpha Values")
    plt.ylabel("Coeffiecient Weight")
    plt.title("Coeffiecient weights for different alpha values")
    plt.plot(alpha_range,coeffiecients)
    plt.axis('tight')
   
    plt.show()

def get_coeff(x,y,alpha):
    model = Lasso(normalize=True,alpha=alpha)
    model.fit(x,y)
    coefs = model.coef_
    indices = [i for i,coef in enumerate(coefs) if abs(coef) > 0.0]
    return indices
    


if __name__ == "__main__":
    
    x,y = get_data()
    # Build multiple models for different alpha values
    # and plot them    
    build_models(x,y)
    print "\nPredicting using all the variables"
    full_model = LinearRegression(normalize=True)
    full_model.fit(x,y)
    predicted_y = full_model.predict(x)
    model_worth(y,predicted_y)    
           
    print "\nModels at different alpha values\n"
    alpa_values = [0.22,0.08,0.01]
    for alpha in alpa_values:
        
        indices = get_coeff(x,y,alpha)   
        print "\t alpah =%0.2f Number of variables selected = %d "%(alpha,len(indices))
        print "\t attributes include ", indices
        x_new = x[:,indices]
        model = LinearRegression(normalize=True)
        model.fit(x_new,y)
        predicted_y = model.predict(x_new)
        model_worth(y,predicted_y)


