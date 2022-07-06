import numpy as np
import matplotlib.pyplot as plt


def distance(my_data):
    with open('distance.csv', 'a') as f:
        max_distance = 0
        min_distance = 0
        max_pair = ()
        min_pair = ()
        for i in range(len(my_data)):
            for j in range(i+1, len(my_data)):
                distance = np.sqrt(np.dot(my_data[i]-my_data[j], my_data[i]-my_data[j]))
                f.writelines('{}\n'.format(distance))
                if distance >= max_distance:
                    max_distance = distance
                    max_pair = (i, j)
        min_distance = max_distance
        for i in range(len(my_data)):
            for j in range(i+1, len(my_data)):
                distance = np.sqrt(np.dot(my_data[i]-my_data[j], my_data[i]-my_data[j]))
                if distance < min_distance:
                    min_distance = distance
                    min_pair = (i, j)
    return min_pair, min_distance, max_pair, max_distance


def histogram(max_distance):
    bins = []
    x = 0
    for i in range(int((max_distance) * 10)):
        bins.append(round(x, 1))
        x += 0.1
    print(round(max_distance) * 10)
    plt.hist(np.loadtxt('distance.csv'), bins=bins)
    plt.title('Распределение расстояний ')
    plt.xlabel('Расстояния')
    plt.ylabel('Частота')
    plt.grid(True)
    plt.show()


def main():
    my_data = np.genfromtxt('vectors.csv', delimiter=',')
    min_pair, min_distance, max_pair, max_distance = distance(my_data)
    print(min_pair, min_distance, max_pair, max_distance)
    histogram(max_distance)


if __name__ == "__main__":
    main()
