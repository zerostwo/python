class prototype(object):
    """
    Class to hold prototype vectors
    """

    def __init__(self,class_id,p_vector,eplsilon):
        self.class_id = class_id
        self.p_vector = p_vector
        self.epsilon = epsilon
        
    def update(self,u_vector,increment=True):
        if increment:
            # Move the prototype vector closer to input vector
            self.p_vector = self.p_vector + self.epsilon*(u_vector - self.p_vector)
        else:
            # Move the prototype vector away from input vector
            self.p_vector = self.p_vector - self.epsilon*(u_vector - self.p_vector)
