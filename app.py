# app.py
import matplotlib.pyplot as plt

def plot_graph():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    plt.plot(x, y)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Simple Line Graph')
    plt.savefig('plot.png')

if __name__ == "__main__":
    plot_graph()
