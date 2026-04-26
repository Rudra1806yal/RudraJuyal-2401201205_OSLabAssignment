def display_frames(frames):
    return " ".join(str(x) if x != -1 else "-" for x in frames)


# ---------------- FIFO ----------------
def fifo(pages, capacity):
    frames = [-1] * capacity
    queue = []
    faults = 0

    print("\nFIFO Simulation:")
    for page in pages:
        if page not in frames:
            faults += 1
            if -1 in frames:
                idx = frames.index(-1)
                frames[idx] = page
                queue.append(idx)
            else:
                idx = queue.pop(0)
                frames[idx] = page
                queue.append(idx)
        print(f"{page} -> {display_frames(frames)}")
    return faults


# ---------------- LRU ----------------
def lru(pages, capacity):
    frames = []
    faults = 0

    print("\nLRU Simulation:")
    for page in pages:
        if page not in frames:
            faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
        else:
            frames.remove(page)
            frames.append(page)

        temp = frames + [-1] * (capacity - len(frames))
        print(f"{page} -> {display_frames(temp)}")

    return faults


# ---------------- Optimal ----------------
def optimal(pages, capacity):
    frames = []
    faults = 0

    print("\nOptimal Simulation:")
    for i in range(len(pages)):
        page = pages[i]

        if page not in frames:
            faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                future = pages[i + 1:]
                idx = -1
                farthest = -1

                for j in range(len(frames)):
                    if frames[j] not in future:
                        idx = j
                        break
                    else:
                        pos = future.index(frames[j])
                        if pos > farthest:
                            farthest = pos
                            idx = j

                frames[idx] = page

        temp = frames + [-1] * (capacity - len(frames))
        print(f"{page} -> {display_frames(temp)}")

    return faults


# ---------------- MRU ----------------
def mru(pages, capacity):
    frames = []
    faults = 0

    print("\nMRU Simulation:")
    for page in pages:
        if page not in frames:
            faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                frames.pop()  # remove most recently used
                frames.append(page)
        else:
            frames.remove(page)
            frames.append(page)

        temp = frames + [-1] * (capacity - len(frames))
        print(f"{page} -> {display_frames(temp)}")

    return faults


# ---------------- MAIN PROGRAM ----------------
def main():
    print("=== Page Replacement Simulator ===")

    # Task 1: Input
    capacity = int(input("Enter number of frames: "))
    pages = list(map(int, input("Enter page reference string (space-separated): ").split()))

    print("\nReference String:", pages)

    # Run algorithms
    fifo_faults = fifo(pages, capacity)
    lru_faults = lru(pages, capacity)
    opt_faults = optimal(pages, capacity)
    mru_faults = mru(pages, capacity)

    # Task 6: Comparison
    print("\n=== Performance Comparison ===")
    results = {
        "FIFO": fifo_faults,
        "LRU": lru_faults,
        "Optimal": opt_faults,
        "MRU": mru_faults
    }

    for algo, faults in results.items():
        print(f"{algo}: {faults} page faults")

    # Task 7: Analysis
    best = min(results, key=results.get)
    worst = max(results, key=results.get)

    print("\n=== Result Analysis ===")
    print(f"Best Algorithm: {best} (Minimum faults = {results[best]})")
    print(f"Worst Algorithm: {worst} (Maximum faults = {results[worst]})")

    print("\nConclusion:")
    print("- Optimal gives minimum faults (ideal case).")
    print("- LRU performs well due to temporal locality.")
    print("- FIFO is simple but may suffer from Belady’s anomaly.")
    print("- MRU works in special cases but usually performs worse.")


# Run program
main()
