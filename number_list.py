import statistics
import random
import mean_and_variance

class NumberList:
    def __init__(self):
        self._data = []

    def getData(self):
        return self._data

    def setData(self, data):
        self._data = data

    def mean(self):
        return mean_and_variance.mean(self._data)

    def variance(self):
        return mean_and_variance.variance(self._data)

    @staticmethod
    def _getNDataFromKeyboard():
        ndata = 0
        gotNDataCorrectly = False
        while gotNDataCorrectly == False:
            try:
                ndata = float(input())
                if ndata % 1 == 0 and ndata >= 2:
                    gotNDataCorrectly = True
                else:
                    print("_getNDataFromKeyboard: ndata should be >=2 and an integer!")
            except (ValueError, SyntaxError):
                print("_getNDataFromKeyboard: ndata should be an integer!") # end while loop
        return int(ndata) # return ndata as int

    def getDataFromKeyboard(self):
        data_list = []
        for i in range(5):
            input_data = self._getNDataFromKeyboard()
            data_list.append(input_data)
        self.setData(data_list)

    def getRandomData(self, ndata, range1, range2=0):
        if range1 >= range2:
            print("range1 should be > range2")
            return False
        elif ndata % 1 != 0 or ndata < 2:
            print("ndata should be >=2 and an integer")
        else:
            input_data = []
            try:
                for i in range(int(ndata)):
                    input_data.append(round(random.uniform(range1, range2),1))
            except():
                print("ERROR")
            finally:
                self.setData(input_data)


if __name__ == '__main__':
    # Part1
    test_data_1 = [0.1, 1.1, 2.1, 3.1, 4.1]
    test_data_list = NumberList()
    test_data_list.setData(test_data_1)
    print("Numbers: " + str(test_data_list.getData()))
    print("Mean: " + str(test_data_list.mean()))
    print("Variance: " + str(test_data_list.variance()))

    # Part2
    test_data_list_2 = NumberList()
    test_data_list_2.getDataFromKeyboard()
    print("Numbers: " + str(test_data_list_2.getData()))
    print("Mean: " + str(test_data_list_2.mean()))
    print("Variance: " + str(test_data_list_2.variance()))

    # Part3
    test_data_list_3 = NumberList()
    test_data_list_3.getRandomData(5, 10, 20)
    print("Numbers: " + str(test_data_list_3.getData()))
    print("Mean: " + str(test_data_list_3.mean()))
    print("Variance: " + str(test_data_list_3.variance()))