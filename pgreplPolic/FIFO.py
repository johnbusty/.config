from collections import deque

class FIFO:
    @staticmethod
    def pageFaults(pages, n, capacity):
        s = set()
        indexes = deque()
        page_faults = 0
        for i in range(n):
            if len(s) < capacity:
                if pages[i] not in s:
                    s.add(pages[i])
                    page_faults += 1
                    indexes.append(pages[i])
            else:
                if pages[i] not in s:
                    val = indexes[0]
                    indexes.popleft()
                    s.remove(val)
                    s.add(pages[i])
                    indexes.append(pages[i])
                    page_faults += 1
        return page_faults

    @staticmethod
    def main():
        pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
        capacity = 4
        print(FIFO.pageFaults(pages, len(pages), capacity))

FIFO.main()
