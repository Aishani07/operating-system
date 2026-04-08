class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.rt = bt   # remaining time
        self.ct = 0
        self.tat = 0
        self.wt = 0


# ---------- Input Handling ----------
n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    print(f"\nProcess {i+1}")
    at = int(input("Arrival Time: "))
    bt = int(input("Burst Time: "))
    processes.append(Process(i+1, at, bt))

tq = int(input("\nEnter Time Quantum: "))


# ---------- Display Input ----------
print("\nInput Table:")
print("PID\tAT\tBT")
for p in processes:
    print(f"P{p.pid}\t{p.at}\t{p.bt}")


# ---------- Round Robin Scheduling ----------
time = 0
queue = []
gantt = []
visited = [False] * n
completed = 0

while completed < n:

    # Add arrived processes to queue
    for i in range(n):
        if processes[i].at <= time and not visited[i]:
            queue.append(processes[i])
            visited[i] = True

    if not queue:
        time += 1
        continue

    current = queue.pop(0)

    # Execute process
    if current.rt > tq:
        gantt.append((current.pid, time, time + tq))
        time += tq
        current.rt -= tq
    else:
        gantt.append((current.pid, time, time + current.rt))
        time += current.rt
        current.rt = 0
        current.ct = time
        completed += 1

    # Add newly arrived processes during execution
    for i in range(n):
        if processes[i].at <= time and not visited[i]:
            queue.append(processes[i])
            visited[i] = True

    # If process not finished, re-add to queue
    if current.rt > 0:
        queue.append(current)


# ---------- Calculate TAT & WT ----------
for p in processes:
    p.tat = p.ct - p.at
    p.wt = p.tat - p.bt


# ---------- Output Table ----------
print("\nOutput Table:")
print("PID\tAT\tBT\tCT\tTAT\tWT")

total_tat = 0
total_wt = 0

for p in processes:
    total_tat += p.tat
    total_wt += p.wt
    print(f"P{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

print("\nAverage Turnaround Time =", round(total_tat / n, 2))
print("Average Waiting Time =", round(total_wt / n, 2))


# ---------- Gantt Chart ----------
print("\nGantt Chart:")
for g in gantt:
    print(f"| P{g[0]} ", end="")
print("|")

print(gantt[0][1], end="")
for g in gantt:
    print(f"   {g[2]}", end="")
print()