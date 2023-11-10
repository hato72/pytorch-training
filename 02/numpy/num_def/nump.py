import numpy as np

def class_mean(data):
    return np.mean(data,axis=1)

def sec_max(data):
    return np.max(data[2,1],axis=0)

def dif_point(data):
    _max = np.max(data,_max)
    _min = np.min(data,_min)
    return _max - _min

def eighty_point(data):
    return np.sum(data[:,0]>= 80)

def sum_point(data):
    return np.sum(data[:,0]+data[:,1]>=135)

def r_count(data):
    one= np.sum(data[:,0])
    two = np.sum(data[:,1])
    return one / two
