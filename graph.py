import matplotlib.pyplot as plt
import random
def main():
    xVal = [1,2,3]
    yVal = [3,6,2]

    # the histogram of the data
    plt.plot(xVal, yVal)

    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.grid(True)
    plt.show()

if __name__=="__main__":
    main()