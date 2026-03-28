print("$ python3 bankers.py")

# Function to safely take matrix input
def input_matrix(name, n, m):
    matrix = []
    print(f"Enter {name}:")
    for i in range(n):
        while True:
            try:
                row = list(map(int, input(f"Row {i}: ").split()))
                if len(row) != m:
                    print(f" Enter exactly {m} values")
                    continue
                matrix.append(row)
                break
            except:
                print(" Invalid input, try again")
    return matrix

# Function to safely take available resources
def input_available(m):
    while True:
        try:
            row = list(map(int, input("Enter Available Resources: ").split()))
            if len(row) != m:
                print(f" Enter exactly {m} values")
                continue
            return row
        except:
            print(" Invalid input, try again")

# Input n, m safely
while True:
    try:
        n = int(input("Enter number of processes: "))
        m = int(input("Enter number of resources: "))
        break
    except:
        print(" Enter valid numbers")

# Take matrices
alloc = input_matrix("Allocation Matrix", n, m)
maxm = input_matrix("Max Matrix", n, m)

# Validate Allocation <= Max
while True:
    valid = True
    for i in range(n):
        for j in range(m):
            if alloc[i][j] > maxm[i][j]:
                print(f" Allocation > Max at P{i}, Resource {j}")
                print("Re-enter Max Matrix correctly")
                maxm = input_matrix("Max Matrix", n, m)
                valid = False
                break
        if not valid:
            break
    if valid:
        break

avail = input_available(m)

# Need matrix
need = [[maxm[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]

finish = [False] * n
safeSeq = []

while len(safeSeq) < n:
    found = False
    for p in range(n):
        if not finish[p]:
            if all(need[p][j] <= avail[j] for j in range(m)):
                for j in range(m):
                    avail[j] += alloc[p][j]
                safeSeq.append(p)
                finish[p] = True
                found = True
    if not found:
        print("System is NOT in safe state ")
        break

if len(safeSeq) == n:
    print("System is in SAFE state ")
    print("Safe sequence:", " -> ".join(f"P{i}" for i in safeSeq))