# -------- FIFO --------
def fifo(pages, frames):
    memory = []
    faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            faults += 1

    print("\nFIFO Page Faults:", faults)


# -------- LRU (FIXED) --------
def lru(pages, frames):
    memory = []
    faults = 0
    recent = {}

    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                # find least recently used
                lru_page = min(memory, key=lambda x: recent[x])
                memory[memory.index(lru_page)] = page
            faults += 1
        recent[page] = i

    print("LRU Page Faults:", faults)


# -------- OPTIMAL --------
def optimal(pages, frames):
    memory = []
    faults = 0

    for i in range(len(pages)):
        if pages[i] not in memory:
            if len(memory) < frames:
                memory.append(pages[i])
            else:
                future = pages[i+1:]
                index = []

                for m in memory:
                    if m in future:
                        index.append(future.index(m))
                    else:
                        index.append(float('inf'))

                memory[index.index(max(index))] = pages[i]
            faults += 1

    print("Optimal Page Faults:", faults)


# -------- MRU (FIXED) --------
def mru(pages, frames):
    memory = []
    faults = 0
    recent = {}

    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                # replace most recently used
                mru_page = max(memory, key=lambda x: recent[x])
                memory[memory.index(mru_page)] = page
            faults += 1
        recent[page] = i

    print("MRU Page Faults:", faults)


# -------- MAIN --------
frames = int(input("Enter number of frames: "))
pages = list(map(int, input("Enter page reference string: ").split()))

fifo(pages, frames)
lru(pages, frames)
optimal(pages, frames)
mru(pages, frames)