# Python code equivalent to the provided Java code

def waiting_time(n, bt, wt):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

def turnaround_time(n, bt, wt, tt):
    for i in range(n):
        tt[i] = bt[i] + wt[i]

def avg_wt_tt(n, bt):
    wt = [0] * n
    tt = [0] * n
    waiting_time(n, bt, wt)
    turnaround_time(n, bt, wt, tt)
    
    print("\nProcesses || Burst Time || Arrival Time || Waiting Time || Turn-Around Time ")
    awt = 0
    att = 0
    for i in range(n):
        awt += wt[i]
        att += tt[i]
        print(f"{i + 1}\t ||\t{bt[i]}\t||\t{wt[i]}\t||\t{tt[i]}")
    
    awt /= n
    att /= n
    print("\nAverage waiting time = ", awt)
    print("\nAverage turn around time = ", att)

# Main function
def main():
    n = int(input("Enter the number of processes: "))
    bt = [0] * 20
    print("\nEnter the Burst Time for each process.")
    for i in range(n):
        bt[i] = int(input(f"\nFor Process {i + 1}:"))
    avg_wt_tt(n, bt)

if __name__ == "__main__":
    main()

# Code 2 : Python equivalent for sjf Java class

def main_sjf():
    n = int(input("enter no of process:"))
    pid = [0] * n
    at = [0] * n
    bt = [0] * n
    ct = [0] * n
    ta = [0] * n
    wt = [0] * n
    f = [0] * n
    st = 0
    tot = 0
    avgwt = 0
    avgta = 0

    for i in range(n):
        print(f"enter process {i + 1} arrival time:")
        at[i] = int(input())
        pid[i] = i + 1
        f[i] = 0

    for i in range(n):
        print(f"enter process {i + 1} burst time:")
        bt[i] = int(input())

    while True:
        c = n
        min = 999
        if tot == n:
            break
        for i in range(n):
            if at[i] <= st and f[i] == 0 and bt[i] < min:
                min = bt[i]
                c = i
        if c == n:
            st += 1
        else:
            ct[c] = st + bt[c]
            st += bt[c]
            ta[c] = ct[c] - at[c]
            wt[c] = ta[c] - bt[c]
            f[c] = 1
            tot += 1

    print("\npid arrival burst complete turn waiting")
    for i in range(n):
        avgwt += wt[i]
        avgta += ta[i]
        print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{ta[i]}\t{wt[i]}")

    print("\naverage tat is ", (avgta / n))
    print("average wt is ", (avgwt / n))

if __name__ == "__main__":
    main_sjf()
