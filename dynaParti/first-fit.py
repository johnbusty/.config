class First_fit:
    @staticmethod
    def firstFit(blockSize, m, processSize, n):
        allocation = [-1] * n
        for i in range(n):
            for j in range(m):
                if blockSize[j] >= processSize[i]:
                    blockSize[j] -= processSize[i]
                    allocation[i] = j
                    break
        print("\nProcess No.\tProcess Size\tBlock no.")
        for i in range(n):
            print(" " + str(i + 1) + "\t\t" + str(processSize[i]) + "\t\t", end="")
            if allocation[i] != -1:
                print(allocation[i] + 1)
            else:
                print("Not Allocated")
            print()

    @staticmethod
    def main():
        blockSize = [100, 500, 200, 300, 600]
        processSize = [212, 417, 112, 426]
        m = len(blockSize)
        n = len(processSize)
        First_fit.firstFit(blockSize, m, processSize, n)

First_fit.main() 