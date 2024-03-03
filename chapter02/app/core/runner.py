class Runner(object):
    def __init__(self, learner):
        self.__leaner = learner

    def go(self, train_x: list, test_x: list):
        self.__leaner.fit(train_x)
        test_y = self.__leaner.predict(test_x)
        return test_y
