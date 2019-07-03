def max(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for idx in range(2, len(x)):
        if x[idx] > m1:
            m2 = m1
            m1 = x[idx]
        elif x[idx] > m2:
            m2 = x[idx]
    return m1, m2