from utils import read_data, read_thetas
from bonus_utils import plot_show, r_squared

mileages, prices = read_data('data.csv')
theta0, theta1 = read_thetas('thetas.txt')

accuracy = r_squared(mileages, prices, theta0, theta1)
print(f"R² (precision): {accuracy:.4f}")

plot_show()