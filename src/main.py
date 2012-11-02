
from fractal import Fractal
from util import drange

def main():
    epsilon=0.1
    for x in drange(-2, 2, epsilon):
        for y in drange(-2, 2, epsilon):
            print Fractal.CALCULATE((x,y), 30)

if __name__ == "__main__":
    main()
