# =========================================
# CPU Scheduling: FCFS & SJF (Non-Preemptive)
# =========================================

class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0


# =========================================
# DISPLAY FUNCTION
# =========================================
def display(processes, title):
    print(f"\n===== {title} =====")
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")


# =========================================
# FCFS
# =========================================
def fcfs(processes):
    processes.sort(key=lambda x: x.at)

    time = 0
    gantt = []

    for p in processes:
        if time < p.at:
            time = p.at

        start = time
        time += p.bt

        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        gantt.append((p.pid, start, time))

    return processes, gantt


# =========================================
# SJF (Non-Preemptive)
# =========================================
def sjf(processes):
    n = len(processes)
    completed = 0
    time = 0
    visited = [False] * n
    gantt = []

    while completed < n:
        idx = -1
        min_bt = float('inf')

        for i in range(n):
            if processes[i].at <= time and not visited[i]:
                if processes[i].bt < min_bt:
                    min_bt = processes[i].bt
                    idx = i

        if idx == -1:
            time += 1
            continue

        p = processes[idx]
        start = time
        time += p.bt

        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        visited[idx] = True
        completed += 1

        gantt.append((p.pid, start, time))

    return processes, gantt


# =========================================
# GANTT CHART
# =========================================
def print_gantt(gantt):
    print("\nGantt Chart:")
    for p in gantt:
        print(f"| {p[0]} ", end="")
    print("|")

    print("0", end="")
    for p in gantt:
        print(f"\t{p[2]}", end="")
    print()


# =========================================
# AVERAGES
# =========================================
def calculate_avg(processes):
    n = len(processes)
    avg_tat = sum(p.tat for p in processes) / n
    avg_wt = sum(p.wt for p in processes) / n
    return avg_tat, avg_wt


# =========================================
# MAIN DRIVER
# =========================================
if __name__ == "__main__":

    processes_input = [
        Process("P1", 0, 6),
        Process("P2", 2, 8),
        Process("P3", 4, 7),
        Process("P4", 6, 3),
        Process("P5", 8, 4)
    ]

    # Display Input
    print("Initial Processes:")
    print("PID\tAT\tBT")
    for p in processes_input:
        print(f"{p.pid}\t{p.at}\t{p.bt}")

    # FCFS
    fcfs_processes = [Process(p.pid, p.at, p.bt) for p in processes_input]
    fcfs_result, fcfs_gantt = fcfs(fcfs_processes)
    display(fcfs_result, "FCFS Scheduling")
    print_gantt(fcfs_gantt)

    avg_tat, avg_wt = calculate_avg(fcfs_result)
    print(f"\nFCFS Avg TAT: {avg_tat:.2f}")
    print(f"FCFS Avg WT: {avg_wt:.2f}")

    # SJF
    sjf_processes = [Process(p.pid, p.at, p.bt) for p in processes_input]
    sjf_result, sjf_gantt = sjf(sjf_processes)
    display(sjf_result, "SJF Scheduling")
    print_gantt(sjf_gantt)

    avg_tat, avg_wt = calculate_avg(sjf_result)
    print(f"\nSJF Avg TAT: {avg_tat:.2f}")
    print(f"SJF Avg WT: {avg_wt:.2f}")
