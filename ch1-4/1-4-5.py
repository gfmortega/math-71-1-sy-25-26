# l, r, b, t
def aabb_of_circle(h, k, r):
    return h-r, h+r, k-r, k+r

def aabb_of_square(x, y, s):
    return x, x+s, y, y+s

def aabb_of_triangle(x1, y1, x2, y2, x3, y3):
    return (
        min(x1, x2, x3),
        max(x1, x2, x3),
        min(y1, y2, y3),
        max(y1, y2, y3),
    )

def aabb_of_shape(kind, data):
    if kind == 'circle':
        return aabb_of_circle(*data)
    elif kind == 'triangle':
        return aabb_of_triangle(*data)
    elif kind == 'square':
        return aabb_of_square(*data)
    else:
        raise RuntimeError(f'{kind} is unexpected shape')
    
def aabb_area(shape1, shape2, shape3):
    l1, r1, b1, t1 = aabb_of_shape(shape1[0], shape1[1:])
    l2, r2, b2, t2 = aabb_of_shape(shape2[0], shape2[1:])
    l3, r3, b3, t3 = aabb_of_shape(shape3[0], shape3[1:])

    # the leftmost boundary of the rectangle has to be
    #   lefter than all the points of the shapes;
    #   or, lefter than the leftmost point of each shape
    L = min(l1, l2, l3)
    R = max(r1, r2, r3)
    B = min(b1, b2, b3)
    T = max(t1, t2, t3)
    return (R - L) * (T - B)