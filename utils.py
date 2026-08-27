import numpy as np

def read_data(file_path):
    data = np.genfromtxt(file_path, delimiter=',', skip_header=1)
    mileages = data[:, 0]
    prices = data[:, 1]
    return mileages, prices

def estimate_price(mileage, theta0 , theta1):
    return theta0 + theta1 * mileage