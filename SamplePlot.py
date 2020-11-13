import matplotlib.pyplot as plt

if __name__ == '__main__':
    img = plt.imread("RealisticMap.jpg")
    plt.imshow(img, extent=[-180, 180, -90, 90])
    plt.scatter(0, 0, color='red')
    plt.draw()
    plt.scatter(100, 75, color='red')
    plt.draw()
    plt.show()
