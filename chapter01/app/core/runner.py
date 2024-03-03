class Runner(object):
    def __init__(self, learner):
        self.__leaner = learner

    def go(self, train_x: list, train_y: list, test_x: list):
        self.__leaner.fit(train_x, train_y)
        test_y = self.__leaner.predict(test_x)
        return test_y
