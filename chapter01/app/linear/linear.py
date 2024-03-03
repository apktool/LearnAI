from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

from app.core.runner import Runner


class Linear(object):
    def base(self):
        model = linear_model.LinearRegression()
        runner: Runner = Runner(model)
        train_x = [[0, 0], [1, 1], [2, 2]]
        train_y = [0, 1, 2]
        test_x = [[1, 1], [5, 5]]
        test_y = [1, 5]
        pred_y = runner.go(train_x, train_y, test_x)
        print(pred_y)
        # The coefficients
        print("Coefficients: ", model.coef_)
        # The mean squared error
        print("Mean squared error: %.2f" % mean_squared_error(test_y, pred_y))
        # The coefficient of determination: 1 is perfect prediction
        print("Coefficient of determination: %.2f" % r2_score(test_y, pred_y))
