from collections import deque

def main():
    capacity = 4
    arr = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    s = deque(maxlen=capacity)
    count = 0
    page_faults = 0
    for i in arr:
        if i not in s:
            if len(s) == capacity:
                s.popleft()
                s.append(i)
            else:
                s.append(i)
            page_faults += 1
            count += 1
        else:
            s.remove(i)
            s.append(i)
    print(page_faults)

main()
