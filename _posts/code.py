import sys
input = sys.stdin.readline
n = int(input())

ans = 0
#가로줄에 퀸 하나니까
# row = [0] * n
# col_lock = [False] * n
col = []
#재귀함수
def n_queens(x):
    global ans
    global col_lock
    if x == n:
        ans += 1
        return

    else:
        for y in range(n):
            if y not in col:
                # [x, y]에 퀸을 놓겠다.
                # row[x] = y
                if is_promising(x,y):
                    col.append(y)
                    n_queens(x+1)
                    col.pop()

#promising함수
def is_promising(x,y):
    for i in range(len(col)):
        # 같은 세로열이면 안됨.
        # 대각선 라인에 있으면 안됨.
        if abs(y - col[i]) == x - i:
            return False

    return True

n_queens(0)
print(ans)