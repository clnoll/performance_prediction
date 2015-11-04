import matplotlib.pyplot as plt
import numpy as np
import sys


def read_data(path):
    return np.genfromtxt(path, delimiter=",", names=True, unpack=True)


def get_x_values(data):
    return data['Date']


def get_y_values(data):
    return data['Close']


def get_training_data(data):
    num_rows = data.shape[0]
    rows_training = int(num_rows * .7)
    return data[:rows_training:]


def predict(f, data):
    x_new = np.linspace(0, len(get_x_values(data)), len(get_x_values(data)))
    y_new = f(x_new)
    return y_new
