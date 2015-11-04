import matplotlib.pyplot as plt
import numpy as np
import sys

from lmfit import minimize, Parameters, report_fit

from common import (read_data,
                    get_x_values,
                    get_y_values,
                    get_training_data)

DEFAULT_KWARGS = {
    'amp': 10,
    'decay': 0.1,
    'shift': 0.0,
    'omega': 3.0
}


def get_x_range(data):
    return np.array(range(len(get_x_values(data))))


def get_params(kwargs):
    params = Parameters()
    for k, v in kwargs.items():
        params.add(k, value=v)
    return params


def fit_model(data, default_params):
    x = get_x_range(data)
    y = get_y_values(data)
    return minimize(fcn2min, default_params, args=(x, y)).params


def fcn2min(params, x, y):
    return predict(params, x) - y


def predict(params, x):
    amp = params['amp'].value
    shift = params['shift'].value
    omega = params['omega'].value
    decay = params['decay'].value
    y_values = amp * np.sin(x * omega + shift) * np.exp(-x * x * decay)
    return y_values


if __name__ == '__main__':
    data = read_data(sys.argv[1])
    training_data = get_training_data(data)
    print("fitting to %d rows" % training_data.shape[0])
    default_params = get_params(DEFAULT_KWARGS)
    params_subset = fit_model(training_data, default_params)
    fitted_subset_y_values = predict(params_subset, get_x_range(data))
    params_all = fit_model(data, default_params)
    fitted_all_y_values = predict(params_all, get_x_range(data))
    plt.plot(range(len(get_x_values(data))), get_y_values(data), 'go',
             range(len(get_x_values(training_data))), get_y_values(training_data), 'ro',
             range(len(get_x_values(data))), fitted_all_y_values, 'b',
             range(len(get_x_values(data))), fitted_subset_y_values, 'pink'
             )
    plt.show()
