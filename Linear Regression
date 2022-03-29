import numpy as np
import matplotlib.pyplot as plt

# Setup
random_noise = np.random.randint(-100, 100, 100) * 0.1
initial_data = np.arange(10,110,1)
data_plus_noise = random_noise + initial_data

features_array = np.array([])
start_array = []
for i in range(101):
    start_array.append([1, i])

features_array = np.array(start_array)

# For a future implementation
examples_array = np.vstack((np.arange(1,101,1), data_plus_noise)).T

# Initialize theta with 1 feature
theta = np.zeros(2)

# Number of training examples
m = len(data_plus_noise)

# Length of theta must be equal to length of X plus 1
def hypothesis_function(theta, X):
    # Concatenate 0 at the beginning to make both arrays of equal size
    return np.sum(np.multiply(theta, X))

def partial_sum(features_array, labels_array, j: int):
    sum = 0
    for i in range(len(labels_array)):
        sum += (hypothesis_function(theta, features_array[i]) - labels_array[i]) * features_array[i][j]
    return sum

def batch_gradient_descent(learning_rate, features_array, labels_array, theta):
    for j in range(len(theta)):
        theta[j] = theta[j] - learning_rate * partial_sum(features_array, labels_array, j)

for i in range(201):
    batch_gradient_descent(.000001, features_array, data_plus_noise, theta)
    line_values = []
    for i in range(101):
        line_values.append(theta[0] + theta[1] * i)
        plt.plot(data_plus_noise, 'ro', line_values)
    
    plt.pause(1)

plt.show()


