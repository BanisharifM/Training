import numpy as np
import h5py
import matplotlib.pyplot as plt
from testCases_v3 import *
from dnn_utils_v2 import sigmoid, sigmoid_backward, relu, relu_backward
from public_tests import *

plt.rcParams['figure.figsize'] = (5.0, 4.0)  # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'


np.random.seed(1)

# GRADED FUNCTION: initialize_parameters


def initialize_parameters(n_x, n_h, n_y):

    np.random.seed(1)

    W1 = np.random.randn(n_h, n_x)*0.01
    b1 = np.zeros(shape=(n_h, 1))
    W2 = np.random.randn(n_y, n_h)*0.01
    b2 = np.zeros(shape=(n_y, 1))

    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}

    return parameters


parameters = initialize_parameters(3, 2, 1)

print("W1 = " + str(parameters["W1"]))
print("b1 = " + str(parameters["b1"]))
print("W2 = " + str(parameters["W2"]))
print("b2 = " + str(parameters["b2"]))

# GRADED FUNCTION: initialize_parameters_deep


def initialize_parameters_deep(layer_dims):

    np.random.seed(3)
    parameters = {}
    L = len(layer_dims)  # number of layers in the network

    for l in range(1, L):

        parameters['W'+str(l)] = np.random.randn(layer_dims[l],
                                                 layer_dims[l-1])*0.01
        parameters['b'+str(l)] = np.zeros(shape=(layer_dims[l], 1))

        assert(parameters['W' + str(l)].shape ==
               (layer_dims[l], layer_dims[l - 1]))
        assert(parameters['b' + str(l)].shape == (layer_dims[l], 1))

    return parameters


parameters = initialize_parameters_deep([5, 4, 3])

print("W1 = " + str(parameters["W1"]))
print("b1 = " + str(parameters["b1"]))
print("W2 = " + str(parameters["W2"]))
print("b2 = " + str(parameters["b2"]))

# GRADED FUNCTION: linear_forward


def linear_forward(A, W, b):

    Z = np.dot(W, A)+b
    cache = (A, W, b)
    return Z, cache


t_A, t_W, t_b = linear_forward_test_case()
t_Z, t_linear_cache = linear_forward(t_A, t_W, t_b)
print("Z = " + str(t_Z))

# GRADED FUNCTION: linear_activation_forward


def linear_activation_forward(A_prev, W, b, activation):

    if activation == "sigmoid":
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = sigmoid(Z)

    elif activation == "relu":
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = relu(Z)

    cache = (linear_cache, activation_cache)

    return A, cache


A_prev, W, b = linear_activation_forward_test_case()

A, linear_activation_cache = linear_activation_forward(
    A_prev, W, b, activation="sigmoid")
print("With sigmoid: A = " + str(A))

A, linear_activation_cache = linear_activation_forward(
    A_prev, W, b, activation="relu")
print("With ReLU: A = " + str(A))

# GRADED FUNCTION: L_model_forward


def L_model_forward(X, parameters):

    caches = []
    A = X
    # number of layers in the neural network
    L = len(parameters) // 2

    for l in range(1, L):
        A_prev = A
        A, linear_activation_cache = linear_activation_forward(
            A_prev, parameters["W" + str(l)], parameters["b" + str(l)], "relu")
        caches.append(linear_activation_cache)

        AL, linear_activation_cache = linear_activation_forward(
            A, parameters["W" + str(L)], parameters["b" + str(L)], "sigmoid")
        caches.append(linear_activation_cache)

    return AL, caches


t_X, t_parameters = L_model_forward_test_case_2hidden()
# t_AL, t_caches = L_model_forward(t_X, t_parameters)

# print("AL = " + str(t_AL))


# GRADED FUNCTION: compute_cost

def compute_cost(AL, Y):

    m = Y.shape[1]

    cost = (-1 / m) * np.sum(np.multiply(Y, np.log(AL)) +
                             np.multiply(1 - Y, np.log(1 - AL)))

    cost = np.squeeze(cost)

    return cost


Y, AL = compute_cost_test_case()

print("cost = " + str(compute_cost(AL, Y)))


A = np.array([[1, 2], [3, 4]])

print('axis=1 and keepdims=True')
print(np.sum(A, axis=1, keepdims=True))
print('axis=1 and keepdims=False')
print(np.sum(A, axis=1, keepdims=False))
print('axis=0 and keepdims=True')
print(np.sum(A, axis=0, keepdims=True))
print('axis=0 and keepdims=False')
print(np.sum(A, axis=0, keepdims=False))


# GRADED FUNCTION: linear_backward

def linear_backward(dZ, cache):
    A_prev, W, b = cache
    m = A_prev.shape[1]

    dW = (1/m)*np.dot(dZ, A_prev.T)
    db = (1/m)*np.sum(dZ, axis=1, keepdims=True)
    dA_prev = np.dot(W.T, dZ)

    return dA_prev, dW, db


t_dZ, t_linear_cache = linear_backward_test_case()
t_dA_prev, t_dW, t_db = linear_backward(t_dZ, t_linear_cache)

print("dA_prev: " + str(t_dA_prev))
print("dW: " + str(t_dW))
print("db: " + str(t_db))

# GRADED FUNCTION: L_model_backward


def L_model_backward(AL, Y, caches):
    grads = {}
    L = len(caches)  # the number of layers
    m = AL.shape[1]
    Y = Y.reshape(AL.shape)  # after this line, Y is the same shape as AL

    dAL = dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))
    current_cache = caches[-1]
    grads["dA" + str(L-1)], grads["dW" + str(L)], grads["db" + str(L)] = linear_backward(sigmoid_backward(dAL,
                                                                                                          current_cache[1]),
                                                                                         current_cache[0])
    for l in reversed(range(L-1)):
        print(l)
        current_cache = caches[l]
        dA_prev_temp, dW_temp, db_temp = linear_backward(
            sigmoid_backward(dAL, current_cache[1]), current_cache[0])
        grads["dA" + str(l)] = dA_prev_temp
        grads["dW" + str(l + 1)] = dW_temp
        grads["db" + str(l + 1)] = db_temp

    return grads


t_AL, t_Y_assess, t_caches = L_model_backward_test_case()
grads = L_model_backward(t_AL, t_Y_assess, t_caches)

print("dA0 = " + str(grads['dA0']))
print("dA1 = " + str(grads['dA1']))
print("dW1 = " + str(grads['dW1']))
print("dW2 = " + str(grads['dW2']))
print("db1 = " + str(grads['db1']))
print("db2 = " + str(grads['db2']))

# GRADED FUNCTION: update_parameters


def update_parameters(parameters, grads, learning_rate):

    L = len(parameters) // 2  # number of layers in the neural network

    for l in range(L):
        parameters["W" + str(l + 1)] = parameters["W" + str(l + 1)] - \
            learning_rate * grads["dW" + str(l + 1)]
        parameters["b" + str(l + 1)] = parameters["b" + str(l + 1)] - \
            learning_rate * grads["db" + str(l + 1)]

    return parameters


t_parameters, grads = update_parameters_test_case()
t_parameters = update_parameters(t_parameters, grads, 0.1)

print("W1 = " + str(t_parameters["W1"]))
print("b1 = " + str(t_parameters["b1"]))
print("W2 = " + str(t_parameters["W2"]))
print("b2 = " + str(t_parameters["b2"]))
