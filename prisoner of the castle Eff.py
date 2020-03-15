a, b, c, d, e = int(input()), int(input()), int(
    input()), int(input()), int(input())

if (a <= d and c <= e) or (b <= d and c <= e) or (
        c <= d and a <= e) or (c <= d and b <= e):
    print('YES')
else:
    print('NO')
