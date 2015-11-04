import matplotlib.pyplot as plt
import numpy as np
import sys

from common import (read_data,
                    get_x_values,
                    get_y_values,
                    get_training_data)


def fit_model(data):
    x = np.linspace(0, len(get_x_values(data)), len(get_x_values(data)))
    y = get_y_values(data)
    # calculate polynomial
    z = np.polyfit(x, y, 3)
    f = np.poly1d(z)
    return f


def predict(f, data):
    x_new = np.linspace(0, len(get_x_values(data)), len(get_x_values(data)))
    y_new = f(x_new)
    return y_new


if __name__ == '__main__':
    data = read_data(sys.argv[1])
    training_data = get_training_data(data)
    print("fitting to %d rows" % training_data.shape[0])
    model_subset = fit_model(training_data)
    fitted_subset_y_values = predict(model_subset, data)
    model_all = fit_model(data)
    fitted_all_y_values = predict(model_all, data)
    plt.plot(range(len(get_x_values(data))), get_y_values(data), 'go',
             range(len(get_x_values(training_data))), get_y_values(training_data), 'ro',
             range(len(get_x_values(data))), fitted_all_y_values, 'b',
             range(len(get_x_values(data))), fitted_subset_y_values, 'pink')

    plt.show()
