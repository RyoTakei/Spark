def collision(x1, y1, w1, h1, x2, y2, w2, h2):
    '''
    this returns if two object it touching
    :param x1: x pos of object 1
    :param y1: y pos of object 1
    :param w1: width of object 1
    :param h1: height of object 1
    :param x2: x pos of object 2
    :param y2: y pos of object 2
    :param w2: width of object 2
    :param h2: height of object 2
    :return: True if two objects are touching.
    '''
    return x1 < x2 + w2 and y1 < y2 + h2 and x2 < x1 + w1 and y2 < y1 + h1
