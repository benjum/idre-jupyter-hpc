import numpy as np
import pandas as pd

def my_compute(x):
    return x + 1

def use_for_loop_loc(dataset):
    """ Use panda loc() function to retrieve and assign values"""
    dataset['b'] = np.nan
    for i in range(len(dataset)):
        dataset.loc[i, 'b'] = my_compute(dataset.loc[i, 'a'])
        
def use_for_loop_at(dataset):
    """ Use panda at() function to retrieve and assign value"""
    dataset['b'] = np.nan
    for i in range(len(dataset)):
        dataset.at[i, 'b'] = my_compute(dataset.at[i, 'a'])

def use_for_loop_iat(dataset):
    """ Use panda iat() function to retrieve and assign value"""
    dataset['b'] = np.nan
    for i in range(len(dataset)):
        dataset.iat[i, 1] = my_compute(dataset.iat[i, 0])

def use_panda_iterrows(dataset):
    """ Use panda iterrows() to iterate """
    b = np.empty(len(dataset))
    for index, row in dataset.iterrows():
        b = my_compute(row['a'])
    dataset['b'] = b

def use_column(dataset):
    dataset['b'] = dataset.a + 1

def use_panda_apply(dataset):
    """ Use panda built-in apply function"""
    dataset['b'] = dataset.apply(my_compute)

def use_zip(dataset):
    """ Use enumerate function to iterate"""
    b = np.empty(len(dataset))
    for i, (x) in enumerate(zip(dataset.a)):
        b[i] = my_compute(x[0])
    dataset['b'] = b

def use_numpy_for_loop(dataset):
    """ Get column values as a numpy array compute and then assign values back to panda data frame"""
    b = np.empty(len(dataset))
    original = dataset.a
    for i in range(len(dataset)):
        b[i] = my_compute(original[i])
    dataset['b'] = b
