def fcfs(requests, head):
    seek_time = 0
    sequence = []

    print("\nFCFS Simulation:")
    for req in requests:
        seek = abs(head - req)
        seek_time += seek
        print(f"Move from {head} to {req} -> Seek = {seek}")
        head = req
        sequence.append(req)

    print("Sequence:", sequence)
    return seek_time


def sstf(requests, head):
    seek_time = 0
    requests = requests.copy()
    sequence = []

    print("\nSSTF Simulation:")
    while requests:
        nearest = min(requests, key=lambda x: abs(x - head))
        seek = abs(head - nearest)
        seek_time += seek
        print(f"Move from {head} to {nearest} -> Seek = {seek}")
        head = nearest
        sequence.append(nearest)
        requests.remove(nearest)

    print("Sequence:", sequence)
    return seek_time


def scan(requests, head, disk_size):
    seek_time = 0
    sequence = []

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort(reverse=True)
    right.sort()

    print("\nSCAN Simulation:")

    # Move right
    for r in right:
        seek = abs(head - r)
        seek_time += seek
        print(f"Move from {head} to {r} -> Seek = {seek}")
        head = r
        sequence.append(r)

    # Go to end
    end = disk_size - 1
    seek = abs(head - end)
    seek_time += seek
    print(f"Move from {head} to {end} -> Seek = {seek}")
    head = end

    # Reverse direction
    for r in left:
        seek = abs(head - r)
        seek_time += seek
        print(f"Move from {head} to {r} -> Seek = {seek}")
        head = r
        sequence.append(r)

    print("Sequence:", sequence)
    return seek_time


def cscan(requests, head, disk_size):
    seek_time = 0
    sequence = []

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort()
    right.sort()

    print("\nC-SCAN Simulation:")

    # Move right
    for r in right:
        seek = abs(head - r)
        seek_time += seek
        print(f"Move from {head} to {r} -> Seek = {seek}")
        head = r
        sequence.append(r)

    # Move to end
    end = disk_size - 1
    seek = abs(head - end)
    seek_time += seek
    print(f"Move from {head} to {end} -> Seek = {seek}")

    # Jump to beginning
    print(f"Jump from {end} to 0")
    seek_time += end
    head = 0

    # Continue left side
    for r in left:
        seek = abs(head - r)
        seek_time += seek
        print(f"Move from {head} to {r} -> Seek = {seek}")
        head = r
        sequence.append(r)

    print("Sequence:", sequence)
    return seek_time


# ---------------- MAIN PROGRAM ----------------
def main():
    print("=== Disk Scheduling Simulator ===")

    # Task 1: Input
    n = int(input("Enter number of disk requests: "))
    requests = list(map(int, input("Enter request sequence: ").split()))
    head = int(input("Enter initial head position: "))
    disk_size = int(input("Enter disk size: "))

    print("\nRequest Queue:", requests)
    print("Initial Head Position:", head)

    # Run Algorithms
    fcfs_time = fcfs(requests, head)
    sstf_time = sstf(requests, head)
    scan_time = scan(requests, head, disk_size)
    cscan_time = cscan(requests, head, disk_size)

    # Task 6: Comparison
    print("\n=== Performance Comparison ===")
    results = {
        "FCFS": fcfs_time,
        "SSTF": sstf_time,
        "SCAN": scan_time,
        "C-SCAN": cscan_time
    }

    for algo, time in results.items():
        print(f"{algo}: Total Seek Time = {time}")

    # Task 7: Analysis
    best = min(results, key=results.get)
    worst = max(results, key=results.get)

    print("\n=== Result Analysis ===")
    print(f"Best Algorithm: {best} (Minimum Seek Time = {results[best]})")
    print(f"Worst Algorithm: {worst} (Maximum Seek Time = {results[worst]})")

    print("\nConclusion:")
    print("- SSTF usually gives better performance than FCFS.")
    print("- SCAN provides balanced performance (elevator movement).")
    print("- C-SCAN ensures uniform waiting time.")
    print("- FCFS is simple but inefficient for large movements.")


# Run program
main()
