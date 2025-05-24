import matplotlib.pyplot as plt

# funkcja 1: y = 5x - 2 ; funkcja 2: y = -2x + 5 ; funkcja 3: y = 3x + 3

# X = []
# for i in range(-10, 10):
#     X.append(i)
#
# X = list(range(-10, 10))

X = [i for i in range(-10, 10)]

# y1 = []
# for i in X:
#     y1.append(5 * i -2)

y1 = [5 * i - 2 for i in X]