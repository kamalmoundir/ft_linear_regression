import numpy as np
import os

def read_data(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return None, None
    try:
        data = np.genfromtxt(file_path, delimiter=',', skip_header=1)
        if data.size == 0:
            print(f"Error: {file_path} is empty or has no data rows.")
            return None, None
        if data.ndim == 1:
            print(f"Error: {file_path} needs at least 2 data rows.")
            return None, None
        
        mileages = data[:, 0]
        prices = data[:, 1]

        if np.isnan(mileages).any() or np.isnan(prices).any():
            print(f"Error: {file_path} contains invalid (non-numeric) values.")
            return None, None
        
        return mileages, prices
    except Exception:
        print(f"Error: {file_path} contains invalid (non-numeric) values.")
        return None, None

def estimate_price(mileage, theta0 , theta1):
    return theta0 + theta1 * mileage


def read_thetas(file_path):
    if not os.path.exists(file_path):
        return 0, 0
    try:

        data = np.genfromtxt(file_path, delimiter=',')
        theta0 = data[0]
        theta1 = data[1]
        if np.isnan(theta0) or np.isnan(theta1):
            print("Warning: thetas file contains invalid data, using 0, 0")
            return 0, 0
        return theta0, theta1
    except Exception:
        print("Warning: could not read thetas file, using 0, 0")
        return 0, 0

def get_mileage():
    while True:
        user_input = input("Enter a mileage: ")
        user_input = user_input.replace(',', '')
        try:
            mileage = float(user_input)
            if mileage < 0:
                print("Mileage cannot be negative, try again.")
                continue
            return mileage
        except Exception:
            print("Invalid input, please enter a number.")