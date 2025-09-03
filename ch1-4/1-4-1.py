from math import sqrt

def dist(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def perimeter(A, B, C, D):
    return dist(A, B) + dist(B, C) + dist(C, D) + dist(D, A)

if __name__ == '__main__':
    print(perimeter(
        (-1.50, -1.00), (1.50, -1.00),
        (2.00, 1.00), (-1.00, 1.00)
    ))