import math

class calc:
    def exp(self, _list):
        layer_outputs = list(_list)
        #E = 2.71828182846
        E = math.e

        exp_values = []

        for output in layer_outputs:
            exp_values.append(E**output)

        return exp_values