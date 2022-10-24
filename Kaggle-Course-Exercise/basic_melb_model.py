import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

melbourne_file_path = '/Users/gk/Desktop/コード/kaggle-ML/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)


def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    # Fit the model with the training data
    model.fit(train_X, train_y)
    predictions_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, predictions_val)
    return mae


melbourne_data = melbourne_data.dropna(axis=0)
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
melbourne_features_2 = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude', 'Price']
X = melbourne_data[melbourne_features]
# print(X.describe())
# print("\n\nThis is the head values of X:\n")
# print(X.head(4))
# To split the data into training and validation data:
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
# compare MAE with differing values of max_leaf_nodes
min_mae = 10e18
optimum_max_leaf_nodes = 0
for max_leaf_nodes in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    if my_mae < min_mae:
        min_mae = my_mae
        optimum_max_leaf_nodes = max_leaf_nodes

print("Optimum max leaf nodes: %d  \t\t Best Mean Absolute Error:  %d" % (optimum_max_leaf_nodes, min_mae))

# print("Making predictions for the following 6 houses:")
# print(X.head(6))
# print("\n\nThe predictions are:")
# print(melbourne_model.predict(X.head()))
# print("\nPrices are:")
# print(X_2.head())


""" RANDOM FORESTS """
print("\nRandom Forests:")
from sklearn.ensemble import RandomForestRegressor

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melbourne_predictions = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melbourne_predictions))
