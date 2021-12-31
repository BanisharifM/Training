import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load training data set from CSV file
training_data_df =

# Pull out columns for X (data to train with) and Y (value to predict)
X_training =
Y_training =

# Load testing data set from CSV file
test_data_df =

# Pull out columns for X (data to train with) and Y (value to predict)
X_testing =
Y_testing =

# All data needs to be scaled to a small range like 0 to 1 for the neural
# network to work well. Create scalers for the inputs and outputs.
X_scaler =
Y_scaler =

# Scale both the training inputs and outputs
X_scaled_training =
Y_scaled_training =

# It's very important that the training and test data are scaled with the same scaler.
X_scaled_testing =
Y_scaled_testing =

print(X_scaled_testing.shape)
print(Y_scaled_testing.shape)

print("Note: Y values were scaled by multiplying by {:.10f} and adding {:.4f}".format(Y_scaler.scale_[0], Y_scaler.min_[0]))
