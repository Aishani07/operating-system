# -------- FCFS --------
def fcfs(requests, head):
    seek_time = 0
    sequence = []

    for req in requests:
        seek_time += abs(head - req)
        sequence.append(req)
        head = req

    print("\nFCFS Sequence:", sequence)
    print("Total Seek Time:", seek_time)


# -------- SSTF --------
def sstf(requests, head):
    seek_time = 0
    sequence = []
    reqs = requests.copy()

    while reqs:
        nearest = min(reqs, key=lambda x: abs(x - head))
        seek_time += abs(head - nearest)
        sequence.append(nearest)
        head = nearest
        reqs.remove(nearest)

    print("\nSSTF Sequence:", sequence)
    print("Total Seek Time:", seek_time)


# -------- SCAN --------
def scan(requests, head, disk_size):
    seek_time = 0
    sequence = []

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort(reverse=True)
    right.sort()

    # Move right
    for r in right:
        seek_time += abs(head - r)
        sequence.append(r)
        head = r

    # Go to end
    seek_time += abs(head - (disk_size - 1))
    head = disk_size - 1

    # Move left
    for r in left:
        seek_time += abs(head - r)
        sequence.append(r)
        head = r

    print("\nSCAN Sequence:", sequence)
    print("Total Seek Time:", seek_time)


# -------- C-SCAN --------
def cscan(requests, head, disk_size):
    seek_time = 0
    sequence = []

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort()
    right.sort()

    # Move right
    for r in right:
        seek_time += abs(head - r)
        sequence.append(r)
        head = r

    # Jump to beginning
    seek_time += abs(head - (disk_size - 1))
    head = 0
    seek_time += disk_size - 1

    # Continue from start
    for r in left:
        seek_time += abs(head - r)
        sequence.append(r)
        head = r

    print("\nC-SCAN Sequence:", sequence)
    print("Total Seek Time:", seek_time)


# -------- MAIN PROGRAM --------
n = int(input("Enter number of requests: "))
requests = list(map(int, input("Enter request sequence: ").split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size: "))

# Calling all functions
fcfs(requests, head)
sstf(requests, head)
scan(requests, head, disk_size)
cscan(requests, head, disk_size)