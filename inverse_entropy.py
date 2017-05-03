from scipy.optimize import differential_evolution
import math
import numpy as np

def entropy(prob_array):
    entropy=0
    for prob in prob_array:
        if prob>0:
            entropy += - prob*math.log(prob, 2)
    return entropy

def entropy_diff(prob_array,*desired):
    entropy=0
    target,=desired
    prob_array[0]=0.5
    for prob in prob_array:
        if prob>0:
            entropy += - prob*math.log(prob, 2)
    return abs(entropy-target)+abs(1-np.sum(prob_array))


def solver(num_genes,target_entropy):
    bounds=[(0,1)]*num_genes
    desired=(target_entropy,)
    result = differential_evolution(entropy_diff, bounds,args=desired)
    rez=result.x
    rez=rez/np.sum(rez)
    return rez

if __name__ == '__main__':
    num_genes=16
    target_entopy=4.0
    rez=solver(num_genes,target_entopy)
    print(rez)
    print(entropy(rez))