class bankers:
    def __init__(self):
        self.n = 5
        self.m = 3
        self.need = [[0 for j in range(self.m)] for i in range(self.n)]
        self.max = None
        self.alloc = None
        self.avail = None
        self.safeSequence = [0 for i in range(self.n)]

    def initializeValues(self):
        self.alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [1, 3, 5]]
        self.max = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [4, 2, 2], [7, 3, 3]]
        self.avail = [3, 3, 2]

    def isSafe(self):
        count = 0
        visited = [False for i in range(self.n)]
        work = self.avail.copy()
        while count < self.n:
            flag = False
            for i in range(self.n):
                if not visited[i]:
                    for j in range(self.m):
                        if self.need[i][j] > work[j]:
                            break
                    else:
                        self.safeSequence[count] = i
                        visited[i] = True
                        flag = True
                        for j in range(self.m):
                            work[j] += self.alloc[i][j]
                        count += 1
            if not flag:
                break
        if count < self.n:
            print("The System is UnSafe!")
        else:
            print("Following is the SAFE Sequence")
            for i in range(self.n):
                print("P" + str(self.safeSequence[i]), end="")
                if i != self.n - 1:
                    print(" -> ", end="")
            print()

    def calculateNeed(self):
        for i in range(self.n):
            for j in range(self.m):
                self.need[i][j] = self.max[i][j] - self.alloc[i][j]

if __name__ == "__main__":
    gfg = bankers()
    gfg.initializeValues()
    gfg.calculateNeed()
    gfg.isSafe()
