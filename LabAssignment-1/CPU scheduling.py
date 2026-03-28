# Process Class
class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at  # Arrival Time
        self.bt = bt  # Burst Time
        self.ct = 0   # Completion Time
        self.tat = 0  # Turnaround Time
        self.wt = 0   # Waiting Time


# ------------------ Input ------------------
def take_input():
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        print(f"\nEnter details for Process {i+1}")
        pid = input("Process ID: ")
        at = int(input("Arrival Time: "))
        bt = int(input("Burst Time: "))
        processes.append(Process(pid, at, bt))

    return processes


# ------------------ Display Table ------------------
def display(processes):
    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")


# ------------------ FCFS ------------------
def fcfs(processes):
    processes.sort(key=lambda x: x.at)
    time = 0
    gantt = []

    for p in processes:
        if time < p.at:
            time = p.at  # CPU idle condition

        start = time
        time += p.bt
        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        gantt.append((p.pid, start, time))

    return gantt


# ------------------ SJF (Non-Preemptive) ------------------
def sjf(processes):
    processes.sort(key=lambda x: x.at)
    n = len(processes)

    completed = []
    ready = []
    time = 0
    i = 0
    gantt = []

    while len(completed) < n:

        # Add arrived processes to ready queue
        while i < n and processes[i].at <= time:
            ready.append(processes[i])
            i += 1

        if ready:
            # Select process with shortest burst time
            ready.sort(key=lambda x: x.bt)
            p = ready.pop(0)

            start = time
            time += p.bt

            p.ct = time
            p.tat = p.ct - p.at
            p.wt = p.tat - p.bt

            completed.append(p)
            gantt.append((p.pid, start, time))
        else:
            time += 1  # CPU idle

    return completed, gantt


# ------------------ Gantt Chart ------------------
def print_gantt(gantt):
    print("\nGantt Chart:")
    for p in gantt:
        print(f"| {p[0]} ", end="")
    print("|")

    print(gantt[0][1], end="")
    for p in gantt:
        print(f"\t{p[2]}", end="")
    print("\n")


# ------------------ Averages ------------------
def calculate_avg(processes):
    total_wt = sum(p.wt for p in processes)
    total_tat = sum(p.tat for p in processes)

    avg_wt = total_wt / len(processes)
    avg_tat = total_tat / len(processes)

    return avg_wt, avg_tat


# ------------------ Main ------------------
processes = take_input()

# FCFS
import copy
fcfs_processes = copy.deepcopy(processes)
fcfs_gantt = fcfs(fcfs_processes)

print("\n--- FCFS Scheduling ---")
display(fcfs_processes)
print_gantt(fcfs_gantt)

fcfs_avg_wt, fcfs_avg_tat = calculate_avg(fcfs_processes)
print(f"Average Waiting Time: {fcfs_avg_wt:.2f}")
print(f"Average Turnaround Time: {fcfs_avg_tat:.2f}")


# SJF
sjf_processes = copy.deepcopy(processes)
sjf_result, sjf_gantt = sjf(sjf_processes)

print("\n--- SJF Scheduling (Non-Preemptive) ---")
display(sjf_result)
print_gantt(sjf_gantt)

sjf_avg_wt, sjf_avg_tat = calculate_avg(sjf_result)
print(f"Average Waiting Time: {sjf_avg_wt:.2f}")
print(f"Average Turnaround Time: {sjf_avg_tat:.2f}")


# ------------------ Comparison ------------------
print("\n--- Comparison ---")
if sjf_avg_wt < fcfs_avg_wt:
    print("SJF has lower waiting time → Better")
else:
    print("FCFS has lower waiting time → Better")

if sjf_avg_tat < fcfs_avg_tat:
    print("SJF has lower turnaround time → Better")
else:
    print("FCFS has lower turnaround time → Better")