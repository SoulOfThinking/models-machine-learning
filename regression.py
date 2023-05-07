import numpy as np


def com_error_for_line_given_points(b, w, points):  # 计算平均loss值
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (w * x + b)) ** 2
    return totalError / float(len(points))


# 求梯度信息
def step_gradient(b_current, w_current, points, learningRate):
    b_gradient = 0
    w_gradient = 0
    N = float(len(points))
    for i in range(len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2 / N) * (y - ((w_current * x) + b_current))
        w_gradient += -(2 / N) * x * (y - ((w_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_w = w_current - (learningRate * w_gradient)
    return [new_b, new_w]


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, np.array(points), learning_rate)
    return [b, m]


def run():
    points = np.genfromtxt("data.csv", delimiter=",")
    learning_rate = 0.0001
    initial_b = 0
    initial_m = 0
    num_iterations = 1000
    print("Starting gradient descent at b ={0},m={1},error = {2}".format(initial_b, initial_m,
                                                                         com_error_for_line_given_points(initial_b,
                                                                                                         initial_m,
                                                                                                         points)))
    print("Running....")
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print("After {0} iterations b = {1} , m={2} , error={3}".format(num_iterations, b, m,
                                                                    com_error_for_line_given_points(b, m, points)))


if __name__ == "__main__":
    run()
