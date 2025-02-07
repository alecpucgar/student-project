import matplotlib.pyplot as plt
import pandas as pd
if __name__ == '__main__':
    data = pd.read_csv('data/data.csv')
    plt.title('Data Analysis')
    plt.plot(data.iloc[:, 0], data.iloc[:, 1])
    plt.show()
