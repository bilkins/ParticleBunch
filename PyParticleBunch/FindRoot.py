import numpy as np

def find_x(f, y, lower_bound, upper_bound, resolution=100):
    x = np.linspace(lower_bound, upper_bound, resolution)
    delta = abs(f(x) - y)
    x0 = x[delta == delta.min()]
    return x0.mean(), delta.min()

def find_x_converge(f, y, lower_bound, upper_bound, delta_limit = 1e-6, resolution=100, max_iterations=100):
    
    if max_iterations <= 0:
        print('Invalid value for maximum number of iterations.')
        raise ValueError
        
    x0, delta = find_x(f, y, lower_bound, upper_bound, resolution)
    n_iter = 0
    
    while delta > delta_limit:
        if n_iter==max_iterations:
            print('Exceeded maximum number of iterations.')
            break
        else:
            span = upper_bound - lower_bound
            if x0 == lower_bound or x0 == upper_bound:
                lower_bound = x0 - span / 2
                upper_bound = x0 + span / 2
            else:
                lower_bound = x0 - span / resolution
                upper_bound = x0 + span / resolution
            x0, delta = find_x(f, y, lower_bound, upper_bound, resolution)
        n_iter += 1
    return x0, delta
        