import numpy as np

delR = int()
rArr = []
tArr = []

track = np.array([[(rArr[0] + 2 * delR, tArr[0]), (rArr[1] + 2 * delR, tArr[1]), (rArr[2] + 2 * delR, tArr[2]), (rArr[3] + 2 * delR, tArr[3]), (rArr[4] + 2 * delR, tArr[4])],
                  [(rArr[0] + delR, tArr[0]), (rArr[1] + delR, tArr[1]), (rArr[2] + delR, tArr[2]), (rArr[3] + delR, tArr[3]), (rArr[4] + delR, tArr[4])],
                  [(rArr[0], tArr[0]), (rArr[1], tArr[1]), (rArr[2], tArr[2]), (rArr[3], tArr[3]), (rArr[4], tArr[4])],
                  [(rArr[0] - delR, tArr[0]), (rArr[1] - delR, tArr[1]), (rArr[2] - delR, tArr[2]), (rArr[3] - delR, tArr[3]), (rArr[4] - delR, tArr[4])],
                  [(rArr[0] - 2 * delR, tArr[0]), (rArr[1] - 2 * delR, tArr[1]), (rArr[2] - 2 * delR, tArr[2]), (rArr[3] - 2 * delR, tArr[3]), (rArr[4] - 2 * delR, tArr[4])]
                  ])
