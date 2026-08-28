from utils  import read_data, estimate_price

def train(mileages, prices, learning_rate=0.1, iterations=1000):

    theta0 = 0
    theta1 = 0
    m = len(mileages)
    max_mileages = mileages.max()
    min_mileages = mileages.min()
    if(max_mileages == min_mileages):
        print("Error: all mileages are identical, cannot train.")
        exit()

    normalized_mileages = (mileages - min_mileages) / (max_mileages - min_mileages)

    for i in range(iterations) :
        prediction = theta0 + theta1 * normalized_mileages
        errors = prediction - prices

        tmp_theta0 =  learning_rate * (1 / m) * sum(errors)
        tmp_theta1 = learning_rate * (1 / m) * sum(errors * normalized_mileages)

        theta0 = theta0 - tmp_theta0
        theta1 = theta1 - tmp_theta1

    new_theta1 = theta1 / (max_mileages - min_mileages)
    new_theta0 = theta0 - new_theta1 * min_mileages

    with open('thetas.txt', 'w') as f:
        f.write(f"{new_theta0},{new_theta1}")

    return new_theta0, new_theta1


mileages, prices = read_data('data.csv')
print('number of inputs : ', len(mileages))
theta0, theta1  = train(mileages, prices)
print('theta0:', theta0)
print('theta1:', theta1)