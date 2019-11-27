# Юмаев ИУ7-55 РК1
# Метод классификации SVM

import numpy as np # Для работы с векторами
from matplotlib import pyplot as plt


class SVM:
    def __init__(self):
        pass

    def fit(self, data):
        self.data = data

        # {||w||: [w, b]} Contain any optimization values
        opt_dict = {}

        transforms = [[ 1, 1],
                      [-1, 1],
                      [-1,-1],
                      [ 1,-1]]

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
        latest_optimum = self.max_feature_value*10

        # stepping down the vector
        for step in step_sizes:
            w = np.array([latest_optimum, latest_optimum])
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
                    print('Optimized a step.')
                else:
                    w = w - step

            norms = sorted([n for n in opt_dict])
            #||w|| : [w,b]
            opt_choice = opt_dict[norms[0]]
            self.w = opt_choice[0]
            self.b = opt_choice[1]
            latest_optimum = opt_choice[0][0] + step * 2

    def predict(self, features):
        self.features = features
        # sign(x * w + b)
        prediction = np.sign(np.dot(np.array(features), self.w) + self.b)

        return prediction

# Данные для классификации
data_dict = {-1: np.array([[1, 7],
                           [2, 8],
                           [3, 8]]),
              1: np.array([[5, 1],
                           [6,-1],
                           [7, 3]])}

model = SVM()
model.fit(data_dict)
