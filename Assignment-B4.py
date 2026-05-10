def solve(i, cols, ld, rd, cur, n):
    if i == n: return True
    for j in range(n):
        if cols[j] or rd[i+j] or ld[i-j+n-1]: continue
        cols[j] = rd[i+j] = ld[i-j+n-1] = 1
        cur.append(j)
        if solve(i+1, cols, ld, rd, cur, n): return True
        cur.pop()
        cols[j] = rd[i+j] = ld[i-j+n-1] = 0
    return False

def nQueen(n):
    cols, ld, rd, cur = [0]*n, [0]*(2*n), [0]*(2*n), []
    if solve(0, cols, ld, rd, cur, n):
        b = [['.']*n for _ in range(n)]
        for i in range(n): b[i][cur[i]] = 'Q'
        for row in b: print(" ".join(row))
    else: print("No solution exists.")

nQueen(int(input("Enter the number of queens:\t")))
