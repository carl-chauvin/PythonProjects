import pandas as pd
import numpy as np


#list = [0,1,2,3,4,5,6,7,8]

def calculate(list):
    matrix = np.array(list).reshape(3,3)
    try:
        if len(list) == 9:
            mean_m = [(matrix.mean(axis=0).tolist()), (matrix.mean(axis=1).tolist()),(matrix.flatten().mean())]

            var_m = [(matrix.var(axis=0).tolist()), (matrix.var(axis=1).tolist()),(matrix.flatten().var())]

            std_m = [(matrix.std(axis=0).tolist()), (matrix.std(axis=1).tolist()),(matrix.flatten().std())]

            max_m = [(matrix.max(axis=0).tolist()), (matrix.max(axis=1).tolist()),(matrix.flatten().max())]

            min_m = [(matrix.min(axis=0).tolist()), (matrix.min(axis=1).tolist()),(matrix.flatten().min())]

            sum_m = [(matrix.sum(axis=0).tolist()), (matrix.sum(axis=1).tolist()),(matrix.flatten().sum())]
        else:
            print('Error...')
    except ValueError:
        print('la matris solo debe contener 9 dogitos')

    calculations = {
        'mean': mean_m,
        'var': var_m,
        'standard deviation': std_m,
        'max': max_m,
        'min': min_m,
        'sum':sum_m
    }


    return calculations

""" def calculate(list):
    try:
        solution = np.array(list).reshape(3,3)
        calculations = {}

        #para calcular la media
        axis1 = np.mean(solution, axis=0)
        axis2 = np.mean(solution, axis=1)
        flattened = np.mean([axis1, axis2])
        calculations['mean'] = [axis1.tolist(), axis2.tolist(), flattened.tolist()]

        #para calcular la varianza
        axis1 = np.var(solution, axis=0)
        axis2 = np.var(solution, axis=1)
        flattened = np.var([axis1, axis2])
        calculations['variance'] = [axis1.tolist(), axis2.tolist(), flattened.tolist()]

        #para calcular la desviacion estandar
        axis1 = np.std(solution, axis=0)
        axis2 = np.std(solution, axis=1)
        flattened = np.std([axis1, axis2])
        calculations['standard deviation'] = [axis1.tolist(), axis2.tolist(), flattened.tolist()]

        #para calcular el maximo
        axis1 = np.max(solution, axis=0)
        axis2 = np.max(solution, axis=1)
        flattened = np.max([axis1, axis2])
        calculations['max'] = [axis1.tolist(), axis2.tolist(), flattened.tolist()]

        #para calcular el minimo
        axis1 = np.min(solution, axis=0)
        axis2 = np.min(solution, axis=1)
        flattened = np.min([axis1, axis2])
        calculations['min'] = [axis1.tolist(), axis2.tolist(), flattened.tolist()]

        #para calcular la suma
        axis1 = np.sum(solution, axis=0)
        axis2 = np.sum(solution, axis=1)
        flattened = np.sum([axis1, axis2])
        calculations['sum'] = [axis1.tolist(), axis2.tolist(), flattened.tolist()]
    except ValueError:
        print('la matris solo debe contener 9 dogitos')


    return calculations """