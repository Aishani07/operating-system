# =========================================
# Banker's Algorithm Implementation
# =========================================

def calculate_need(max_matrix, allocation, n, m):
    need = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(max_matrix[i][j] - allocation[i][j])
        need.append(row)
    return need


def bankers_algorithm(n, m, allocation, max_matrix, available):
    need = calculate_need(max_matrix, allocation, n, m)

    print("\nNeed Matrix:")
    for row in need:
        print(row)

    work = available[:]
    finish = [False] * n
    safe_sequence = []

    while len(safe_sequence) < n:
        found = False

        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):

                    print(f"\nProcess P{i} is executing")
                    print("Work before:", work)

                    for j in range(m):
                        work[j] += allocation[i][j]

                    print("Work after:", work)

                    safe_sequence.append(i)
                    finish[i] = True
                    found = True

        if not found:
            break

    if len(safe_sequence) == n:
        print("\nSystem is in SAFE STATE")
        print("Safe Sequence:", " -> ".join([f"P{i}" for i in safe_sequence]))
    else:
        print("\nSystem is in UNSAFE STATE")


# =========================================
# MAIN DRIVER CODE (TEST CASE)
# =========================================

if __name__ == "__main__":

    # Number of processes and resources
    n = 5
    m = 3

    # Allocation Matrix
    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    # Maximum Matrix
    max_matrix = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]

    # Available Resources
    available = [3, 3, 2]

    bankers_algorithm(n, m, allocation, max_matrix, available)
