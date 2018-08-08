# -*- coding: utf-8 -*-
"""
Chapter 6 : Machine Learning - 1
Recipe    : Buildign decision trees for multi-class problems.

@author: gsubramanian
"""

import math

def prob(data,element):
    """Calculates the percentage count of a given element

    Given a list and an element, returns the elements percentage count
        
    """
    element_count =0
   	# Test conditoin to check if we have proper input
    if len(data) == 0 or element == None \
                or not isinstance(element,(int,long,float)):
        return None      
    element_count = data.count(element)
    return element_count / (1.0 * len(data))


def entropy(data):
    """"Calcuate entropy
    """
    entropy =0.0
    
    if len(data) == 0:
        return None
    
    if len(data) == 1:
        return 0
    try:
        for element in data:
            p = prob(data,element)
            entropy+=-1*p*math.log(p,2)
    except ValueError as e:
        print e.message
        
    
    return entropy

