def rotate_matrix(M: list[list[int]]) -> None:
    n = len(M)
    last = n - 1

    for i in range(n // 2):
        for j in range(i, last-i):
            temp = M[i][j]
            M[i][j] = M[j][last-i]
            M[j][last-i] = M[last-i][last-j]
            M[last-i][last-j] = M[last-j][i]
            M[last-j][i] = temp


if __name__ == '__main__':
    M = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15]]
    rotate_matrix(M)
    for row in M:
        print(row)
