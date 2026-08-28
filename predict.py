from utils import estimate_price, read_thetas, get_mileage


def predict(mileage):
    theta0, theta1 = read_thetas('thetas.txt')
    predicted_price = estimate_price(mileage, theta0, theta1)
    if predicted_price < 0:
        predicted_price = 0
    print("predicted price :", predicted_price)



predict(get_mileage())