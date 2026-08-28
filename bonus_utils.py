import matplotlib.pyplot as plt
from utils import read_data, read_thetas, estimate_price


def plot_show():
    mileages, prices = read_data('data.csv')
    theta0, theta1 = read_thetas('thetas.txt')

    line_x = [mileages.min(), mileages.max()]
    line_y = [estimate_price(x, theta0, theta1) for x in line_x]
    plt.plot(line_x, line_y, color='red', label='Regression line')


    plt.scatter(mileages, prices, color='blue', label='Actual data')

    plt.xlabel('Mileage (km)')
    plt.ylabel('Price')
    plt.title('Car price vs mileage')
    plt.legend()
    plt.show()

def r_squared(mileages, prices, theta0, theta1):
    predictions = theta0 + theta1 * mileages
    ss_res = sum((prices - predictions) ** 2)
    ss_tot = sum((prices - prices.mean()) ** 2)
    return 1 - (ss_res /ss_tot)