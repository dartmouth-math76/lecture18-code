import numpy as np

def AcceptOrReject(gamma):
    """ Based on the acceptance probability gamma in the Metropolis-Hastings rule, 
        should the proposal be accepted or rejected?
    """
    
    u = np.random.rand()
    if(u<gamma):
        return True
    else:
        return False