def read_single_set(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        a, b, c = map(float, line.split())
    return a, b, c

a, b, c = read_single_set('input.txt')
r1, r2 = solve_quadratic(a, b, c)
if r1 is None:
    print("No real roots")
else:
    print(f"Roots: {r1}, {r2}")
