import argparse


class ArgParser():
    """
    THis class is used for parameter parse.

    Attributes:
        args: An argparse class to parase parameters.
    """

    def __init__(self):
        """
        Defiune what kinds of parameters we need.
        """
        parser = argparse.ArgumentParser(description="Working for image processing")
        parser.add_argument("dataPath", type=str, help="Dataset path(relative path)")
        parser.add_argument("-b", "--batch_size", type=int, default=32, help="input batch size")
        parser.add_argument("-l", "--learning_rate", type=float, default=0.01)
        parser.add_argument("-c", "--class_num", type=int,default=10)
        self.args = parser.parse_args()

    def show(self):
        """
        Print all the parameters.
        :return: None
        """
        args_show = vars(self.args)
        print("------  The hyper parameters is  ------")
        for i,item in enumerate(vars(self.args)):
            print(i,":",item," => ", args_show[item])
        print("---------------------------------------")