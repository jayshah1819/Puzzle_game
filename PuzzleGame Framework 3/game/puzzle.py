import numpy as np

v = [10, 0, 0, 0, 1]
q = [[10, 10], [0, 0], [0, 0], [0, 0], [1, 1]]

# Parameters
gamma = 0.99  # Discount factor
r = 1


for t in range(10):
    v_new = v.copy()  # new copy of v
    for i in range(1, len(v) - 1):
        q[i][0] = gamma * v[i - 1] + r  # left action
        q[i][1] = gamma * v[i + 1] + r  # right ation
        v_new[i] = max(q[i][0], q[i][1])
    v = v_new.copy()
    print(t, v[1], v[2], v[3])
# print(t, q[1][0], q[1][1])
