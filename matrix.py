m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m3 = []
for i in range(len(m1)):
    for j in range(len(m1[i])):
        m3.append(m1[i][j] + m2[i][j])

print(m3)