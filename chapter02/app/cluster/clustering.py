from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error, r2_score

from app.core.runner import Runner


class Cluster(object):
    def base(self):
        model = KMeans(n_clusters=2, random_state=0)
        runner: Runner = Runner(model)
        train_x = [[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]]
        test_x = [[0, 0], [4, 4]]
        test_y = [1, 1]
        pred_y = runner.go(train_x, test_x)
        print(pred_y)
        # The coefficients
        print(model.cluster_centers_)
        print("Coefficients: ", model.labels_)
        # The mean squared error
        print("Mean squared error: %.2f" % mean_squared_error(test_y, pred_y))
        # The coefficient of determination: 1 is perfect prediction
        print("Coefficient of determination: %.2f" % r2_score(test_y, pred_y))
