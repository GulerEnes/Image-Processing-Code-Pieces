import cv2
from matplotlib import pyplot as plt


# Activate these two line if code doesn't work because of Qt error
# import matplotlib
# matplotlib.use('TkAgg')

def makeCumulative(arr):
    kum = [arr[0]] * 255
    for i in range(1, len(arr) - 1):
        kum[i] = kum[i - 1] + arr[i]
    return kum


img = cv2.imread('7.jpeg', 0)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
hist = [int(i[0]) for i in hist]

histKum = makeCumulative(hist)

fig1 = plt.figure()
fig2 = plt.figure()

ax1 = fig1.add_subplot()
ax2 = fig2.add_subplot()

ax1.plot(hist)
ax2.plot(histKum)

plt.show()
