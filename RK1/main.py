# Юмаев ИУ7-55 РК1
# Метод классификации SVM

import numpy as np # Для работы с векторами
from matplotlib import pyplot as plt
from sklearn.datasets import make_classification, make_blobs
from itertools import combinations_with_replacement
from sklearn.datasets import load_iris
from itertools import product

class SVM:
    def __init__(self):
        pass

    def fit(self, data):
        self.data = data

        # {||w||: [w, b]} Contain any optimization values
        opt_dict = {}

        self.n_features = len(data[list(data.keys())[0]][0])
        print(self.n_features)
        arrays = [(-1, 1) for _ in range(self.n_features)]
        transforms = np.array(list(product(*arrays)))

        print(transforms)

        all_data = []
        for class_label in self.data:
            for featureset in self.data[class_label]:
                for feature in featureset:
                    all_data.append(feature)

        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        # no need to keep this memory.
        all_data=None

        # For our first pass, we'll take big steps (10%).
        # Once we find the minimum with these steps,
        # we're going to step down to a 1% step size to
        # continue finding the minimum here. Then, one more time,
        # we step down to 0.1% for fine tuning.
        step_sizes = [self.max_feature_value * 0.1,
                      self.max_feature_value * 0.01,
                      # starts getting very high cost after this.
                      self.max_feature_value * 0.001]

        b_range_multiple = 5
        b_multiple = 5
        latest_optimum = self.max_feature_value * 10

        # stepping down the vector
        print("Learning has been started...")
        for step in step_sizes:
            w = np.array([latest_optimum for i in range(self.n_features)])
            optimized = False
            while not optimized:
                for b in np.arange(-1 * (self.max_feature_value * b_range_multiple),
                                         self.max_feature_value * b_range_multiple,
                                   step * b_multiple):
                    for transformation in transforms:
                        w_t = w * transformation
                        found_option = True
                        for class_label in self.data:
                            for xi in self.data[class_label]:
                                yi = class_label
                                if not yi * (np.dot(w_t, xi) + b) >= 1:
                                    found_option = False
                                    
                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t, b]

                if w[0] < 0:
                    optimized = True
                else:
                    w = w - step

            norms = sorted([n for n in opt_dict])

            print(norms)
            
            #||w|| : [w, b]
            opt_choice = opt_dict[norms[0]]
            self.w = opt_choice[0]
            self.b = opt_choice[1]
            print(self.w)
            print(self.b)
            latest_optimum = opt_choice[0][0] + step * 2

    def predict(self, features):
        self.features = features
        # sign(x * w + b)
        prediction = np.sign(np.dot(np.array(features), self.w) + self.b)

        return prediction

# Данные для классификации
iris = load_iris(return_X_y=True)

"""
X0 = [iris[0][i] for i in range(len(iris[1])) if iris[1][i] == 0]
y0 = [iris[1][i] for i in range(len(iris[1])) if iris[1][i] == 0]
X1 = [iris[0][i] for i in range(len(iris[1])) if iris[1][i] == 1]
y1 = [iris[1][i] for i in range(len(iris[1])) if iris[1][i] == 1]

X0_train = X0[:40]
X0_test  = X0[40:]
y0_train = y0[:40]
y0_test  = y0[40:]

X1_train = X1[:40]
X1_test  = X1[40:]
y1_train = y1[:40]
y1_test  = y1[40:]

data_dict = {0: X0_train,
             1: X1_train}
"""

data_dict = {-1: np.array([[1, 7],
                           [2, 8],
                           [3, 8]]),
              1: np.array([[5, 1],
                           [6,-1],
                           [7, 3]])}

model = SVM()
model.fit(data_dict)
