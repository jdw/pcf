

class Fractal(object):
    def __init__(self, epsilon=0):
        pass

    def __str__(self):
        pass

    @staticmethod
    def CALCULATE(pos, max_iterations):
        x,y = pos
        iteration = 0
        Z = complex(0, 0)
        C = complex(float(x),float(y))

        while abs(Z) < 2.0 and iteration < max_iterations:
            Z = Z * Z + C
            iteration += 1

        return iteration

if __name__ == "__main__":
    print Fractal.CALCULATE((1,1), 30)

