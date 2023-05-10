import torch
from matplotlib import pyplot as plt

def plot_curve(data):
    fig = plt.figure()
    plt.plot(range(len(data)), data, color='blue')
    plt.legend(['value'], loc='upper right')
    plt.xlabel('step')
    plt.ylabel('value')
    plt.show()


def abs(number):
    if not isinstance(number, (float, int)):
        return number
    if number < 0:
        number = number * -1
    return number

